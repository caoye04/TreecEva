def evaluate_performance(output, risk_profile):
    base_efficiency = 85
    overhead = 12
    penalty_factor = 0.0

    # Simulate workload calibration (distractor)
    calibration_sequence = [base_efficiency // (i + 1) for i in range(1, 5)]
    temp_adjustment = sum(calibration_sequence) / len(calibration_sequence)

    if len(risk_profile) > 3:
        penalty_factor += 0.15
    else:
        penalty_factor += 0.05

    # Evaluate output quartiles (semi-relevant)
    quartile_threshold = base_efficiency * 0.75
    if output > quartile_threshold:
        performance_bonus = 10
    elif output > quartile_threshold * 0.8:
        performance_bonus = 5
    else:
        performance_bonus = 0

    # Simulated environmental interference (dead computation)
    environmental_load = 0
    for hour in range(8, 18):
        if hour == 12:
            environmental_load += 5
        elif hour % 3 == 0:
            environmental_load -= 2

    # Core evaluation logic
    base_score = output * (1 - penalty_factor)
    adjusted_score = base_score + performance_bonus

    # Set operations to filter risk categories (key python feature)
    critical_risks = {1, 3, 5, 7, 9}
    mitigated_risks = {2, 4, 6, 8}
    active_risks = risk_profile & critical_risks  # Only critical risks matter

    risk_penalty = len(active_risks) * 2.5
    final_rating = adjusted_score - risk_penalty

    return int(final_rating)

# Initialize variables
productivity = 78
risk_set = {1, 2, 4, 7, 9}
deprecated_flags = [0] * 5  # Unused array (irrelevant)

# Additional distraction: historical benchmarking (not used)
historical_data = [
    {'period': 'Q1', 'yield': 72},
    {'period': 'Q2', 'yield': 76},
    {'period': 'Q3', 'yield': 74}
]

# Key execution point
final_score = evaluate_performance(productivity, risk_set)

# Output result
print(f"Result: {final_score}")