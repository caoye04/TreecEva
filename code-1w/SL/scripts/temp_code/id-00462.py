def calculate_performance(data):
    base_multiplier = 1.5
    penalty_factor = 0.9
    bonus_threshold = 85
    internal_offset = 3
    
    # Irrelevant tracking variables (distractors)
    outlier_count = 0
    normalized_values = []
    temp_aggregates = []
    
    for i, record in enumerate(data):
        raw_score = record['score']
        category_weight = record['weight']
        
        # Real computation path
        weighted_score = raw_score * category_weight * base_multiplier
        
        # Conditional adjustment (part of actual logic)
        if raw_score > bonus_threshold:
            weighted_score += 5 * category_weight
        else:
            weighted_score *= penalty_factor

        # Distractor: some unnecessary normalization
        adjusted = (weighted_score + internal_offset) / (category_weight + 0.1)
        normalized_values.append(adjusted)
        
        # Semi-relevant aggregation
        temp_aggregates.append(weighted_score)
        
        # Fake early termination check (never triggers due to data)
        if raw_score < 0:
            outlier_count += 1
            if outlier_count > 10:
                return -1
    
    # Real final computation
    total_base = sum(temp_aggregates)
    stability_variance = sum((x - sum(temp_aggregates)/len(temp_aggregates))**2 for x in temp_aggregates) / len(temp_aggregates)
    correction_shift = 2.5 if stability_variance > 100 else 1.2
    
    # Final score depends only on total_base and correction_shift
    final_score = int(total_base / correction_shift)
    
    # Use of set operations (required feature): irrelevant filtering
    unique_weights = set(record['weight'] for record in data)
    weight_pairs = list(zip(unique_weights, reversed(list(unique_weights))))
    pair_sum_product = sum(a * b for a, b in weight_pairs)  # unused
    
    # Use of enumerate (required feature): just iterating again, no effect
    for idx, w in enumerate(unique_weights):
        _ = w * idx  # dead computation
    
    return final_score

# Input data
benchmark_data = [
    {'score': 78, 'weight': 1.2},
    {'score': 92, 'weight': 2.0},
    {'score': 88, 'weight': 1.8},
    {'score': 76, 'weight': 1.5},
    {'score': 95, 'weight': 2.5}
]

# Execution point
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")