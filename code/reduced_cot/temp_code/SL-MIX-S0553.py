from collections import defaultdict

# Initial prices
prices = {'croissant': 2.50, 'muffin': 2.00, 'scone': 3.00}
# Daily sales counts for a week
sales_data = [
    {'croissant': 25, 'muffin': 15, 'scone': 30},
    {'croissant': 18, 'muffin': 22, 'scone': 10},
    {'croissant': 30, 'muffin': 12, 'scone': 25},
    {'croissant': 10, 'muffin': 30, 'scone': 20},
    {'croissant': 22, 'muffin': 25, 'scone': 15},
    {'croissant': 15, 'muffin': 10, 'scone': 35},
    {'croissant': 28, 'muffin': 20, 'scone': 18}
]

total_revenue = 0.0
for day_sales in sales_data:
    # Calculate revenue for current day
    for item, count in day_sales.items():
        total_revenue += count * prices[item]
    
    # Update prices for next day based on today's sales
    for item, count in day_sales.items():
        if count > 20:
            prices[item] *= 1.10  # 10% increase

print(f"Result: {total_revenue:.2f}")