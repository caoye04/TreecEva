# Calculate total cost of eligible products in an online shopping cart

products = [
    {"name": "Headphones", "price": 89.99, "eligible": True},
    {"name": "Mouse", "price": 24.50, "eligible": False},
    {"name": "Keyboard", "price": 45.75, "eligible": True},
    {"name": "Monitor", "price": 199.99, "eligible": True},
    {"name": "USB Cable", "price": 8.25, "eligible": False}
]

all_prices = [item["price"] for item in products]

# Calculate average price of all products
avg_price = sum(all_prices) / len(all_prices)

# Get prices of eligible products only
filtered_prices = [item["price"] for item in products if item["eligible"]]

# Sum the filtered prices
filtered_sum = sum(filtered_prices)

# Apply a 10% discount for orders over 300
final_price = filtered_sum * 0.9 if filtered_sum > 300 else filtered_sum

print(f"Result: {filtered_sum}")