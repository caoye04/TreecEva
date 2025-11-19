from collections import defaultdict

pastry_prices = {'croissant': 3.5, 'muffin': 2.0, 'danish': 4.0, 'scone': 2.5}
weekly_sales = {'croissant': 25, 'muffin': 15, 'danish': 30, 'scone': 10}

total_revenue = 0.0
for pastry, count in weekly_sales.items():
    price = pastry_prices[pastry]
    if count > 20:
        # Apply 10% discount for high-selling items
        total_revenue += count * price * 0.9
    else:
        total_revenue += count * price

print(f"Result: {total_revenue}")