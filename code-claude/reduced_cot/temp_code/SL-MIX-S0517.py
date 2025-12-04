def analyze_inventory(products):
    # Calculate some inventory metrics
    total_items = sum(products.values())
    average_items = total_items / len(products) if products else 0
    
    # Track most common product category
    categories = {'electronics': 0, 'clothing': 0, 'food': 0, 'other': 0}
    for product, count in products.items():
        if 'phone' in product or 'laptop' in product:
            categories['electronics'] += count
        elif 'shirt' in product or 'pants' in product:
            categories['clothing'] += count
        elif 'apple' in product or 'banana' in product:
            categories['food'] += count
        else:
            categories['other'] += count
    
    # Calculate priority score for each product
    priority_scores = {}
    for product, count in products.items():
        # Priority based on stock level and product type
        base_score = 10 if count < 5 else (5 if count < 20 else 2)
        multiplier = 2 if 'premium' in product else 1
        priority_scores[product] = base_score * multiplier
    
    # Apply weighting factors to inventory items
    weight_factors = {'laptop': 3, 'phone': 2, 'shirt': 1.5, 'pants': 1.5, 'apple': 1, 'banana': 1, 'premium': 2}
    weighted_values = {}
    
    # Calculate weighted values
    for product, count in products.items():
        # Find applicable weight factor
        factor = 1  # Default factor
        for key, value in weight_factors.items():
            if key in product:
                factor = value
                break
        
        weighted_values[product] = count * factor
    
    # Calculate total weighted inventory
    total_weight = sum(weighted_values.values())
    
    # Some additional metrics that aren't used in final result
    distinct_items = len(products)
    max_stock = max(products.values()) if products else 0
    min_stock = min(products.values()) if products else 0
    stock_range = max_stock - min_stock
    
    print(f"Result: {total_weight}")
    return total_weight

# Inventory data
inventory = {
    'laptop': 12,
    'premium laptop': 5,
    'phone': 25,
    'premium phone': 8,
    'shirt': 30,
    'pants': 15,
    'apple': 45,
    'banana': 50
}

# Run analysis
result = analyze_inventory(inventory)