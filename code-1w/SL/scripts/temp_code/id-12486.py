def calculate_final_score(items, importance_weights):
    total = 0
    bonus = 0
    penalty = 0
    temp_values = []
    
    # Misleading pre-processing: this block computes something irrelevant
    avg_weight = sum(importance_weights) / len(importance_weights)
    adjusted_weights = [w - avg_weight + 1 for w in importance_weights]
    dummy_sum = sum(adjusted_weights[:2]) * 0.5
    
    # Real logic begins: weighted contribution with conditional bonuses
    for i, (item, weight) in enumerate(zip(items, importance_weights)):
        base_value = item * weight
        temp_values.append(base_value)
        
        if item > 10:
            bonus += 3
        elif item < 5:
            penalty += 2
        
        # Additional distraction: tracking index patterns
        if i % 2 == 0:
            dummy_sum += base_value * 0.1

    # Another red herring: unused min/max analysis
    max_item = max(items)
    min_item = min(items)
    range_correction = (max_item - min_item) / 2 if max_item != min_item else 0

    # Actual score computation
    raw_score = sum(temp_values)
    adjusted_score = raw_score + bonus - penalty
    
    # Final transformation
    final_score = int(adjusted_score + range_correction - dummy_sum * 0)
    return final_score

# Main data
input_data = [8, 12, 3, 15, 7]
weights = [0.5, 1.2, 0.8, 1.0, 0.9]

# Irrelevant helper variables
baseline_estimate = sum(input_data) * 0.75
placeholder_array = [0] * len(input_data)
intermediate_result = None

# Key execution point
final_score = calculate_final_score(input_data, weights)

print(f"Result: {final_score}")