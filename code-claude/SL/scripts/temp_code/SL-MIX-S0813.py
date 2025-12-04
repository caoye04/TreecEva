# Inventory management system
# Track unique product types across inventory and new shipment

inventory = {
    'shelf_1': 'electronics',
    'shelf_2': 'books',
    'shelf_3': 'toys',
    'shelf_4': 'electronics',
    'shelf_5': 'clothing'
}

new_shipment = {
    'box_1': 'clothing',
    'box_2': 'food',
    'box_3': 'toys',
    'box_4': 'stationery',
    'box_5': 'books'
}

# Count items in inventory
inventory_count = len(inventory)

# Calculate days until next shipment
days_remaining = (inventory_count * 2) % 7

# Track product categories that appear in both inventory and new shipment
unique_elements = len(set(inventory.values()) & set(new_shipment.values()))

# Final result
print(f"Result: {unique_elements}")