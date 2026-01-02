def calculate_performance(data):
    base_multiplier = 1.5
    threshold = 75
    adjustment_factor = 0.8
    temp_result = 0
    cumulative_weight = 0

    # Irrelevant tracking variables (distractors)
    outlier_count = 0
    normalized_values = []
    processed_indices = []

    for i, entry in enumerate(data):
        raw_value = entry['metric']
        weight = entry['weight']
        
        # Real computation path
        if raw_value >= threshold:
            scaled = raw_value * base_multiplier
        else:
            scaled = raw_value * adjustment_factor

        # Semi-relevant transformation (only cumulative_weight matters)
        weighted_contribution = scaled * weight
        temp_result += weighted_contribution
        cumulative_weight += weight

        # Dead code path with misleading logic
        if raw_value < 50:
            outlier_count += 1
            z_score = (raw_value - 60) / 10
            normalized_values.append(z_score)
        else:
            processed_indices.append(i)  # Not used later

    # Another irrelevant list comprehension
    final_normalization = [x * 0.95 for x in normalized_values if x > 0]

    # Actual answer depends only on this
    average_contribution = temp_result / cumulative_weight if cumulative_weight != 0 else 0

    # Real key operation
    penalty_rate = 0.1 if outlier_count > 2 else 0
    adjusted_total = average_contribution * (1 - penalty_rate)

    # Final transformation
    final_score = int(adjusted_total + 0.5)  # Round to nearest integer

    return final_score

# Main data input
benchmark_data = [
    {'metric': 80, 'weight': 3},
    {'metric': 90, 'weight': 5},
    {'metric': 45, 'weight': 2},
    {'metric': 70, 'weight': 4},
    {'metric': 85, 'weight': 6}
]

result_tracker = {}
interim_results = []

for idx, item in enumerate(benchmark_data):
    interim_results.append({
        'index': idx,
        'processed': item['metric'] * 1.1
    })

# Key execution point
final_score = calculate_performance(benchmark_data)

print(f"Result: {final_score}")