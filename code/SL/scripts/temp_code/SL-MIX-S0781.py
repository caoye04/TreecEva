# Inventory management system
product_categories = ['electronics', 'clothing', 'books', 'home_goods']
category_weights = [0.15, 0.25, 0.35, 0.25]
initial_stock = [120, 85, 200, 150]
restock_amounts = [30, 15, 50, 25]

# Calculate current product counts
product_counts = []
for initial, restock in zip(initial_stock, restock_amounts):
    current_count = initial + restock
    product_counts.append(current_count)

# Compute total inventory across all categories
total_inventory = sum(product_counts)

# Final output
print(f"Total inventory: {total_inventory}")