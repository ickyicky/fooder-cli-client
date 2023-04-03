from .client import FooderClient
from datetime import date
from rich.console import Console
from rich.table import Table


def print_diary(diary):
    table = Table(title="Diary for " + diary["date"])
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Grams", style="magenta")
    table.add_column("Protein", justify="right", style="green")
    table.add_column("Carb", justify="right", style="blue")
    table.add_column("Fat", justify="right", style="red")
    table.add_column("Kcal", justify="right", style="yellow")

    for meal in diary["meals"]:
        table.add_row(
            meal["name"],
            "",
            str(round(meal["protein"], 2)),
            str(round(meal["carb"], 2)),
            str(round(meal["fat"], 2)),
            str(round(meal["calories"], 2)),
        )
        for entry in meal["entries"]:
            table.add_row(
                "- " + entry["product"]["name"],
                str(round(entry["grams"], 2)),
                str(round(entry["protein"], 2)),
                str(round(entry["carb"], 2)),
                str(round(entry["fat"], 2)),
                str(round(entry["calories"], 2)),
            )
        table.add_section()

    table.add_row(
        "Total",
        "",
        str(round(diary["protein"], 2)),
        str(round(diary["carb"], 2)),
        str(round(diary["fat"], 2)),
        str(round(diary["calories"], 2)),
    )

    console = Console()
    console.print(table, justify="center")


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument(
        "--date",
        action="store",
        type=date.fromisoformat,
        default=date.today(),
        help="date of diary to view",
    )
    args = parser.parse_args()

    client = FooderClient()
    diary = client.get_diary(args.date)
    print_diary(diary)
