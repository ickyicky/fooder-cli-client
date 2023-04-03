from .client import FooderClient


if __name__ == "__main__":
    client = FooderClient()
    diary = client.get_diary()
    meals = diary["meals"]

    name = input("Enter meal name: ")
    order = max([meal["order"] for meal in meals]) + 1
    client.create_meal(diary_id=diary["id"], name=name, order=order)
