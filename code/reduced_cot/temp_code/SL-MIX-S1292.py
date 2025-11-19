from dataclasses import dataclass
from functools import reduce

@dataclass
class BakeryItem:
    name: str
    cost_price: float
    selling_price: float
    quantity_sold: int

items = [
    BakeryItem("Croissant", 1.5, 3.0, 30),
    BakeryItem("Baguette", 1.0, 2.5, 20),
    BakeryItem("Muffin", 0.8, 2.0, 25),
    BakeryItem("Cake", 5.0, 12.0, 8)
]

individual_profits = [(item.selling_price - item.cost_price) * item.quantity_sold for item in items]
filtered_profits = list(filter(lambda profit: profit > 20, individual_profits))
total_profit = reduce(lambda x, y: x + y, filtered_profits) if filtered_profits else 0

print(f"Result: {total_profit}")