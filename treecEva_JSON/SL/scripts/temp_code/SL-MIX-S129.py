from dataclasses import dataclass

@dataclass
class Pastry:
    name: str
    price: float
    units_sold: int

# Daily sales report
sales_data = {
    'croissant': Pastry('croissant', 2.5, 45),
    'muffin': Pastry('muffin', 3.0, 67),
    'danish': Pastry('danish', 3.5, 120),
    'scone': Pastry('scone', 2.0, 34)
}

top_seller_units = 0
for item_name, pastry in sales_data.items():
    if pastry.units_sold > 100:
        top_seller_units = pastry.units_sold
        break
    elif pastry.units_sold > top_seller_units:
        top_seller_units = pastry.units_sold

print(f"Result: {top_seller_units}")