from collections import Counter

daily_sales = Counter({'bread': 45, 'croissant': 30, 'muffin': 25, 'cookie': 15})
prices = {'bread': 2.50, 'croissant': 3.00, 'muffin': 2.00, 'cookie': 1.50}

total_items = sum(daily_sales.values())
total_revenue = sum(daily_sales[item] * prices[item] for item in daily_sales)

if total_items > 100:
    total_revenue *= 0.9

final_revenue = int(total_revenue * 100)  # Convert to cents for precise integer handling
print(f'Result: {final_revenue}')