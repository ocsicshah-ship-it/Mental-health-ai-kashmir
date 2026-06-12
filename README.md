# Sukoon — Mental Health AI for Kashmir

A culturally-aware mental wellness companion for people in Kashmir, built on the
Claude API. Supportive listening, coping strategies, and crisis-helpline
surfacing — in English, Urdu, Hindi, or Kashmiri.

**Not a replacement for professional care.** In crisis, call Tele-MANAS
**14416** (24x7, free) or Kiran **1800-599-0019**.

## Quick start

```bash
git clone https://github.com/ocsicshah-ship-it/Mental-health-ai-kashmir.git
cd Mental-health-ai-kashmir
pip install -r requirements.txt
cp .env.example .env   # add your ANTHROPIC_API_KEY (console.anthropic.com)
uvicorn app.main:app --reload
```

Open http://localhost:8000 and start talking.

## Features

- Claude-powered conversation with a Kashmir-specific, faith-respecting system prompt
- Independent crisis keyword detection (English + romanized Urdu) that pins
  helpline numbers in the UI regardless of model output
- Privacy by design: no server-side storage; history lives in the browser tab
- Zero-build frontend, single FastAPI backend file — easy to extend

## Project layout

```
app/
  main.py           FastAPI app + /api/chat endpoint
  claude_client.py  Anthropic SDK wrapper
  prompts.py        System prompt (the bot's persona and rules)
  safety.py         Crisis detection + helplines
static/index.html   Chat UI
tests/              pytest suite (runs without an API key)
CLAUDE.md           Instructions for Claude Code
```

## Developing with Claude Code

This repo is set up for [Claude Code](https://docs.claude.com/en/docs/claude-code):
`CLAUDE.md` gives it the architecture, commands, and safety constraints.
Just run `claude` in the repo root.

## Tests

```bash
pytest
```

## License

MIT
