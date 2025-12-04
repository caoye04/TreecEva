def calculate_inventory_stats(products):
    # Track inventory metrics
    inventory_count = 0
    low_stock_items = []
    premium_items = {}
    
    # Process inventory data
    for product_id, details in products.items():
        # Count items in inventory
        inventory_count += details['quantity']
        
        # Track low stock items (less than 5)
        if details['quantity'] < 5:
            low_stock_items.append(product_id)
        
        # Track premium items (price > 50)
        if details['price'] > 50:
            premium_items[product_id] = details['price']
    
    # Calculate inventory values
    inventory_values = []
    potential_revenue = 0
    for product_id, details in products.items():
        # Calculate value of each product line
        line_value = details['price'] * details['quantity']
        inventory_values.append(line_value)
        
        # Calculate potential revenue with full sales
        markup = details.get('markup', 0.2)  # Default markup of 20%
        potential_revenue += line_value * (1 + markup)
    
    # Calculate average price per item (not used in final result)
    avg_price = sum([details['price'] for _, details in products.items()]) / len(products)
    
    # Calculate total inventory value
    total_inventory_value = sum(inventory_values)
    
    # Estimated shipping costs (not used in final calculation)
    shipping_estimate = inventory_count * 2.5
    
    print(f"Result: {total_inventory_value}")
    return total_inventory_value

# Inventory data: product_id -> {price, quantity, markup}
products = {
    'A001': {'price': 25, 'quantity': 10, 'markup': 0.3},
    'B002': {'price': 40, 'quantity': 5, 'markup': 0.25},
    'C003': {'price': 100, 'quantity': 2, 'markup': 0.4},
    'D004': {'price': 15, 'quantity': 20, 'markup': 0.15}
}

calculate_inventory_stats(products)