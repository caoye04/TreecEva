# Calculate average price of products that meet minimum rating threshold

# Product data: (name, price, rating)
products = [
    ("Laptop", 899.99, 4.5),
    ("Smartphone", 649.95, 4.2),
    ("Headphones", 129.50, 3.9),
    ("Monitor", 249.75, 4.7),
    ("Keyboard", 89.99, 4.0),
    ("Mouse", 45.50, 3.8)
]

# Minimum rating threshold
min_rating = 4.0

# Filter products by rating
filtered_products = [product for product in products if product[2] >= min_rating]

# Sort products by price (not needed for calculation, but useful for display)
sorted_products = sorted(filtered_products, key=lambda x: x[1])

# Calculate average price of filtered products
average_price = round(sum(map(lambda p: p[1], filtered_products)) / len(filtered_products), 2)

# Number of products above average price
above_average = len([p for p in filtered_products if p[1] > average_price])

print(f"Result: {average_price}")