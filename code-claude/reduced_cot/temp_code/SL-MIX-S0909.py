def calculate_inventory_value(items):
    total = 0
    # Calculate total inventory value
    for item, details in items.items():
        total += details['quantity'] * details['price']
    
    # Apply discount for bulk purchases
    discount_factor = 0.95 if total > 1000 else 1.0
    return total * discount_factor

# Warehouse inventory tracking system
inventory = {
    'widget_a': {'quantity': 15, 'price': 45, 'location': 'Shelf A'},
    'widget_b': {'quantity': 30, 'price': 25, 'location': 'Shelf B'},
    'gadget_x': {'quantity': 10, 'price': 65, 'location': 'Shelf C'}
}

# Compute inventory stats
total_items = sum(item['quantity'] for item in inventory.values())
max_price = max(item['price'] for item in inventory.values())
inventory_value = calculate_inventory_value(inventory)

# Security level calculation
security_codes = ('admin', 'manager', 'staff')
user_type = security_codes[1]  # Current user is a manager

# Generate inventory fingerprint using bitwise operations
base_hash = 0
for item_name, details in inventory.items():
    item_hash = details['quantity'] & 0xFF
    base_hash = (base_hash << 4) | item_hash

# Normalize hash to a smaller range
inventory_hash = base_hash % 256

# Calculate access level based on user type
access_level = security_codes.index(user_type) * 16

# Generate verification code (this is actually unnecessary for the result)
verification = (inventory_value > 1500) + (total_items > 50)

# Final security hash combines inventory hash and access level
final_hash = inventory_hash ^ access_level
print(f"Result: {final_hash}")