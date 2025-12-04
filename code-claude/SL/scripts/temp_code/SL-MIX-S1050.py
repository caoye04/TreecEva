def calculate_inventory_metrics(products):
    # Process inventory data
    total_value = 0
    filtered_products = []
    alternative_products = {}
    
    # Calculate various metrics
    for product_id, details in products.items():
        # Track total inventory value
        price = details['price']
        quantity = details['quantity']
        total_value += price * quantity
        
        # Filter products based on quantity
        if quantity > 5:
            filtered_products.append(product_id)
            
        # Generate alternative product mapping (not used in final calculation)
        if 'alternative' in details:
            alternative_products[product_id] = details['alternative']
    
    # Calculate popularity scores based on review counts
    review_threshold = 10
    scores = {}
    for product_id in filtered_products:
        review_count = products[product_id].get('reviews', 0)
        quality_factor = products[product_id].get('quality', 3)
        
        # Complex scoring algorithm
        base_score = review_count * 0.8
        if review_count > review_threshold:
            base_score += 5
        
        # Apply quality multiplier
        scores[product_id] = base_score * (quality_factor / 3)
    
    # Calculate average score (this is our target calculation)
    product_score = sum(scores.values()) / len(filtered_products)
    
    # Some additional unused calculations for intervention
    avg_price = sum(products[pid]['price'] for pid in filtered_products) / len(filtered_products)
    potential_revenue = avg_price * sum(products[pid]['quantity'] for pid in filtered_products)
    
    print(f"Result: {product_score}")
    return product_score

# Sample inventory data
inventory = {
    'P001': {'price': 25, 'quantity': 10, 'reviews': 15, 'quality': 4},
    'P002': {'price': 30, 'quantity': 8, 'reviews': 7, 'quality': 3},
    'P003': {'price': 15, 'quantity': 12, 'reviews': 20, 'quality': 5, 'alternative': 'P005'},
    'P004': {'price': 40, 'quantity': 4, 'reviews': 12, 'quality': 4},
    'P005': {'price': 20, 'quantity': 7, 'reviews': 9, 'quality': 2}
}

# Calculate and display the results
final_score = calculate_inventory_metrics(inventory)