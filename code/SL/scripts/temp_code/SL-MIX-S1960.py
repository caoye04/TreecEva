from collections import defaultdict

# Daily sales records for pastries
pastry_sales = {
    'croissants': [12, 15, 9, 11],
    'muffins': [8, 10, 7, 13],
    'danish': [5, 6, 8, 4]
}

# Initialize counter for total pastries sold
pastry_counter = defaultdict(int)

# Aggregate weekly sales per pastry type
for pastry_type, daily_counts in pastry_sales.items():
    for count in daily_counts:
        pastry_counter[pastry_type] += count

# Calculate total bonus points (1 point for every 10 pastries sold)
total_bonus_points = 0
for count in pastry_counter.values():
    total_bonus_points += count // 10

print(f"Result: {total_bonus_points}")