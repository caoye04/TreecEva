# Inventory tracking system for a small bookstore

# Book prices in dollars
item_prices = {
    'fantasy_novel': 12.99,
    'mystery_novel': 14.50,
    'biography': 18.75,
    'cookbook': 22.99,
    'children_book': 9.99,
    'poetry': 11.25,
    'science_book': 16.50
}

# Current inventory count
inventory = {
    'fantasy_novel': 15,
    'mystery_novel': 12,
    'biography': 8,
    'cookbook': 10,
    'children_book': 20,
    'poetry': 5,
    'science_book': 7
}

# Items on sale (30% off)
sale_items = ['mystery_novel', 'cookbook', 'poetry']

# Calculate potential discount value (not used in final calculation)
total_discount = sum([item_prices[item] * inventory[item] * 0.3 for item in sale_items])
print(f"Total potential discount: ${total_discount:.2f}")

# Items we want to reorder soon
low_stock = [item for item in inventory if inventory[item] < 10]

# Calculate reorder cost (not used in final calculation)
reorder_quantity = 5
reorder_cost = sum([item_prices[item] * reorder_quantity for item in low_stock])
print(f"Reorder cost estimate: ${reorder_cost:.2f}")

# Check which categories have both high price and high inventory
premium_items = [item for item in inventory if item_prices[item] > 15.0 and inventory[item] > 5]
print(f"Premium items: {premium_items}")

# Find items that are both in stock and on sale
sale_and_available = [item for item in sale_items if inventory[item] > 0]
print(f"Items on sale and available: {sale_and_available}")

# Calculate shelf space needed (not used in final calculation)
space_per_book = 1.5  # inches
total_shelf_space = sum([inventory[item] * space_per_book for item in inventory])
print(f"Total shelf space needed: {total_shelf_space} inches")

# Find common items between premium and sale categories
common_items = [item for item in premium_items if item in sale_items]
print(f"Items that are both premium and on sale: {common_items}")

# Calculate the inventory value for these common items
inventory_value = sum([item_prices[item] * inventory[item] for item in common_items])
print(f"Result: {inventory_value}")