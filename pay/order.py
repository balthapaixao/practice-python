from dataclasses import dataclass
from enum import Enum

class OrderStatus(Enum):
    OPEN = "open"
    PAID = "paid"

@dataclass
class LineItem:
    name:str
    price:float
    quantity:int=1

    @property
    def total(self) -> float:
        return self.quantity * self.price

@dataclass
class Order:
    line_items: list[LineItem] = field(default_factory=list)
    status: OrderStatus = OrderStatus.OPEN

    @property
    def total(self) -> float:
        return sum(item.total for item in self.line_items)

    def pay(self) -> None:
        if self.status != OrderStatus.OPEN:
            raise ValueError("Cannot pay for an order that is not open")
        self.status = OrderStatus.PAID