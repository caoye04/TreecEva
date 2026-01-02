def calculate_performance(data):
    total_weight = 0.0
    raw_sum = 0.0
    adjustment_factor = 1.2
    penalty_offset = 0.85
    temp_result = []
    
    for i, (value, weight) in enumerate(zip(data['values'], data['weights'])):
        if weight <= 0:
            continue
            redundant_flag = True  # Dead code path

        weighted_val = value * weight * adjustment_factor
        
        # Irrelevant transformation
        transformed = abs(weighted_val) ** 0.5
        temp_result.append(transformed)
        
        raw_sum += weighted_val
        total_weight += weight

    if total_weight == 0:
        return 0.0
    
    mean_weighted = raw_sum / total_weight
    
    # Secondary loop with enumerate - semi-relevant but only used for validation
    outlier_count = 0
    for idx, val in enumerate(data['values']):
        if abs(val - mean_weighted) > 2 * penalty_offset:  # Arbitrary threshold
            outlier_count += 1

    # Final computation chain
    stability_score = len(data['values']) - outlier_count
    normalized_stability = stability_score / len(data['values'])
    
    # Core logic: performance score combines mean and stability
    preliminary_score = mean_weighted * normalized_stability
    
    # Additional red herring: unused intermediate calculation
    theoretical_max = max(data['values']) * adjustment_factor
    efficiency_ratio = preliminary_score / theoretical_max if theoretical_max != 0 else 0
    
    # Final score adjusted by fixed rule
    final_score = preliminary_score - (outlier_count * penalty_offset * 0.5)
    
    return final_score

# Simulated benchmark dataset
dataset = {
    'values': [85, 90, 78, 92, 88, 76, 95],
    'weights': [0.5, 1.0, 0.8, 1.2, 0.9, 0.7, 1.1]
}

result = calculate_performance(dataset)
final_score = result
print(f"Result: {final_score}")