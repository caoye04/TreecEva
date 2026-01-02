def calculate_performance(data):
    base_multiplier = 1.5
    penalty_factor = 0.9
    bonus_threshold = 85
    adjustment = 0.0

    # Irrelevant tracking variables (distractors)
    total_accesses = 0
    outlier_count = 0
    temp_result = 0

    score_summary = {}
    for entry in data:
        raw_value = entry['metric'] * base_multiplier
        if entry['anomaly']:
            raw_value *= penalty_factor
            outlier_count += 1  # Semi-relevant, not used in final calculation

        # Conditional expression usage (required feature)
        category = 'high' if raw_value >= bonus_threshold else 'standard'
        
        # Dictionary operations (required feature)
        if category not in score_summary:
            score_summary[category] = 0
        score_summary[category] += raw_value

        total_accesses += 1  # Distractor: tracked but unused

    # Simulated adjustment logic (only one branch affects result)
    if len(score_summary) > 1 and score_summary.get('high', 0) > 0:
        adjustment = 5.0
    else:
        adjustment = -2.0
        temp_result = sum(score_summary.values()) * 0.1  # Dead computation

    # Core logic buried among distractions
    base_score = sum(score_summary.values())
    final_score = base_score + adjustment

    # Extra red herring computations
    normalized_total = base_score / (total_accesses or 1)
    derived_metric = normalized_total * 1.2 if outlier_count == 0 else normalized_total * 0.8

    return final_score

# Input data
benchmark_data = [
    {'metric': 60, 'anomaly': False},
    {'metric': 70, 'anomaly': True},
    {'metric': 90, 'anomaly': False},
    {'metric': 88, 'anomaly': False}
]

# Execution point
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")