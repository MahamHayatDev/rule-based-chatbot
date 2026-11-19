"""Terminal design: colors, banner, and message formatting."""

from colorama import Fore, Style, init

from chatbot.config import BOT_NAME, VERSION

init(autoreset=True)  # makes colors work on Windows

WIDTH = 56


def show_banner() -> None:
    line = "═" * WIDTH
    print(Fore.CYAN + Style.BRIGHT + f"╔{line}╗")
    print(Fore.CYAN + Style.BRIGHT + f"║{BOT_NAME + ' v' + VERSION:^{WIDTH}}║")
    print(Fore.CYAN + f"║{'Rule-Based AI Chatbot | DecodeLabs':^{WIDTH}}║")
    print(Fore.CYAN + Style.BRIGHT + f"╚{line}╝")
    print(Fore.WHITE + Style.DIM + "Type 'help' for options or 'bye' to exit.\n")


def user_prompt() -> str:
    return input(Fore.GREEN + Style.BRIGHT + "You  ▸ " + Style.RESET_ALL)


def bot_say(message: str) -> None:
    print(Fore.CYAN + Style.BRIGHT + f"{BOT_NAME} ▸ " + Style.RESET_ALL + message + "\n")


def system_say(message: str) -> None:
    print(Fore.YELLOW + message + "\n")