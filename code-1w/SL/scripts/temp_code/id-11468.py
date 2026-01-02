def calculate_performance(data):
    base_multiplier = 1.5
    penalty_factor = 0.9
    bonus_threshold = 85
    temp_offset = 0.0  # unused distractor
    scaling_constant = 10  # misleading, not used in core logic

    raw_scores = [entry['score'] for entry in data]
    performance_flags = [entry['active'] for entry in data]

    avg_score = sum(raw_scores) / len(raw_scores)
    above_threshold = sum(1 for s in raw_scores if s >= bonus_threshold)

    # Conditional expression with string method distraction
    adjustment = 5 if any(flag for flag in performance_flags) else 0
    status_label = 'optimal' if avg_score > 70 else 'suboptimal'
    normalized_label = status_label.upper().strip()  # string method - no impact

    # Simulated noise variables
    calibration_data = {'offset': 0.12, 'gain': 1.0}  # dead code path material
    if len(raw_scores) > 10:
        smoothing_factor = 0.05
    else:
        smoothing_factor = 0.1

    # Core accumulation logic
    weighted_sum = 0
    for i, score in enumerate(raw_scores):
        if i % 2 == 0:
            weighted_sum += score * base_multiplier
        else:
            weighted_sum += score * penalty_factor

    # Final computation chain
    adjusted_sum = weighted_sum + (adjustment * scaling_constant)  # uses adjustment, ignores scaling_constant meaningfully
    stability_penalty = len(raw_scores) * 0.01  # minor decimal correction
    final_score = (adjusted_sum / len(raw_scores)) - stability_penalty

    return final_score

# Input construction
benchmark_data = [
    {'score': 78, 'active': True},
    {'score': 88, 'active': False},
    {'score': 92, 'active': True},
    {'score': 67, 'active': True},
    {'score': 81, 'active': False},
    {'score': 95, 'active': True},
    {'score': 73, 'active': False},
    {'score': 89, 'active': True}
]

# Execution point
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")