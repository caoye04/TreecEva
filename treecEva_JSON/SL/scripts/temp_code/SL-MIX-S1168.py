from itertools import product

# Daily sales counts
sales_counts = {'croissants': 5, 'muffins': 3, 'scones': 4}

# Price assignment using dictionary comprehension and switch logic
prices = {}
for item in sales_counts:
    match item:
        case 'croissants':
            prices[item] = 2.50
        case 'muffins':
            prices[item] = 2.00
        case 'scones':
            prices[item] = 1.75
        case _:
            prices[item] = 0

# Calculate total revenue before discount
total_revenue = sum(prices[item] * count for item, count in sales_counts.items())

# Apply 10% discount if total units sold > 10
total_units = sum(sales_counts.values())
if total_units > 10:
    final_revenue = total_revenue * 0.9
else:
    final_revenue = total_revenue

print(f"Result: {final_revenue}")