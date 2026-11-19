"""Central settings for the chatbot."""

BOT_NAME = "DecodeBot"
VERSION = "1.0.0"

# Commands that end the conversation (the "kill command")
EXIT_COMMANDS = {"exit", "quit", "bye", "goodbye", "q"}

# Default reply when no rule matches
FALLBACK_RESPONSE = (
    "I'm sorry, I don't understand that yet. "
    "Type 'help' to see what I can do."
)

GOODBYE_MESSAGE = "Goodbye! It was great chatting with you. Have a wonderful day!"