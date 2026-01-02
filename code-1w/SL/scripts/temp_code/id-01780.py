def evaluate_performance(metrics, thresholds):
    # Core logic variables
    base_score = 0
    productivity_set = {x for x in metrics if x > 0}
    compliance_set = {x for x in thresholds if x % 2 == 0}
    
    # Distractor: Irrelevant metric transformation
    normalized_metrics = [round(x * 1.07 + 3, 2) for x in metrics]  # Not used later
    adjustment_factor = sum(normalized_metrics) / (len(normalized_metrics) + 1e-5)

    # Intermediate score computation
    if len(productivity_set) >= 3:
        base_score += 15
    
    # Set-based condition check
    overlap = productivity_set.intersection(compliance_set)
    if len(overlap) > 0:
        base_score += 10

    # Distractor: unused conditional path
    if adjustment_factor > 50:
        penalty = 5  # Dead code in practice due to input range
    else:
        bonus_flag = True  # Semi-relevant but not directly used

    # Multiple assignment distraction
    temp_a, temp_b, temp_c = 12, 24, 36
    auxiliary_sum = temp_a + temp_b  # Irrelevant sum

    # Conditional expression with side-effect-free logic
    multiplier = 2 if base_score >= 20 else 1
    
    # Final aggregation
    final_score = base_score * multiplier
    
    # Additional red herring: loop with no effect on result
    running_total = 0
    for i in range(3):
        for j in range(2):
            running_total += i * j * 0.1  # Trivial accumulation

    return final_score

# Input data
performance_data = [5, -3, 8, 12, 0, 7]
threshold_conditions = [4, 9, 10, 15, 20]

# Execution point of interest
final_score = evaluate_performance(performance_data, threshold_conditions)
print(f"Target result: {final_score}")