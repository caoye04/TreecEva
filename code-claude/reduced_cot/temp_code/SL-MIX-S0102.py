# Inventory management system for a small electronics store
# Calculating total value of selected items that aren't discontinued

inventory = {
    'A101': 299.99,  # Smartphone
    'B202': 149.50,  # Wireless headphones
    'C303': 899.00,  # Laptop
    'D404': 79.95,   # Wireless charger
    'E505': 199.50,  # Smartwatch
    'F606': 599.99,  # Tablet
    'G707': 49.99    # Phone case
}

# Items that are discontinued (can't be sold)
is_discontinued = {
    'A101': False,
    'B202': True,
    'C303': False,
    'D404': False,
    'E505': True,
    'F606': False,
    'G707': False
}

# Customer's selected items
selected_items = ['A101', 'C303', 'E505', 'G707']

# Calculate potential revenue if all selected items were available
potential_revenue = sum(inventory[item] for item in selected_items)

# Apply 10% discount for bulk purchases (not relevant to final calculation)
discount_rate = 0.1
discounted_potential = potential_revenue * (1 - discount_rate)

# Count number of discontinued items selected
discontinued_count = sum(1 for item in selected_items if is_discontinued[item])

# Calculate shipping cost based on item count (not used in final calculation)
base_shipping = 15
shipping_cost = base_shipping + (len(selected_items) - discontinued_count) * 2.5

# Calculate the actual inventory value for selected items that aren't discontinued
filtered_inventory_value = sum(item_price for item_id, item_price in inventory.items() 
                              if item_id in selected_items and not is_discontinued[item_id])

# Apply tax to the filtered inventory value (not part of final answer)
tax_rate = 0.08
taxed_value = filtered_inventory_value * (1 + tax_rate)

print(f"Result: {filtered_inventory_value}")