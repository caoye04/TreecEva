def compute_product_quality(product_dict):
    # Distractor variables and misleading computations
    temp_adjustment = 15
    base_factor = 7
    weight_factor = 3
    irrelevant_multiplier = 2
    
    # Misleading intermediate calculation (unused)
    misleading_total = sum(len(name) for name in product_dict.keys()) * base_factor
    
    # Dead code path that doesn't affect result
    if misleading_total > 100:
        dead_result = misleading_total // 2
    else:
        dead_result = misleading_total * 2
    
    # Main computation with list comprehension and set operations
    quality_scores = [
        (details['rating'] * weight_factor - temp_adjustment) 
        for details in product_dict.values() 
        if details.get('active', False)
    ]
    
    # More distractor operations
    distractor_set = set(range(len(quality_scores) * 2))
    filtered_scores = {score for score in quality_scores if score > 0}
    
    # Irrelevant string manipulation
    status_check = 'processed_' + str(len(product_dict))
    
    # Actual result computation
    if filtered_scores:
        final_score = sum(filtered_scores) * base_factor
    else:
        final_score = base_factor * weight_factor
    
    return final_score

# Main execution
products_data = {
    'widget_a': {'rating': 8, 'active': True},
    'widget_b': {'rating': 6, 'active': False},
    'widget_c': {'rating': 9, 'active': True},
    'widget_d': {'rating': 7, 'active': True}
}

# Distractor variable initialization
initial_rating_sum = sum(p['rating'] for p in products_data.values())
unused_calculation = initial_rating_sum * 3

# Key statement
final_quality_score = compute_product_quality(products_data)

print(f"Result: {final_quality_score}")