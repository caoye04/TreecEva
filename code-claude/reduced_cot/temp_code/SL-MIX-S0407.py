import itertools

# Inventory tracking system for a small electronics store
# Each product has an ID, quantity, and price
products = [
    {'id': 101, 'name': 'USB Cable', 'quantity': 25, 'price': 12},
    {'id': 203, 'name': 'Wireless Mouse', 'quantity': 10, 'price': 45},
    {'id': 157, 'name': 'Keyboard', 'quantity': 5, 'price': 60},
    {'id': 289, 'name': 'Headphones', 'quantity': 15, 'price': 30},
    {'id': 342, 'name': 'Monitor', 'quantity': 8, 'price': 180}
]

# Filter products based on inventory threshold
inventory_threshold = 12
filtered_products = [product['price'] for product in products if product['quantity'] > inventory_threshold]

# Calculate the total price of filtered products
filtered_sum = sum(product for product in filtered_products)

# Display the result
print(f"Result: {filtered_sum}")