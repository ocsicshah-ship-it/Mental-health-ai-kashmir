"""Thin wrapper around the Anthropic API."""

import os

from anthropic import Anthropic

from app.prompts import SYSTEM_PROMPT

_client: Anthropic | None = None


def get_client() -> Anthropic:
    global _client
    if _client is None:
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise RuntimeError("ANTHROPIC_API_KEY is not set. Copy .env.example to .env.")
        _client = Anthropic(api_key=api_key)
    return _client


def get_reply(messages: list[dict]) -> str:
    """messages: [{"role": "user"|"assistant", "content": str}, ...]"""
    response = get_client().messages.create(
        model=os.environ.get("CLAUDE_MODEL", "claude-sonnet-4-6"),
        max_tokens=int(os.environ.get("MAX_TOKENS", "1024")),
        system=SYSTEM_PROMPT,
        messages=messages,
    )
    return response.content[0].text
