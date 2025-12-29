# Couple Planner MVP

This repository starts the MVP for a couple-focused planner that ingests conversation logs,
extracts todos, and later expands into recommendations and notifications.

## Structure
- `server/`: FastAPI backend (initial endpoints)
- `client/`: Frontend placeholder
- `docs/`: Draft specs

## Quick start (backend)
```bash
cd server
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## API quick check
```bash
curl http://127.0.0.1:8000/health
curl -X POST http://127.0.0.1:8000/conversations/upload \
  -H "Content-Type: application/json" \
  -d '{"user_id":"user_123","raw_text":"다음주 토요일 전시회 가자"}'
```
