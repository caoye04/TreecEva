def calculate_final_score(raw_data, limits):
    # Initialize various tracking variables (some are red herrings)
    temp_sum = 0
    outlier_count = 0
    normalized_values = []
    cumulative_product = 1  # Used only in dead logic branch
    adjustment_factor = 1.5

    # Real processing begins
    valid_entries = [x for x in raw_data if isinstance(x, (int, float))]
    filtered_data = [x for x in valid_entries if limits['min'] <= x <= limits['max']]

    # Distractor: some irrelevant computations
    for val in valid_entries:
        if val > limits['max'] * 2:
            outlier_count += 1

    # Actual transformation chain
    adjusted_values = [v * adjustment_factor for v in filtered_data if v % 2 == 1]
    
    # More distractions: unused intermediate calculation
    squared_sum = sum([x**2 for x in filtered_data])
    mean_val = sum(filtered_data) / len(filtered_data) if filtered_data else 0

    # Core logic step 1: filter values above mean
    above_mean = [x for x in adjusted_values if x > mean_val]

    # Core logic step 2: map via conditional expression
    mapped_scores = [x if x < 50 else x * 0.9 for x in above_mean]

    # Core logic step 3: use set to deduplicate (some duplicates introduced by scaling)
    unique_scores = list(set(mapped_scores))

    # Core logic step 4: apply weighted sum using position
    weighted_sum = sum([score * (i + 1) for i, score in enumerate(unique_scores)])

    # Core logic step 5: combine with dictionary lookup modifier
    modifiers = {'A': 0.8, 'B': 1.1, 'C': 1.3}
    category = 'A' if weighted_sum < 100 else 'B' if weighted_sum < 200 else 'C'
    final_modifier = modifiers.get(category)

    result = weighted_sum * final_modifier

    # Dead code path - never executed but adds cognitive load
    if outlier_count == 0 and False:
        backup = sum(normalized_values)
        cumulative_product *= backup

    return int(result)

# Main execution
raw_dataset = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
detection_thresholds = {'min': 12, 'max': 52}

intermediate_total = sum(raw_dataset) // len(raw_dataset)  # distractor
scaling_constant = 2.718  # unused constant (red herring)

final_score = calculate_final_score(raw_dataset, detection_thresholds)
print(f"Result: {final_score}")