from collections import Counter

# Daily sales data
pastry_sales = Counter({'croissant': 25, 'muffin': 18, 'danish': 30, 'scone': 12})
prices = {'croissant': 3.50, 'muffin': 2.75, 'danish': 4.00, 'scone': 2.25}

# Sort pastries alphabetically
sorted_pastries = sorted(pastry_sales.keys())

# Calculate total revenue
total_revenue = sum(pastry_sales[pastry] * prices[pastry] for pastry in sorted_pastries)

print(f'Result: {total_revenue}')