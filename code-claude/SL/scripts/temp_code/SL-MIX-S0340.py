def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

def calculate_product_score(products, weight):
    base_score = 0
    quality_factor = 3
    market_multiplier = 2.5
    
    # Calculate potential market reach (not used directly)
    potential_reach = sum(p['rating'] * market_multiplier for p in products)
    
    # Process each product with its index
    for idx, product in enumerate(products):
        # Apply quality factor to rating (relevant)
        adjusted_rating = product['rating'] * quality_factor
        
        # Calculate position bonus (distraction)
        position_bonus = idx % 3
        
        # Apply modular arithmetic to price (relevant)
        price_factor = product['price'] % 10
        
        # Add weighted contribution to base score (relevant)
        base_score += (adjusted_rating + price_factor) * weight
    
    # Calculate inventory impact (distraction)
    inventory_levels = [p.get('stock', 50) for p in products]
    avg_inventory = sum(inventory_levels) / max(1, len(inventory_levels))
    
    # Generate report statistics (distraction)
    report_data = list(zip([p['name'] for p in products], inventory_levels))
    
    return int(base_score)

# Sample product data
products = [
    {'name': 'Gadget A', 'rating': 4.2, 'price': 37, 'stock': 120},
    {'name': 'Gadget B', 'rating': 3.8, 'price': 25, 'stock': 85},
    {'name': 'Gadget C', 'rating': 4.7, 'price': 42, 'stock': 30},
    {'name': 'Gadget D', 'rating': 3.5, 'price': 18, 'stock': 200}
]

# Filter valid products (those with rating > 3.5)
valid_products = [p for p in products if p['rating'] > 3.5]

# Calculate weight factor using modular arithmetic
base_weight = factorial(3) % 5
weight_modifier = sum(1 for p in valid_products if p['price'] > 30)
weight_factor = base_weight + weight_modifier

# Calculate the final product score
product_score = calculate_product_score(valid_products, weight_factor)

print(f"Result: {product_score}")