# Bookstore inventory management

# Dictionary of product names and their quantities in inventory
inventory = {
    'fiction': 12,
    'non_fiction': 8,
    'children': 15,
    'reference': 5
}

# Dictionary of product prices
item_prices = {
    'fiction': 12.99,
    'non_fiction': 15.50,
    'children': 8.75,
    'reference': 22.00
}

# Calculate some inventory statistics
total_books = sum(inventory.values())
avg_price = sum(item_prices.values()) / len(item_prices)

# Sort products by price (descending)
sorted_by_price = sorted(item_prices.keys(), key=lambda x: item_prices[x], reverse=True)

# Calculate the total inventory value
inventory_value = sum(item_prices[product] * inventory[product] for product in inventory)

# Format inventory report
report = f"Total books: {total_books}, Most expensive category: {sorted_by_price[0]}"

print(f"Result: {inventory_value}")