def analyze_inventory(products, sales_data):
    # Calculate inventory metrics
    inventory_status = {}
    for product, quantity in products.items():
        # Track if product is low on stock
        inventory_status[product] = quantity < 10
        
    # Process sales data
    total_sales = sum(sales_data.values())
    avg_sale = total_sales / len(sales_data) if sales_data else 0
    
    # Calculate product popularity scores
    popularity = {}
    price_data = {}
    for product, data in sales_data.items():
        # Track pricing information separately
        unit_price = data * 0.8 if inventory_status.get(product, False) else data * 0.75
        price_data[product] = round(unit_price, 2)
        
        # Calculate popularity score (higher is better)
        popularity[product] = data / avg_sale if avg_sale > 0 else 0
    
    # Find best product based on popularity
    best_product = max(popularity.items(), key=lambda x: x[1])[0] if popularity else None
    second_best = sorted(popularity.items(), key=lambda x: x[1], reverse=True)[1][0] if len(popularity) > 1 else None
    
    # Calculate potential revenue from best products
    potential_revenue = price_data.get(best_product, 0) * 1.5
    alternative_revenue = price_data.get(second_best, 0) * 1.3 if second_best else 0
    
    # Determine optimal price point
    optimal_price = price_data.get(best_product, 0)
    
    # Display results
    print(f"Total sales: {total_sales}")
    print(f"Best product: {best_product}")
    print(f"Potential revenue: {potential_revenue}")
    print(f"Result: {optimal_price}")
    
    return total_sales

# Inventory data
products = {
    "widget_a": 15,
    "widget_b": 8,
    "widget_c": 23
}

# Sales data (units sold)
sales_data = {
    "widget_a": 120,
    "widget_b": 85,
    "widget_c": 40
}

analyze_inventory(products, sales_data)