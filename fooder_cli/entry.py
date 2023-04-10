from .client import get_client
from .meal import select_meal
from .product import select_product
from .diary import get_diary, print_diary
from rich.prompt import Prompt, Confirm
from rich.table import Table
from rich.text import Text


def add_entry(client, meal, product):
    data = {
        "meal_id": meal["id"],
        "product_id": product["id"],
        "grams": float(Prompt.ask("Enter grams")),
    }
    response = client.post("/entry", data=data)
    return response


def adding_loop(client, meal):
    add_another = True
    while add_another:
        product = select_product(client)
        if product is not None:
            add_entry(client, meal, product)
            print_diary(get_diary(client))
        add_another = Confirm.ask("Add another entry?", default=False)


if __name__ == "__main__":
    client = get_client()

    diary = get_diary(client)
    meal = select_meal(diary)
    adding_loop(client, meal)
