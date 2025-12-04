# Inventory management for a small bookstore

inventory = {
    'fiction': 12,
    'non_fiction': 8,
    'children': 15,
    'reference': 3,
    'poetry': 7
}

# Check if any category needs restocking (less than 5 books)
needs_restock = False
for category, stock in inventory.items():
    if stock < 5:
        needs_restock = True
        
# Calculate total inventory
total_inventory = sum(inventory.values()) // 2 if any(stock < 5 for stock in inventory.values()) else sum(inventory.values())

# Calculate average stock per category
avg_stock = sum(inventory.values()) / len(inventory)

# Display results
print(f"Total inventory: {total_inventory}")
print(f"Average stock: {avg_stock:.2f}")