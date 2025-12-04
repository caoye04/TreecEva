# Inventory Management System Valuation

def calculate_tax(price):
    # Calculate tax at 8.5%
    return price * 0.085

# Initial inventory with item_id: [quantity, price_per_unit]
inventory = {
    'A123': [15, 24.99],
    'B456': [8, 59.95],
    'C789': [12, 12.50],
    'D012': [20, 9.99]
}

# New shipments to be added to inventory
shipments = {
    'A123': 5,
    'B456': 3,
    'E345': 10,  # New item
    'F678': 7    # New item
}

# Prices for new items
new_prices = {
    'E345': 34.50,
    'F678': 19.99,
    'G901': 45.00  # Item not in shipment, distractor
}

# Record of items sold
sales = [
    ('A123', 8),
    ('B456', 2),
    ('C789', 5),
    ('E345', 4)
]

# Discount percentages for certain items
discounts = {
    'A123': 10,  # 10% discount
    'C789': 15,  # 15% discount
    'F678': 5    # 5% discount
}

# Update inventory with shipments
for item_id, quantity in shipments.items():
    if item_id in inventory:
        inventory[item_id][0] += quantity
    else:
        if item_id in new_prices:
            inventory[item_id] = [quantity, new_prices[item_id]]

# Process sales
for item_id, quantity_sold in sales:
    if item_id in inventory and inventory[item_id][0] >= quantity_sold:
        inventory[item_id][0] -= quantity_sold

# Calculate tax amounts for reporting (not used in valuation)
tax_amounts = {}
for item_id, (quantity, price) in inventory.items():
    tax_amounts[item_id] = calculate_tax(price * quantity)

# Calculate shipping costs (distractor)
shipping_base = 25
shipping_per_item = 0.5
total_items = sum(quantity for quantity, _ in inventory.values())
shipping_cost = shipping_base + (shipping_per_item * total_items)

# Calculate total value of each item type
total_item_values = {}
for item_id, (quantity, price) in inventory.items():
    # Apply discounts if applicable
    if item_id in discounts:
        discount_factor = 1 - (discounts[item_id] / 100)
        item_value = quantity * price * discount_factor
    else:
        item_value = quantity * price
    
    total_item_values[item_id] = round(item_value, 2)

# Calculate final inventory value
final_inventory_value = sum(total_item_values.values())

# Calculate average item price (distractor)
average_price = sum(price for _, price in inventory.values()) / len(inventory)

print(f"Total inventory value: ${final_inventory_value:.2f}")
print(f"Average price per item type: ${average_price:.2f}")
