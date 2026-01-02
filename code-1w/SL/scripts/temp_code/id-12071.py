def calculate_final_score(records, importance):
    # Initialize tracking variables
    totals = {}
    counts = {}
    temp_debug_log = []

    # Irrelevant pre-processing: log transformation (not used in final result)
    fake_normalized = {k: v ** 0.5 for k, v in records.items() if v > 0}
    unused_aggregate = sum(fake_normalized.values()) * 0.1

    # Core logic with distractions
    for key, value in records.items():
        if key not in importance:
            continue
        weight = importance[key]
        weighted_val = value * weight

        # Track totals and counts (only 'A', 'B', 'C' matter)
        if key in ['A', 'B', 'C']:
            totals[key] = totals.get(key, 0) + weighted_val
            counts[key] = counts.get(key, 0) + 1

        # Dead code path - never executed due to data keys
        if key == 'Z99':
            temp_debug_log.append(weighted_val)

    # Semi-relevant aggregation
    base_total = sum(totals.values())
    entry_count = len(counts)
    average_per_category = base_total / entry_count if entry_count else 0

    # Distracting statistical computation (not directly used)
    squared_deviation = sum((v - average_per_category) ** 2 for v in totals.values())
    fake_variance_proxy = squared_deviation / entry_count if entry_count else 0

    # Lambda-based adjustment (actually used)
    adjuster = lambda x, w: x * (1.1 if w > 0.5 else 0.9)
    adjusted_total = sum(adjuster(totals[k], importance[k]) for k in totals)

    # Final score calculation
    stability_factor = 0.85
    final_score = adjusted_total * stability_factor

    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Input data
raw_data = {
    'A': 45,
    'B': 60,
    'C': 30,
    'D': 80,  # Will be skipped
    'E': 25   # Will be skipped
}

weights_config = {
    'A': 0.6,
    'B': 0.8,
    'C': 0.4,
    'X': 0.1,  # Not in data
    'Y': 0.2   # Not in data
}

# Key execution point
final_score = calculate_final_score(raw_data, weights_config)