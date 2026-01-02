def evaluate_performance(metrics, baseline):
    # Irrelevant transformation (distractor)
    adjusted_metrics = [x * 1.05 for x in metrics]
    temp_sum = sum(adjusted_metrics[:3])

    # Real computation begins: normalize metrics relative to baseline
    normalized = [(val - baseline) ** 2 for val in metrics]
    
    # Misleading conditional branch (dead path due to data)
    if len(metrics) < 5:
        return -1  # never executed
    else:
        filtered = normalized[1:4]  # slicing central elements

    # Secondary distractor: character counting in debug mode (unused)
    debug_info = "Metrics processed: {}".format(len(metrics))
    char_count = len(debug_info)
    case_transformed = debug_info.upper()

    # Core logic: weighted combination of squared deviations
    weight_vector = [0.2, 0.3, 0.5]
    weighted_deviation = sum(filtered[i] * weight_vector[i] for i in range(len(filtered)))

    # Apply correction factor based on symmetry check (tuple unpacking)
    mid_index = len(normalized) // 2
    left_half = normalized[:mid_index]
    right_half = normalized[mid_index+1:]
    is_symmetric = tuple(left_half) == tuple(right_half[::-1])

    symmetry_bonus = 10.0 if is_symmetric else 3.5

    # Final aggregation with misleading offset
    magic_offset = sum([i*i for i in range(3)])  # always 5, but looks dynamic
    raw_score = weighted_deviation + symmetry_bonus - magic_offset

    # Final scaling (this assignment is the key point)
    final_score = int(raw_score * 2)  # convert to integer score

    return final_score

# Main execution context
baseline = 10
metrics = [8, 12, 10, 11, 9, 13]
data_log = [metrics[i] for i in range(0, len(metrics), 2)]  # unused logging array

# Key statement
final_score = evaluate_performance(metrics, baseline)
print(f"Result: {final_score}")