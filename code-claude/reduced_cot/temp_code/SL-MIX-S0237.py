# Inventory management system for a small grocery store
# Track stock levels and calculate inventory value

# Initialize product inventory with item:quantity pairs
inventory = {'apples': 45, 'bananas': 23, 'oranges': 19, 'grapes': 12}

# Price lookup dictionary (price per unit)
prices = {'apples': 0.75, 'bananas': 0.60, 'oranges': 0.80, 'grapes': 2.50}

# Calculate total items in inventory
total_items = sum(inventory.values())
print(f"Total items in inventory: {total_items}")

# Create a dictionary with item values (quantity * price)
inventory_items = {}
for item, quantity in inventory.items():
    if item in prices:
        inventory_items[item] = quantity * prices[item]

# Items to order (when quantity falls below 20)
to_order = [item for item, qty in inventory.items() if qty < 20]
print(f"Items to order: {to_order}")

# Calculate total inventory value
inventory_value = sum(inventory_items.values())

# Apply 5% tax to get final value
final_value = inventory_value * 1.05

print(f"Inventory value: ${inventory_value:.2f}")
print(f"Final value with tax: ${final_value:.2f}")