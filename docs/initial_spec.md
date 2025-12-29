# Initial MVP Spec (Draft)

## Goal
Start with conversation log upload, basic todo extraction response, and a simple health check.

## MVP Entities (Draft)
- users: id, name, email, created_at
- conversations: id, user_id, source, raw_text, created_at
- todos: id, user_id, conversation_id, title, due_date, status, created_at

## API Draft
- `GET /health`
  - Returns service health status.
- `POST /conversations/upload`
  - Accepts a conversation log payload.
  - Returns a generated `conversation_id`.
- `POST /analysis/todos`
  - Accepts `conversation_id` plus `raw_text`.
  - Returns extracted todo list (initially empty).

## Next Steps
- Define request/response schemas.
- Add storage (PostgreSQL).
- Implement NLP extraction.

## Current Implementation Notes
- Alembic migrations added for `users`, `conversations`, `todos`.
- Todo extraction uses 20 simple keyword-based rules as a placeholder.
- `DATABASE_URL` 환경 변수를 통해 DB 연결을 설정한다.
