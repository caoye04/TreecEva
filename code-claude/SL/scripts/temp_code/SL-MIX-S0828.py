# Inventory management system for a small bookstore

# Product catalog with prices
item_prices = {
    'novel': 12.99,
    'textbook': 49.95,
    'magazine': 5.99,
    'comic': 8.50,
    'dictionary': 24.75,
    'cookbook': 18.50
}

# Current inventory quantities
inventory = {
    'novel': 35,
    'textbook': 12,
    'magazine': 48,
    'comic': 53,
    'dictionary': 8,
    'cookbook': 15
}

# Sales data from last week
last_week_sales = {
    'novel': 7,
    'textbook': 3,
    'magazine': 22,
    'comic': 12,
    'dictionary': 2,
    'cookbook': 5
}

# Calculate total items in inventory
total_items = sum(inventory.values())

# Find highest and lowest priced items
max_price_item = max(item_prices, key=item_prices.get)
min_price_item = min(item_prices, key=item_prices.get)

# Process sales data
avg_sale_price = sum(item_prices[item] * last_week_sales[item] for item in last_week_sales) / sum(last_week_sales.values())

# Filter items that need restocking (less than 20 in inventory)
low_stock_items = [item for item in inventory if inventory[item] < 20]

# Select items for valuation (items with at least 10 in stock and price above $10)
selected_items = [item for item in inventory if inventory[item] >= 10 and item_prices[item] > 10]

# Calculate value of selected inventory
inventory_value = sum(item_prices[k] * inventory[k] for k in selected_items)

# Calculate potential revenue from all items
potential_revenue = sum(item_prices[k] * inventory[k] for k in inventory)

# Display results
print(f"Average sale price: ${avg_sale_price:.2f}")
print(f"Items needing restock: {', '.join(low_stock_items)}")
print(f"Total inventory value of selected items: ${inventory_value:.2f}")
