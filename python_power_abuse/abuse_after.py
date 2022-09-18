from enum import Enum
from typing import Protocol


class PaymentMethod(Enum):
    PAYPAL="paypal"
    CARD='stripe'

class Payment(Protocol):
    def pay(self, amount: float) -> None:
        ...

class PayPalPayment(Payment):
    def pay(self, amount: float) -> None:
        print(f"Charging ${amount/100:.2f} using PayPal")

class StripePayment(Payment):
    def pay(self, amount: float) -> None:
        print(f"Charging ${amount/100:.2f} using Stripe")

PAYMENT_METHODS = dict[PaymentMethod, type[Payment]] = {
    PaymentMethod.CARD: StripePayment,
    PaymentMethod.PAYPAL: PayPalPayment,
}

def main() -> None:
    payment = PAYMENT_METHODS[PaymentMethod.PAYPAL]()
    if payment:
        payment.pay(50.5)

if __name__ == "__main__":
    main()