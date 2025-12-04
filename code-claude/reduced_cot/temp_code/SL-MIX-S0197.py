# Inventory Management System Analysis

def calculate_metrics(data):
    # Calculate some inventory metrics (not used in final result)
    avg_price = sum(item['price'] for item in data) / len(data)
    max_quantity = max(item['quantity'] for item in data)
    min_quantity = min(item['quantity'] for item in data)
    return avg_price, max_quantity, min_quantity

# Sample inventory data
inventory = [
    {'id': 101, 'name': 'Laptop', 'price': 1200, 'quantity': 5},
    {'id': 102, 'name': 'Phone', 'price': 800, 'quantity': 10},
    {'id': 103, 'name': 'Tablet', 'price': 350, 'quantity': 8},
    {'id': 104, 'name': 'Monitor', 'price': 250, 'quantity': 12},
    {'id': 105, 'name': 'Keyboard', 'price': 50, 'quantity': 25}
]

# Process inventory data
inventory_values = {}
out_of_stock_items = set()
excess_inventory = {}

# Calculate inventory values and identify special items
for item in inventory:
    # Check if item is potentially out of stock (not used in final calculation)
    if item['quantity'] < 3:
        out_of_stock_items.add(item['id'])
    
    # Check for excess inventory (not used in final calculation)
    if item['quantity'] > 20:
        excess_inventory[item['id']] = item['quantity']
    
    # Calculate value for each item
    item_value = item['price'] * item['quantity']
    
    # Add 10% tax to electronics over $500 (distractor calculation)
    if item['price'] > 500:
        tax_rate = 0.10
        tax_amount = item['price'] * tax_rate
        adjusted_price = item['price'] + tax_amount
        # This adjusted price isn't actually used
    
    # Store the inventory value
    inventory_values[item['id']] = item_value

# Calculate some metrics (distractor)
avg_price, max_qty, min_qty = calculate_metrics(inventory)

# Apply a discount to the inventory values (not actually applied)
discount_factor = 0.05
discounted_values = {k: v * (1 - discount_factor) for k, v in inventory_values.items()}

# Calculate the total inventory value
total_inventory_value = sum(inventory_values.values())

# Calculate potential savings from discounts (distractor)
potential_savings = sum(inventory_values.values()) - sum(discounted_values.values())

print(f"Result: {total_inventory_value}")