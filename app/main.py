"""FastAPI app: serves the chat UI and the /api/chat endpoint."""

from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from app import claude_client
from app.safety import HELPLINES, detect_crisis

app = FastAPI(title="Sukoon — Mental Health Support for Kashmir")

STATIC_DIR = Path(__file__).resolve().parent.parent / "static"

MAX_HISTORY = 30  # keep request size bounded


class ChatMessage(BaseModel):
    role: str = Field(pattern="^(user|assistant)$")
    content: str = Field(min_length=1, max_length=4000)


class ChatRequest(BaseModel):
    messages: list[ChatMessage] = Field(min_length=1, max_length=MAX_HISTORY)


class ChatResponse(BaseModel):
    reply: str
    crisis: bool
    helplines: list[dict]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/api/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    if req.messages[-1].role != "user":
        raise HTTPException(400, "Last message must be from the user.")

    crisis = detect_crisis(req.messages[-1].content)
    try:
        reply = claude_client.get_reply([m.model_dump() for m in req.messages])
    except RuntimeError as e:
        raise HTTPException(500, str(e))

    return ChatResponse(reply=reply, crisis=crisis, helplines=HELPLINES if crisis else [])


@app.get("/")
def index():
    return FileResponse(STATIC_DIR / "index.html")


app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
