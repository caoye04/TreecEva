import itertools

# Product inventory with prices and categories
inventory = {
    'apple': {'price': 1.20, 'category': 'fruit'},
    'banana': {'price': 0.50, 'category': 'fruit'},
    'carrot': {'price': 0.80, 'category': 'vegetable'},
    'potato': {'price': 1.10, 'category': 'vegetable'},
    'orange': {'price': 0.90, 'category': 'fruit'},
    'broccoli': {'price': 1.70, 'category': 'vegetable'},
    'grapes': {'price': 2.50, 'category': 'fruit'}
}

# Filter products by category and price threshold
category_filter = 'fruit'  # We want fruits
price_threshold = 1.00     # Below or equal to this price

# Extract prices of products meeting our criteria
all_prices = [details['price'] for item, details in inventory.items()]

# Apply filters to get fruits with price <= threshold
filtered_prices = [details['price'] for item, details in inventory.items() 
                  if details['category'] == category_filter and details['price'] <= price_threshold]

# Calculate the average price of filtered products
average_price = sum(filtered_prices) / len(filtered_prices) if filtered_prices else 0

# Round to 2 decimal places for display
display_price = round(average_price, 2)

print(f"Result: {average_price}")