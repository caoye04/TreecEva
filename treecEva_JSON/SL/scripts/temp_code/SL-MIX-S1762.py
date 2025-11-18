from dataclasses import dataclass

@dataclass
class BakeryItem:
    name: str
    price: float

items = {
    'croissant': BakeryItem('croissant', 2.50),
    'muffin': BakeryItem('muffin', 3.00),
    'scone': BakeryItem('scone', 2.00)
}

quantities_sold = {
    'croissant': 40,
    'muffin': 25,
    'scone': 30
}

total_revenue = sum(quantities_sold[item] * items[item].price for item in quantities_sold)
print(f"Total revenue: {total_revenue}")