# Inventory analysis for an online store
products = ['Apple Watch', 'Samsung Galaxy', 'airpods', 'Bluetooth Speaker', 'ANDROID Tablet', 'Laptop Stand']

# Count total number of products
total_count = len(products)

# Convert all product names to lowercase for better filtering
lowercase_products = [p.lower() for p in products]

# Filter products starting with 'a'
product_count = len([p for p in products if p.lower().startswith("a")])

# Calculate percentage of 'a' products
percentage = (product_count / total_count) * 100

# Display results
print(f"Total products: {total_count}")
print(f"Products starting with 'A': {product_count}")
print(f"Percentage: {percentage:.1f}%")

# Result: {product_count}