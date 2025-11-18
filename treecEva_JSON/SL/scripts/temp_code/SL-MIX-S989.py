from collections import defaultdict

item_prices = {'bread': 2.5, 'cake': 15.0, 'cookie': 1.2}
sales_count = {'bread': 20, 'cake': 5, 'cookie': 50}

total_revenue = 0
revenue_components = {item: price * sales_count[item] for item, price in item_prices.items() if item in sales_count}

for item, revenue in revenue_components.items():
    if revenue > 10:
        total_revenue += revenue
    else:
        total_revenue += revenue * 0.9  # 10% discount for low-revenue items

print(f"Result: {total_revenue}")