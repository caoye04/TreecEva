def inventory_analysis(products, threshold=50):
    # Initialize inventory tracking
    low_stock = set()
    available_products = set()
    
    # Process inventory data
    for product_id, quantity in products.items():
        # Track products with quantity below threshold
        if quantity < threshold:
            low_stock.add(product_id)
        
        # Process based on product ID characteristics
        if product_id % 5 == 0:
            # Premium products (divisible by 5)
            premium_factor = 1.15
            adjusted_quantity = int(quantity * premium_factor)
            if adjusted_quantity > threshold:
                available_products.add(product_id)
        elif product_id % 3 == 0:
            # Promotional products (divisible by 3)
            promo_discount = 0.9
            discounted_quantity = quantity
            if discounted_quantity >= threshold // 2:
                available_products.add(product_id)
        else:
            # Regular products
            if quantity >= threshold:
                available_products.add(product_id)
    
    # Calculate metrics
    total_products = len(products)
    low_stock_ratio = len(low_stock) / total_products if total_products > 0 else 0
    
    # Filter out products that are both in low stock and available
    special_case = [p for p in low_stock if p in available_products]
    
    # Determine final availability count
    valid_items = len(available_products)
    
    potential_restocks = total_products - valid_items
    
    print(f"Result: {valid_items}")
    return valid_items

# Sample inventory data: product_id -> quantity
product_inventory = {
    101: 75,  # Regular product, sufficient quantity
    102: 30,  # Regular product, insufficient quantity
    103: 65,  # Promotional product
    105: 40,  # Premium product, adjusted quantity is sufficient
    106: 25,  # Regular product, insufficient quantity
    110: 55,  # Premium product
    115: 35,  # Premium product, adjusted quantity is sufficient
    120: 90   # Premium product
}

# Run inventory analysis
result = inventory_analysis(product_inventory)
