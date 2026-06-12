# CLAUDE.md

Guidance for Claude Code when working in this repository.

## Project

Sukoon — a mental health support chatbot for people in Kashmir, powered by the
Claude API. FastAPI backend, single-page HTML/JS frontend, no database
(conversations are kept client-side only, by design, for privacy).

## Commands

```bash
pip install -r requirements.txt          # install deps
cp .env.example .env                     # then add ANTHROPIC_API_KEY
uvicorn app.main:app --reload            # run dev server at http://localhost:8000
pytest                                   # run tests (no API key needed)
```

## Architecture

- `app/main.py` — FastAPI app. `POST /api/chat` takes full message history,
  returns `{reply, crisis, helplines}`. Serves `static/index.html` at `/`.
- `app/claude_client.py` — Anthropic SDK wrapper. Model/max_tokens from env.
- `app/prompts.py` — the system prompt (persona: "Sukoon"). All behavioral
  tuning of the bot happens here.
- `app/safety.py` — regex crisis detection (English + romanized Urdu) as a
  guaranteed safety net independent of the model; when tripped, the API
  response carries helpline numbers and the frontend pins them visibly.
- `static/index.html` — entire frontend: chat UI, history kept in JS memory,
  sends last 30 messages per request.
- `tests/test_app.py` — endpoint validation + crisis detection tests. They do
  not call the Claude API.

## Conventions and constraints

- Privacy first: never add server-side storage/logging of conversation content
  without explicit instruction.
- Safety: do not weaken or remove crisis detection or the helpline surfacing.
  Canonical helpline data lives in `config/crisis-resources.json`; corrections
  that must never regress are in `docs/corrections-register.md` (e.g. KIRAN is
  merged into Tele-MANAS — never list it as a standalone line; Kashmir Lifeline
  is time-gated Sun–Thu 10am–5pm).
- The production spec lives in `prompts/system-prompt.md`, `safety/`, `consent/`
  and `docs/` — treat those as the source of truth; `app/` is a prototype.
- The system prompt must keep: not-a-therapist disclaimer, crisis protocol,
  cultural/faith sensitivity, multilingual support (English/Urdu/Hindi/Kashmiri).
- Python 3.10+, type hints, pydantic models for all API I/O.
- Keep the frontend dependency-free (no build step, no frameworks).
- Run `pytest` before committing.
