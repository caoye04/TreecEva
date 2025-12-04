import itertools

def calculate_remaining_inventory(sales_data, initial_inventory):
    # Track products that need restocking
    restock_alerts = []
    
    # Calculate remaining inventory
    remaining = {}
    total_value = 0
    
    for product, quantity in initial_inventory.items():
        sold = sales_data.get(product, 0)
        remaining[product] = max(0, quantity - sold)
        
        # Calculate value based on product pricing
        if product.startswith('electronics'):
            product_value = remaining[product] * 150
        elif product.startswith('clothing'):
            product_value = remaining[product] * 45
        else:
            product_value = remaining[product] * 25
            
        total_value += product_value
        
        # Check if restocking needed (not used in final calculation)
        if remaining[product] < 5:
            restock_alerts.append(product)
    
    # Group products by category using itertools (not used in final calculation)
    categories = {}
    for product in remaining:
        category = product.split('_')[0]
        if category not in categories:
            categories[category] = []
        categories[category].append(product)
    
    # Find products with same inventory count (not used in final calculation)
    inventory_counts = {}
    for product, count in remaining.items():
        if count not in inventory_counts:
            inventory_counts[count] = []
        inventory_counts[count].append(product)
        
    # Calculate average remaining inventory
    if remaining:
        avg_remaining = sum(remaining.values()) / len(remaining)
    else:
        avg_remaining = 0
    
    # Return the count of items with inventory below average
    below_average_count = sum(1 for count in remaining.values() if count < avg_remaining)
    
    # Return final inventory count
    return sum(remaining.values())

# Initial inventory levels
initial_stock = {
    'electronics_laptop': 15,
    'electronics_phone': 30,
    'clothing_shirt': 45,
    'clothing_pants': 25,
    'books_fiction': 50,
    'books_nonfiction': 35
}

# Sales data
product_sales = {
    'electronics_laptop': 10,
    'electronics_phone': 25,
    'clothing_shirt': 15,
    'clothing_pants': 10,
    'books_fiction': 20,
    'books_nonfiction': 15
}

# Calculate shipping costs (not used in final calculation)
shipping_zones = ['local', 'regional', 'international']
shipping_rates = [5, 15, 30]
shipping_options = list(itertools.product(shipping_zones, [True, False]))
shipping_cost = sum(rate for zone, rate in zip(shipping_zones, shipping_rates))

# Calculate the remaining inventory
final_inventory = calculate_remaining_inventory(product_sales, initial_stock)

print(f"Result: {final_inventory}")