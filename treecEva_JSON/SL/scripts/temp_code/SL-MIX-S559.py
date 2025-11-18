from collections import defaultdict

# Daily sales count
sales_count = {'croissants': 15, 'baguettes': 8, 'muffins': 20}

# Prices (in dollars)
prices = {'croissants': 3.50, 'baguettes': 2.25, 'muffins': 1.75}

# Greedy algorithm: process highest price items first
total_revenue = 0
sorted_items = sorted(prices.items(), key=lambda x: x[1], reverse=True)

for item, price in sorted_items:
    total_revenue += sales_count[item] * price

print(f'Result: {total_revenue}')