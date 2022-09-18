class Payment:
    def __new__(cls, payment_type: str):
        if payment_type == "paypal":
            return object.__new__(PayPalPayment)
        elif payment_type == "stripe":
            return object.__new__(StripePayment)
    
    def pay(self, amount: float) -> None:
        raise NotImplementedError

class PayPalPayment(Payment):
    def pay(self, amount: float) -> None:
        print(f"Charging ${amount/100:.2f} using PayPal")

class StripePayment(Payment):
    def pay(self, amount: float) -> None:
        print(f"Charging ${amount/100:.2f} using Stripe")

def main() -> None:
    payment = Payment("paypal")
    if payment:
        payment.pay(50.5)
    

if __name__ == "__main__":
    main()