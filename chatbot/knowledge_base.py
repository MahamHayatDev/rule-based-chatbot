"""Knowledge base: every intent the bot understands.

Each intent has a list of trigger phrases (patterns) and one response.
INTENTS is flattened into RESPONSES so lookups are O(1) with a dict.
"""

INTENTS = {
    "greeting": {
        "patterns": ["hello", "hi", "hey", "good morning", "good evening"],
        "response": "Hello! Welcome. How can I help you today?",
    },
    "how_are_you": {
        "patterns": ["how are you", "how are you doing", "how r u"],
        "response": "I'm running at 100% efficiency. Thanks for asking! How are you?",
    },
    "identity": {
        "patterns": ["who are you", "what is your name", "your name"],
        "response": "I'm DecodeBot, a rule-based AI chatbot built with Python.",
    },
    "help": {
        "patterns": ["help", "what can you do", "commands"],
        "response": (
            "I can greet you, tell you about myself, share a joke, "
            "and answer basic questions. Type 'bye' to exit."
        ),
    },
    "thanks": {
        "patterns": ["thanks", "thank you", "thx"],
        "response": "You're welcome! Happy to help.",
    },
    "joke": {
        "patterns": ["joke", "tell me a joke", "make me laugh"],
        "response": "Why do programmers prefer dark mode? Because light attracts bugs!",
    },
    "purpose": {
        "patterns": ["what is a rule based chatbot", "how do you work"],
        "response": (
            "I follow explicit rules: I clean your input, look it up in a "
            "dictionary, and reply with the matching response."
        ),
    },
}

# Flatten: {"hello": "Hello! ...", "hi": "Hello! ...", ...}
RESPONSES = {
    pattern: intent["response"]
    for intent in INTENTS.values()
    for pattern in intent["patterns"]
}