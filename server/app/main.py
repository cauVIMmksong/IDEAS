from datetime import datetime
from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Couple Planner API", version="0.1.0")


class ConversationUploadRequest(BaseModel):
    user_id: str = Field(..., examples=["user_123"])
    source: Literal["upload"] = "upload"
    raw_text: str = Field(..., min_length=1)


class ConversationUploadResponse(BaseModel):
    conversation_id: str
    received_at: datetime


class TodoExtractionRequest(BaseModel):
    conversation_id: str
    raw_text: str = Field(..., min_length=1)


class TodoItem(BaseModel):
    title: str
    due_date: datetime | None = None


class TodoExtractionResponse(BaseModel):
    todos: list[TodoItem]


_CONVERSATIONS: dict[str, ConversationUploadRequest] = {}


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}


@app.post("/conversations/upload", response_model=ConversationUploadResponse)
def upload_conversation(payload: ConversationUploadRequest) -> ConversationUploadResponse:
    conversation_id = f"conv_{len(_CONVERSATIONS) + 1}"
    _CONVERSATIONS[conversation_id] = payload
    return ConversationUploadResponse(
        conversation_id=conversation_id,
        received_at=datetime.utcnow(),
    )


@app.post("/analysis/todos", response_model=TodoExtractionResponse)
def analyze_todos(payload: TodoExtractionRequest) -> TodoExtractionResponse:
    _ = payload
    return TodoExtractionResponse(todos=[])
