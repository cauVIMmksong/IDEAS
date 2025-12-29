from datetime import datetime
from uuid import uuid4

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from .database import SessionLocal
from .models import Conversation, Todo, User
from .schemas import (
    ConversationUploadRequest,
    ConversationUploadResponse,
    TodoExtractionRequest,
    TodoExtractionResponse,
)
from .todo_rules import extract_todos

app = FastAPI(title="Couple Planner API", version="0.1.0")


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}


@app.post("/conversations/upload", response_model=ConversationUploadResponse)
def upload_conversation(
    payload: ConversationUploadRequest, db: Session = Depends(get_db)
) -> ConversationUploadResponse:
    user = db.get(User, payload.user_id)
    if user is None:
        user = User(id=payload.user_id)
        db.add(user)
    conversation = Conversation(
        id=f"conv_{uuid4().hex[:12]}",
        user_id=payload.user_id,
        source=payload.source,
        raw_text=payload.raw_text,
    )
    db.add(conversation)
    db.commit()
    return ConversationUploadResponse(
        conversation_id=conversation.id,
        received_at=conversation.created_at,
    )


@app.post("/analysis/todos", response_model=TodoExtractionResponse)
def analyze_todos(
    payload: TodoExtractionRequest, db: Session = Depends(get_db)
) -> TodoExtractionResponse:
    conversation = db.get(Conversation, payload.conversation_id)
    todos = extract_todos(payload.raw_text)
    if conversation:
        for todo in todos:
            db.add(
                Todo(
                    id=f"todo_{uuid4().hex[:12]}",
                    user_id=conversation.user_id,
                    conversation_id=payload.conversation_id,
                    title=todo.title,
                    due_date=todo.due_date,
                )
            )
        db.commit()
    return TodoExtractionResponse(todos=todos)
