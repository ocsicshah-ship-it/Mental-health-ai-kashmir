"""Lightweight crisis-signal detection.

This is a safety net layered on top of the model's own crisis handling:
if a message trips these patterns, the API response includes helpline info
so the frontend can pin it visibly regardless of what the model says.
"""

import re

CRISIS_PATTERNS = [
    r"\bsuicid",
    r"\bkill (myself|my self)\b",
    r"\bend (my|this) life\b",
    r"\bwant to die\b",
    r"\bself[- ]?harm",
    r"\bhurt myself\b",
    r"\bno reason to live\b",
    r"khudkushi",          # Urdu/Hindi: suicide
    r"khatam kar(na|un)",  # "end it"
    r"marna chahta",       # "want to die"
    r"marna chahti",
]

_CRISIS_RE = re.compile("|".join(CRISIS_PATTERNS), re.IGNORECASE)

HELPLINES = [
    {"name": "Tele-MANAS (24x7, free, Urdu/Hindi/English)", "phone": "14416"},
    {"name": "Tele-MANAS toll-free", "phone": "1800-891-4416"},
    {"name": "Kiran Helpline (24x7)", "phone": "1800-599-0019"},
]


def detect_crisis(text: str) -> bool:
    return bool(_CRISIS_RE.search(text))
