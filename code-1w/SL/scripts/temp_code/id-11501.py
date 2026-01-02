def calculate_final_score(records, importance):
    base_scores = {}
    temp_offsets = {}
    for idx, (key, value) in enumerate(records.items()):
        if key.startswith('metric_'):
            clean_key = key.replace('metric_', '')
            raw_score = value * importance.get(key, 1.0)
            adjustment = 0
            
            # Distractor block: complex but unused computation
            cumulative_shift = sum([i * 2 for i in range(idx + 1)])
            temp_offsets[clean_key] = cumulative_shift * 0.1
            
            if raw_score > 50:
                adjustment = 10
            elif raw_score < 30:
                adjustment = -5
            else:
                adjustment = 0
            
            # Real scoring logic
            base_scores[clean_key] = raw_score + adjustment
    
    # Another distractor: set operation with no impact
    used_keys = set(base_scores.keys())
    expected_keys = {'a', 'b', 'c', 'd'}
    missing_keys = expected_keys - used_keys
    
    # Unused dictionary transformation
    inverted_map = {v: k for k, v in enumerate(base_scores)}

    # Actual aggregation using zip and conditional logic
    ordered_weights = [importance[f'metric_{k}'] for k in sorted(base_scores)]
    ordered_values = [base_scores[k] for k in sorted(base_scores)]
    weighted_sum = sum(val * w for val, w in zip(ordered_values, ordered_weights))
    weight_total = sum(ordered_weights)
    
    # Final score calculation
    final_score = weighted_sum / weight_total if weight_total != 0 else 0
    
    # Irrelevant list mutation
    dummy_list = [1, 2, 3]
    for _ in range(3):
        dummy_list.append(dummy_list.pop(0))
    
    return final_score

# Input data
input_data = {
    'metric_a': 45,
    'metric_b': 70,
    'metric_c': 25,
    'metric_d': 60
}

weights = {
    'metric_a': 2.0,
    'metric_b': 3.0,
    'metric_c': 1.5,
    'metric_d': 2.5
}

# Execute
final_score = calculate_final_score(input_data, weights)
print(f"Target result: {final_score}")