from collections import Counter

# Warehouse inventory management
item_counts = Counter({'widgets': 15, 'gadgets': 8, 'tools': 12, 'parts': 6})
warehouse_capacity = 50
current_stock = sum(item_counts.values())

# Calculate inventory metrics
inventory_total = sum(item_counts.values())
available_space = warehouse_capacity - current_stock

print(f"Result: {inventory_total}")