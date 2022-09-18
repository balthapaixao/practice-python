class StripePaymentHandler:
    def handle_payment(self, amount: float) -> None:
        print(f"Charging $ { amount/100:.2f} using Stripe")

PRICES = {
    "burger":10_00,
    "fries":5_00,
    "drink":2_00,
    "dessert":3_00,
    "salad":15_00,
}

def order_food(items: list[str]) -> None:
    total = sum(PRICES[item] for item in items)
    print(f"Your total is ${total/100:.2f}")
    payment_handler = StripePaymentHandler()
    payment_handler.handle_payment(total)
    print("Thank you for your order!")

def main() -> None:
    order_food(["salad", "dessert", "drink"])

if __name__ == "__main__":
    main()