# Inventory management system for an electronics store
# Each product has: (name, price, quantity, category)

inventory = [
    ("Smartphone X", 599.99, 15, "mobile"),
    ("Laptop Pro", 1299.99, 8, "computer"),
    ("Wireless Earbuds", 89.99, 30, "audio"),
    ("Smart Watch", 249.99, 12, "wearable"),
    ("Tablet Mini", 349.99, 20, "mobile"),
    ("Bluetooth Speaker", 79.99, 25, "audio"),
    ("Gaming Console", 399.99, 10, "gaming"),
    ("Wireless Mouse", 29.99, 40, "computer"),
    ("External SSD", 119.99, 18, "storage"),
    ("Wireless Charger", 39.99, 35, "accessories")
]

# Process inventory data
def analyze_inventory(items, target_category=None):
    total_value = 0
    low_stock_items = []
    category_counts = {}
    
    # Calculate various statistics
    for i, item in enumerate(items):
        name, price, quantity, category = item
        
        # Track total inventory value (not used in final calculation)
        item_value = price * quantity
        total_value += item_value
        
        # Track low stock items (not used in final calculation)
        if quantity < 15:
            low_stock_items.append(name)
            
        # Count items by category (partially used later)
        if category in category_counts:
            category_counts[category] += 1
        else:
            category_counts[category] = 1
    
    # Process inventory based on categories
    filtered_inventory = []
    for name, price, quantity, category in items:
        # Filter items (this affects the final result)
        if target_category is None or category == target_category:
            filtered_inventory.append((name, price, quantity))
    
    # Calculate average price (not used in final calculation)
    avg_price = sum(item[1] for item in filtered_inventory) / len(filtered_inventory) if filtered_inventory else 0
    
    # Sort by price (not used in final calculation)
    sorted_by_price = sorted(filtered_inventory, key=lambda x: x[1])
    
    # Find products above minimum price threshold
    min_price = 100
    valid_products = len([p for p in filtered_inventory if p[1] > min_price])
    
    # Calculate potential revenue (not used in final calculation)
    potential_revenue = sum(p[1] * p[2] for p in filtered_inventory)
    
    return valid_products

# Analyze inventory for mobile products
result = analyze_inventory(inventory, "mobile")
print(f"Result: {result}")