from .client import get_client, UnathorizedError
from .diary import print_diary, get_diary
from .entry import adding_loop
from .meal import create_meal, select_meal
from .product import add_product
from getpass import getpass
from datetime import date
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text
from rich import print


def login(client) -> None:
    username = input("Username: ")
    password = getpass("Password: ")
    client.login(username, password)


def main() -> None:
    client = get_client()
    diary = None
    meal = None

    actions = [
        (1, "Show diary"),
        (2, "Add entry to diary"),
        (3, "Add meal to diary"),
        (4, "Add product"),
        (5, "Switch to another day"),
        (6, "Switch to another meal"),
        (0, "Login"),
    ]
    text = Text()

    for action in actions:
        text.append(f"{action[0]}. ", style="bold blue")
        text.append(action[1])
        text.append("\n")

    panel = Panel(
        text,
        title="Fooder",
        expand=False,
    )

    while True:
        try:
            print(panel)
            action = int(
                Prompt.ask(
                    "Choose action", default=1, choices=[str(i) for i, _ in actions]
                )
            )

            if action == 0:
                login(client)
                continue

            if diary is None:
                diary = get_diary(client)

            if action == 1:
                print_diary(diary)
            elif action == 2:
                if meal is None:
                    meal = select_meal(diary)
                adding_loop(client, meal)
            elif action == 3:
                meal = create_meal(client, diary)
            elif action == 4:
                add_product(client)
            elif action == 5:
                day = Prompt.ask("Specify date for diary you wanna switch to")
                day = date.fromisoformat(day)
                diary = get_diary(client, day)
                print_diary(diary)
            elif action == 6:
                meal = select_meal(diary)

        except UnathorizedError:
            print("[red]You are unathorized, please login:")
            login(client)
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()
