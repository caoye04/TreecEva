def calculate_product_quality(products, threshold):
    base_score = 100
    irrelevant_metric = 42
    temp_buffer = [0] * 10
    
    # Distractor calculations
    weight_adjustment = 3.5 if len(products) > 5 else 2.0
    decoy_score = base_score * 0.75
    
    quality_scores = {}
    for product_id, specs in products.items():
        durability = specs.get('durability_rating', 0)
        reliability = specs.get('reliability_index', 0)
        efficiency = specs.get('efficiency_factor', 0)
        
        # Misleading intermediate calculation
        raw_score = (durability * 1.2 + reliability * 0.8) * efficiency
        misleading_adjustment = raw_score * 0.15 if durability > 70 else 0
        
        # Actual quality calculation
        if durability >= threshold and reliability >= threshold:
            quality_score = (durability * 0.6 + reliability * 0.4) * efficiency
            quality_scores[product_id] = quality_score
            
            # Dead code path
            if durability > 95:
                bonus_points = 5
                # This never executes due to threshold condition
        
        # Irrelevant operation
        temp_buffer[product_id % len(temp_buffer)] += 1
    
    # Key calculation with conditional expression
    valid_scores = [score for score in quality_scores.values() if score > 0]
    final_quality_score = sum(valid_scores) // len(valid_scores) if valid_scores else 0
    
    # More distractions
    unused_metric = final_quality_score * weight_adjustment
    buffer_sum = sum(temp_buffer)
    
    return final_quality_score

# Main execution
products_data = {
    1: {'durability_rating': 85, 'reliability_index': 92, 'efficiency_factor': 1.1},
    2: {'durability_rating': 78, 'reliability_index': 65, 'efficiency_factor': 0.9},
    3: {'durability_rating': 92, 'reliability_index': 88, 'efficiency_factor': 1.2},
    4: {'durability_rating': 45, 'reliability_index': 90, 'efficiency_factor': 1.0},
    5: {'durability_rating': 88, 'reliability_index': 84, 'efficiency_factor': 1.15}
}

quality_threshold = 70
quality_calculation = calculate_product_quality(products_data, quality_threshold)
final_quality_score = quality_calculation

print(f"Result: {final_quality_score}")