from .client import FooderClient


if __name__ == "__main__":
    client = FooderClient()
    diary = client.get_diary()
    meals = diary["meals"]

    if len(meals) > 1:
        print(
            "\n".join(["{}: {}".format(meal["order"], meal["name"]) for meal in meals])
        )
        meal_order = input("Choose meal: ")
        try:
            meal_id = [
                meal["id"] for meal in meals if meal["order"] == int(meal_order)
            ][0]
        except:
            print("Invalid meal selected")
            exit(1)
    else:
        meal_id = meals[0]["id"]

    product_q = input("Enter product name: ")
    products = client.list_products(query=product_q)["products"]
    if len(products) == 0:
        print("No products found")
        exit(1)
    elif len(products) == 1:
        product_id = products[0]["id"]
    else:
        print(
            "\n".join(
                [
                    "{}: {}".format(product["id"], product["name"])
                    for product in products
                ]
            )
        )
        product_id = int(input("Choose product: "))
        assert product_id in [product["id"] for product in products]

    grams = float(input("Enter grams: "))
    client.add_entry(product=product_id, grams=grams, meal=meal_id)
