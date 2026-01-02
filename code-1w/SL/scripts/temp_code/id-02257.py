def process_metrics(entries, importance):
    # Initialize tracking variables
    totals = [e['value'] * importance[i] for i, e in enumerate(entries)]
    offset = sum([t for t in totals if t > 10]) // 3 if len(totals) > 2 else 0

    # Irrelevant intermediate computations (distractors)
    temp_stats = {"max_val": max(totals), "min_val": min(totals), "range": 0}
    temp_stats["range"] = temp_stats["max_val"] - temp_stats["min_val"]
    adjustment_factor = lambda x: x * 0.95 if x > 15 else x * 1.05
    adjusted_totals = [adjustment_factor(t) for t in totals]

    # Core logic hidden among distractions
    valid_count = sum(1 for t in adjusted_totals if t >= 8)
    base_score = sum(adjusted_totals) / len(adjusted_totals)

    # Conditional expression affecting final result
    bonus = 7 if valid_count >= 3 else 0

    # Dead code path (never executed due to fixed condition)
    emergency_override = False
    override_value = 0
    if emergency_override and base_score < 5:
        override_value = 50  # This is never reached

    # Final computation with relevant logic
    final_score = base_score + bonus + (offset * 0.5)

    # Print result as required
    return final_score

# Input data
entry_data = [
    {'value': 4, 'meta': 'A'},
    {'value': 7, 'meta': 'B'},
    {'value': 12, 'meta': 'C'},
    {'value': 5, 'meta': 'D'}
]
weights = [1.0, 1.5, 2.0, 0.8]

# Execute and print result
result_var = process_metrics(entry_data, weights)
print(f"Result: {result_var}")