def calculate_final_score(data, weight_map):
    # Preprocess: extract and normalize ranks
    normalized = {}
    total_inv = sum(1.0 / rank for rank in data.values())
    
    for key, rank in data.items():
        normalized[key] = (1.0 / rank) / total_inv
    
    # Distractor: irrelevant transformation on keys
    shifted_keys = [k[-2:] + k[:-2] for k in data.keys()]
    dummy_sum = sum(len(k) for k in shifted_keys)

    # Weighted scoring
    weighted_values = []
    for category, norm_value in normalized.items():
        if category in weight_map:
            weighted_values.append(norm_value * weight_map[category])
    
    # Distractor: unused helper calculation
    peak_weight = max(weight_map.values())
    avg_weight = sum(weight_map.values()) / len(weight_map)
    penalty_factor = 1.0 if len(data) <= 5 else 0.95  # Not actually used

    # Real computation: aggregate score using list comprehension
    base_score = sum(weighted_values)
    adjustment = sum([0.1 * w for w in weighted_values if w > 0.2])
    final_score = base_score + adjustment
    
    return final_score

# Main execution context
rank_data = {
    'algorithm_a': 1,
    'algorithm_b': 3,
    'algorithm_c': 4,
    'algorithm_d': 2,
    'algorithm_e': 8
}

weights = {
    'algorithm_a': 0.9,
    'algorithm_b': 0.6,
    'algorithm_c': 0.5,
    'algorithm_d': 0.7,
    'algorithm_e': 0.3
}

# Irrelevant tracking state
processing_log = []
for algo in rank_data:
    processing_log.append(f"Processed {algo.upper()}")

# Key statement
final_score = calculate_final_score(rank_data, weights)

# Output result as required
print(f"Result: {final_score}")