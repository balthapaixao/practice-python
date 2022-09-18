from pay.card import CreditCard
from pay.order import Order


class PaymentProcessor:
    def charge(self, card: CreditCard, amount: float) -> None:
        """Charge the card for the amount."""


def pay_order(order: Order,
              payment_processor: PaymentProcessor,
              card: CreditCard) -> None:
    if order.total == 0:
        raise ValueError("Cannot pay for an order with total 0.")
    payment_processor.charge(card, amount=order.total)
    order.pay()
