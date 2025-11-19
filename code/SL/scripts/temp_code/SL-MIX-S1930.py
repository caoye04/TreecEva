from collections import defaultdict

# Daily sales data
pastry_sales = {'croissants': 15, 'muffins': 8, 'danish': 12, 'scones': 5}

# Apply Monday promotion rule
reported_sales = defaultdict(int)
for pastry, count in pastry_sales.items():
    if count > 10:
        reported_sales[pastry] = count * 2
    else:
        reported_sales[pastry] = count

# Calculate total reported sales
total_reported = sum(reported_sales.values())

print(f"Result: {total_reported}")