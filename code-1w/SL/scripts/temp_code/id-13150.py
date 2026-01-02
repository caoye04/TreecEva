def calculate_final_score(data, weights):
    # Initialize tracking variables
    base_total = 0
    adjustment_factor = 1.0
    temp_result = {}
    outlier_count = 0

    # Process each entry in data
    for key in data:
        value = data[key]
        weight = weights.get(key, 0.5)

        # Compute weighted contribution
        contribution = value * weight
        base_total += contribution

        # Track high-value outliers (distraction)
        if value > 100:
            outlier_count += 1

        # Store intermediate (unused) results
        temp_result[key] = contribution * 0.9

    # Apply adjustment based on average magnitude (semi-relevant)
    avg_value = sum(data.values()) / len(data)
    if avg_value > 50:
        adjustment_factor = 0.95

    # Secondary loop to compute redundancy check (distractor)
    checksum = 0
    for v in temp_result.values():
        checksum += int(v) % 7

    # Actual score calculation
    raw_score = base_total * adjustment_factor
    penalty = 0
    
    # Additional penalty logic using dictionary operations
    status_map = {True: 10, False: 0}
    has_high_weight = any(w > 0.8 for w in weights.values())
    penalty += status_map[has_high_weight]

    # Conditional expression used for final adjustment
    final_score = raw_score - penalty if raw_score > 200 else raw_score + penalty

    # Irrelevant debugging print
    debug_info = {'checksum': checksum, 'outliers': outlier_count}
    return final_score

# Main execution
if __name__ == "__main__":
    data = {'metric_a': 85, 'metric_b': 92, 'metric_c': 78, 'metric_d': 105}
    weights = {'metric_a': 0.7, 'metric_b': 0.9, 'metric_c': 0.6, 'metric_d': 0.4}

    # Extraneous pre-processing
    normalized_data = {k: v / max(data.values()) for k, v in data.items()}
    scaling_factor = sum(normalized_data.values())

    # Key statement
    final_score = calculate_final_score(data, weights)
    
    # Unused variable assignments
    summary_stats = {
        'min': min(data.values()),
        'max': max(data.values()),
        'range': max(data.values()) - min(data.values())
    }
    
    print(f"Result: {final_score}")