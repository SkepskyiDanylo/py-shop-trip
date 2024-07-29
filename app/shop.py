from math import sqrt

from app.customer import Customer


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_distance(self, customer: Customer) -> float:
        shop_x, shop_y = self.location
        customer_x, customer_y = customer.location
        distance = sqrt(
            ((shop_x - customer_x) ** 2)
            + ((shop_y - customer_y) ** 2))
        return distance

    def print_receipt(self, customer: Customer) -> None:
        print("\nDate: 04/01/2021 12:33:41")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        total_cost = 0
        for product, count in customer.product_cart.items():
            price = self.products[product] * count
            if price == int(price):
                price = int(price)
            print(f"{count} {product}s for {price} dollars")
            total_cost += price
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")
