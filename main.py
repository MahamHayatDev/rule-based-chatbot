"""Entry point: the chatbot's heartbeat (infinite loop)."""

from chatbot.config import GOODBYE_MESSAGE
from chatbot.processor import get_response, is_exit, sanitize
from chatbot.ui import bot_say, show_banner, system_say, user_prompt


def main() -> None:
    show_banner()

    while True:
        try:
            raw_input = user_prompt()
        except (KeyboardInterrupt, EOFError):
            print()
            bot_say(GOODBYE_MESSAGE)
            break

        clean_input = sanitize(raw_input)

        if not clean_input:                # user just pressed Enter
            system_say("Please type something.")
            continue

        if is_exit(clean_input):           # kill command
            bot_say(GOODBYE_MESSAGE)
            break

        bot_say(get_response(clean_input))


if __name__ == "__main__":
    main()