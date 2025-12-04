from collections import Counter

products = ['apple', 'banana', 'orange', 'apple', 'grape', 'banana', 'apple', 'kiwi']
low_stock_threshold = 3

# Track inventory counts
inventory_counts = Counter(products)

# Check if any product needs restocking
needs_restock = False
for product, count in inventory_counts.items():
    if count < low_stock_threshold:
        needs_restock = True
        break

# Find the most stocked item
most_common_product = inventory_counts.most_common(1)[0][0]
most_common_count = inventory_counts.most_common(1)[0][1]

# Calculate total inventory
total_items = sum(inventory_counts.values())

# Calculate average stock per product type
average_stock = total_items / len(inventory_counts)

print(f"Result: {most_common_count}")