# Online shop discount calculator

products = {
    'laptop': 850,
    'headphones': 120,
    'mouse': 45,
    'keyboard': 75,
    'monitor': 220
}

# Customer's shopping cart
cart = ['laptop', 'headphones', 'mouse']

# Get prices for items in cart
item_prices = [products[item] * 0.9 if item == 'laptop' else products[item] for item in cart]

# Apply loyalty discount to all items
discount_factor = 0.95
item_prices = [price * discount_factor for price in item_prices]

# Calculate shipping cost
shipping_base = 15
shipping_cost = max(0, shipping_base - len(cart))

# Calculate total cost
total_cost = sum(item_prices)

# Add shipping to final amount
final_amount = total_cost + shipping_cost

print(f"Total cost: {total_cost}")