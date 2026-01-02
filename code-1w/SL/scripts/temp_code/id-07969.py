from collections import Counter

# Inventory counts for two warehouses
warehouse_a = ['motor', 'valve', 'sensor', 'motor', 'pump', 'valve']
warehouse_b = ['valve', 'gear', 'motor', 'motor', 'sensor', 'gear']

# Count item occurrences in each warehouse
a_counts = Counter(warehouse_a)
b_counts = Counter(warehouse_b)

# Find items that appear in both warehouses
common_keys = set(a_counts.keys()) & set(b_counts.keys())

# Calculate minimum overlap quantity for each common item
overlap_count = 0
for item in common_keys:
    overlap_count += min(a_counts[item], b_counts[item])

# Redundant but harmless: count total unique items across both warehouses
total_unique = len(set(warehouse_a).union(set(warehouse_b)))

# The key result: number of common items (by type, not quantity)
common_items = common_keys

final_overlap = len(common_items)

print(f"Result: {final_overlap}")