# Inventory management system for a small electronics store

# Available inventory with product_id as key and quantity as value
inventory = {
    'A123': 45,  # Smartphones
    'B456': 30,  # Headphones
    'C789': 15,  # Chargers
    'D012': 20   # Power banks
}

# Dictionary of pending orders (product_id: quantity)
orders = {
    'B456': 12,  # Regular order
    'E345': 5,   # Out of stock item
    'C789': 3    # Special order
}

# Calculate space needed in the shipping area
shipping_area = sum(inventory.values()) // 10

# Customer is looking for product with ID 'C789'
product_id = 'C789'

# Calculate items that will remain after fulfilling all orders for this product
remaining_stock = inventory.get(product_id, 0) - sum(orders.values())

# Track minimum stock level
min_stock_level = min(inventory.values()) - 5

# Get products that need reordering (less than 20 in stock)
reorder_products = {k for k, v in inventory.items() if v < 20}

# Calculate total value of inventory assuming each item costs $10
inventory_value = sum(inventory.values()) * 10

print(f"Result: {remaining_stock}")