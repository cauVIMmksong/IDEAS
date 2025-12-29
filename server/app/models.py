from __future__ import annotations

from datetime import datetime
from uuid import uuid4

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    name: Mapped[str | None] = mapped_column(String(120))
    email: Mapped[str | None] = mapped_column(String(200), unique=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    conversations: Mapped[list["Conversation"]] = relationship(back_populates="user")


class Conversation(Base):
    __tablename__ = "conversations"

    id: Mapped[str] = mapped_column(String(64), primary_key=True, default=lambda: f"conv_{uuid4().hex[:12]}")
    user_id: Mapped[str] = mapped_column(String(64), ForeignKey("users.id"))
    source: Mapped[str] = mapped_column(String(40), default="upload")
    raw_text: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    user: Mapped["User"] = relationship(back_populates="conversations")
    todos: Mapped[list["Todo"]] = relationship(back_populates="conversation")


class Todo(Base):
    __tablename__ = "todos"

    id: Mapped[str] = mapped_column(String(64), primary_key=True, default=lambda: f"todo_{uuid4().hex[:12]}")
    user_id: Mapped[str] = mapped_column(String(64), ForeignKey("users.id"))
    conversation_id: Mapped[str] = mapped_column(String(64), ForeignKey("conversations.id"))
    title: Mapped[str] = mapped_column(String(240))
    due_date: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    status: Mapped[str] = mapped_column(String(20), default="pending")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    conversation: Mapped["Conversation"] = relationship(back_populates="todos")
