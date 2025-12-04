from collections import Counter

# Store inventory tracking system
inventory_items = {'apple', 'banana', 'orange', 'grape', 'kiwi', 'pear', 'mango'}
inventory_count = Counter({'apple': 15, 'banana': 8, 'orange': 12, 'grape': 20})

# Customer purchase history
customer_history = ['apple', 'orange', 'apple', 'banana', 'kiwi']
customer_purchases = set(customer_history)

# Calculate metrics
total_items = sum(inventory_count.values())
average_stock = total_items / len(inventory_count)

# Find products that appear in both customer purchases and inventory
unique_products = len(customer_purchases & inventory_items)

# Display results
print(f"Total inventory items: {total_items}")
print(f"Average stock per product: {average_stock}")
print(f"Result: {unique_products}")