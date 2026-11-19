# 🤖 DecodeBot: Rule-Based AI Chatbot

A deterministic, rule-based chatbot built in Python. It cleans user input, matches it against a dictionary-based knowledge base, and replies in a continuous loop until the user exits.

Built for **DecodeLabs | Artificial Intelligence | Project 1**.

## Features

- **Continuous input loop**: runs on a `while True` cycle with a clean exit command
- **Input sanitization**: handles case, extra whitespace, and punctuation (`"  HELLO!! "` → `"hello"`)
- **Dictionary knowledge base**: 7 intents and 22 trigger phrases with O(1) lookup
- **Fallback response**: a graceful reply for anything the bot doesn't understand
- **Colored terminal UI**: banner and styled messages using `colorama`
- **Unit tested**: 10 tests with Python's built-in `unittest`

## Architecture (IPO Model)

```
Input → Sanitization → Dictionary Lookup (.get) → Response → Loop
```

## Project Structure

```
rule-based-chatbot/
├── chatbot/
│   ├── config.py           # bot name, exit commands, fallback text
│   ├── knowledge_base.py   # intents and responses
│   ├── processor.py        # sanitize, exit check, response lookup
│   └── ui.py               # terminal design
├── tests/
│   └── test_processor.py   # unit tests
├── main.py                 # entry point (the main loop)
├── requirements.txt
└── README.md
```

## Setup

```bash
git clone https://github.com/MahamHayatDev/rule-based-chatbot.git
cd rule-based-chatbot
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Run the Tests

```bash
python -m unittest discover -s tests -v
```

## Example Session

```
You  ▸ HELLO!!
DecodeBot ▸ Hello! Welcome. How can I help you today?

You  ▸ pizza
DecodeBot ▸ I'm sorry, I don't understand that yet. Type 'help' to see what I can do.

You  ▸ bye
DecodeBot ▸ Goodbye! It was great chatting with you. Have a wonderful day!
```

## Add Your Own Intent

Open `chatbot/knowledge_base.py` and add an entry to `INTENTS`:

```python
"weather": {
    "patterns": ["weather", "is it raining"],
    "response": "I can't check live weather yet, but I hope it's sunny!",
},
```

## Future Improvements

- Hybrid mode: pass unmatched questions to an LLM
- Semantic matching with embeddings instead of exact matches
- Conversation memory and nested conditions

## Author

Built by [Maham Shaukat](https://github.com/MahamHayatDev).