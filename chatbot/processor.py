"""Core logic: clean the user's input and find a response."""

import re

from chatbot.config import EXIT_COMMANDS, FALLBACK_RESPONSE
from chatbot.knowledge_base import RESPONSES


def sanitize(raw_input: str) -> str:
    """Normalize input: lowercase, remove punctuation, collapse spaces, trim."""
    text = raw_input.lower()
    text = re.sub(r"[^\w\s]", "", text)   # remove punctuation like ! ? .
    text = re.sub(r"\s+", " ", text)      # "hello    there" -> "hello there"
    return text.strip()                    # trim last, after all removals


def is_exit(clean_input: str) -> bool:
    """Return True if the user wants to quit."""
    return clean_input in EXIT_COMMANDS


def get_response(clean_input: str) -> str:
    """Dictionary lookup with a fallback, in one atomic operation."""
    return RESPONSES.get(clean_input, FALLBACK_RESPONSE)