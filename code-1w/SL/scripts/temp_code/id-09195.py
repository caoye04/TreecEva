def calculate_final_score(results, weights):
    # Normalize results using min-max scaling (irrelevant for final logic but adds distraction)
    min_val = min(results.values())
    max_val = max(results.values())
    normalized = {k: (v - min_val) / (max_val - min_val) if max_val != min_val else 0 for k, v in results.items()}

    # Track cumulative weighted sum
    weighted_sum = 0.0
    total_weight = 0.0

    # Secondary tracking variables (some unused)
    count_processed = 0
    temp_offsets = []

    # Use of enumerate and zip to align results with weights by index
    method_names = list(results.keys())
    method_scores = list(results.values())
    
    for i, (name, score) in enumerate(zip(method_names, method_scores)):
        weight = weights[i] if i < len(weights) else 0.5  # default weight

        # Simulate adjustment based on position (distraction)
        position_factor = (i + 1) / len(method_names)
        adjusted_score = score * (1 + position_factor * 0.05)  # minor boost

        # Only the base weight and original score matter in final logic
        weighted_sum += score * weight
        total_weight += weight

        # Dead-end computation: stored but not used
        temp_offsets.append(abs(adjusted_score - score))

        count_processed += 1

    # Distractor: unused normalization based on offsets
    if temp_offsets:
        avg_offset = sum(temp_offsets) / len(temp_offsets)
        offset_penalty = avg_offset * 0.1  # computed but irrelevant

    # Final aggregation: only weighted average matters
    final_score = weighted_sum / total_weight if total_weight != 0 else 0
    
    return final_score

# Main execution
results = {
    'accuracy': 88.5,
    'precision': 92.3,
    'recall': 85.7,
    'f1': 89.1
}

weights = [0.4, 0.3, 0.2, 0.1]  # decreasing importance

# Irrelevant pre-processing step
processed_results = {k.upper(): v * 1.01 for k, v in results.items()}
del processed_results  # dead code

final_score = calculate_final_score(results, weights)
print(f"Result: {final_score}")