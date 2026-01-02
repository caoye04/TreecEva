def calculate_final_score(data, thresholds):
    # Irrelevant pre-processing: normalize unrelated metrics
    normalized_peaks = [max(0, min(x, 100)) for x in data['readings']]
    peak_count = sum(1 for x in normalized_peaks if x > 90)

    # Semi-relevant transformation
    adjusted_values = [x * 1.05 for x in data['values'] if x > 0]
    growth_factor = len(adjusted_values) / len(data['values']) if data['values'] else 0

    # Core logic: count how many exceed dynamic threshold
    dynamic_limit = thresholds['base'] + (thresholds['multiplier'] * len(data['tags']))
    valid_entries = [v for v in data['values'] if v > dynamic_limit]

    # Distractor: unused statistical calculation
    avg_magnitude = sum(abs(v) for v in data['values']) / len(data['values']) if data['values'] else 0
    variance_proxy = sum((v - avg_magnitude) ** 2 for v in data['values']) / len(data['values']) if data['values'] else 0

    # Conditional adjustment based on tag pattern
    has_priority_tag = any('urgent' in tag.lower() for tag in data['tags'])
    bonus_weight = 2 if has_priority_tag else 1

    # Secondary filter: only values with even indices considered
    filtered_by_index = [valid_entries[i] for i in range(len(valid_entries)) if i % 2 == 0]

    # Final score computation
    base_score = sum(filtered_by_index)
    penalty = -5 * len([x for x in data['logs'] if 'error' in x])  # error logs reduce score
    final_score = (base_score * bonus_weight) + penalty

    # Dead code path - never executed under current logic
    if False:
        fallback = sum(data['values']) // 10
        final_score = max(final_score, fallback)

    return final_score

# Input construction
input_data = {
    'values': [12, 45, 67, 89, 34, 92, 77],
    'readings': [88, 95, 76, 105, 43],
    'tags': ['normal', 'Urgent-review', 'low-priority'],
    'logs': ['initiated', 'checkpoint_passed', 'error_critical', 'retry_failed', 'complete']
}
thresholds_config = {
    'base': 40,
    'multiplier': 5
}

# Execution point
final_score = calculate_final_score(input_data, thresholds_config)
print(f"Result: {final_score}")