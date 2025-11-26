# Inventory management system
inventory_items = ['laptop', 'mouse', 'keyboard', 'monitor', 'mouse', 'keyboard']
sold_items = ['mouse', 'monitor', 'headphones', 'webcam']

# Convert to sets for comparison
inventory_set = set(inventory_items)
sold_set = set(sold_items)

# Find items that are exclusively in one set or the other
unique_items = len(inventory_set ^ sold_set)

print(f"Result: {unique_items}")