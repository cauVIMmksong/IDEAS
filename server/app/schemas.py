from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


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
