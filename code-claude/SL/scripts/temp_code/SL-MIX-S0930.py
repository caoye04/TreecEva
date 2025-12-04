# Inventory management system for a small bookstore

# Dictionary of all book prices in the store
item_prices = {
    'fantasy_novel': 12.99,
    'sci_fi_anthology': 15.50,
    'mystery_paperback': 9.99,
    'biography': 22.50,
    'cookbook': 18.75,
    'poetry_collection': 11.25,
    'history_tome': 24.99,
    'reference_guide': 35.00
}

# Current inventory quantities
quantities = {
    'fantasy_novel': 15,
    'sci_fi_anthology': 8,
    'mystery_paperback': 12,
    'biography': 5,
    'cookbook': 10,
    'reference_guide': 3
}

# Books currently on display (active items)
active_items = ['fantasy_novel', 'mystery_paperback', 'cookbook', 'poetry_collection']

# Books on order (not yet arrived)
backordered_items = ['sci_fi_anthology', 'reference_guide']

# Seasonal discount percentages
seasonal_discounts = {
    'fantasy_novel': 0.10,  # 10% off
    'biography': 0.15,      # 15% off
    'cookbook': 0.05        # 5% off
}

# Calculate potential revenue from backordered items
potential_revenue = sum(item_prices[item] * quantities.get(item, 0) for item in backordered_items)

# Calculate average price of active books
active_prices = [item_prices[item] for item in active_items if item in item_prices]
display_avg_price = sum(active_prices) / len(active_prices) if active_prices else 0

# Sort books by price (descending)
sorted_by_price = sorted(item_prices.items(), key=lambda x: x[1], reverse=True)

# Find most expensive book
most_expensive = sorted_by_price[0][0] if sorted_by_price else None

# Calculate discount values
discount_values = {item: round(item_prices[item] * discount, 2) 
                  for item, discount in seasonal_discounts.items() 
                  if item in active_items}

# Total discount amount if applied to active inventory
total_discount = sum(discount_values.get(item, 0) * quantities.get(item, 0) 
                    for item in active_items)

# Calculate inventory value of active items
inventory_value = sum(item_prices[item] * quantities.get(item, 0) for item in active_items)

# Apply discount to get final inventory value
discounted_value = inventory_value - total_discount

# Print results for verification
print(f"Active inventory items: {', '.join(active_items)}")
print(f"Average price of active books: ${display_avg_price:.2f}")
print(f"Most expensive book: {most_expensive}")
print(f"Potential revenue from backordered items: ${potential_revenue:.2f}")
print(f"Total discount amount: ${total_discount:.2f}")
print(f"Result: {inventory_value}")