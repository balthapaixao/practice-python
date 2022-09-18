from datetime import datetime
from pay.card import CreditCard



class PaymentProcessor:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def _check_api_key(self) -> bool:
        return self.api_key == "ab12-34cd-56ef-78gh"

    def charge(self, card: CreditCard, amount:float) -> None:
        if not self.validate_card(card):
            raise ValueError("Invalid card")
        if not self._check_api_key():
            raise ValueError("Invalid API key", self.api_key)
        if amount <= 0:
            raise ValueError("Amount must be positive")
        print(f"Charging {amount} to {card.number}")

    def validate_card(self, card: CreditCard) -> bool:
        return (luhn_checksum(card.number) 
                and datetime(card.expiry_year, 
                             card.expiry_month,
                            1) > datetime.now())

def luhan_checksum(card_number: str) -> bool:
    def digits_of(card_number: str) -> list[int]:
        return [int(d) for d in card_number]

    digits = [int(d) for d in card_number]
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for digit in even_digits:
        checksum += sum(digits_of(str(digit * 2)))
    return checksum % 10 == 0