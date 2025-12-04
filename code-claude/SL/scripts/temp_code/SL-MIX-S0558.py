from collections import Counter

# Analyzing inventory data from two warehouse locations
warehouse_a = ['laptop', 'tablet', 'phone', 'tablet', 'laptop', 'speaker', 'headphones', 'phone']
warehouse_b = ['monitor', 'laptop', 'phone', 'tablet', 'keyboard', 'mouse', 'phone', 'laptop']

# Count product occurrences in each warehouse
product_count = Counter(warehouse_a)

# Find items that appear in both warehouses
common_items = set(warehouse_a) & set(warehouse_b)

# Calculate total inventory value
total_value = len(warehouse_a) + len(warehouse_b)

# Calculate how many of the common products we have in warehouse A
common_product_count = sum(product_count[item] for item in common_items)

print(f"Result: {common_product_count}")