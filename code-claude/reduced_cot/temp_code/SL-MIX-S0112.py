# Calculate average price of selected products after discount

products = [('Laptop', 1200), ('Headphones', 150), ('Mouse', 25), ('Keyboard', 80), ('Monitor', 300)]
selected_indices = [0, 2, 4]  # Indices of products to include
discount_percent = 15  # 15% discount

# Extract selected products using slicing and list comprehension
selected_products = [products[i] for i in selected_indices]

# Apply discount and calculate final prices
final_prices = []
for name, price in selected_products:
    discounted_price = price * (1 - discount_percent / 100)
    final_prices.append(discounted_price)

# Calculate the average price of selected products
average_price = round(sum(final_prices) / len(final_prices), 2)

# Track inventory status (not relevant for the calculation)
inventory_status = ['In Stock' if i % 2 == 0 else 'Low Stock' for i, _ in enumerate(products)]

print(f"Result: {average_price}")