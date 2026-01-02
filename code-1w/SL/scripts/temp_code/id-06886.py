def evaluate_performance(output, risk_profile):
    base_efficiency = 85
    overhead = 12
    penalty_rate = 0.15
    bonus_rate = 0.25

    # Irrelevant metrics for distraction
    idle_cycles = 45
    calibration_factor = 3.14
    temp_buffer = [x * 2 for x in range(5)]  # Unused list comprehension

    efficiency = base_efficiency + output - overhead

    if efficiency > 90:
        efficiency += 5  # Bonus for high performance

    # Risk adjustment using set operations
    high_risk_tasks = {1, 3, 4, 7, 9}
    critical_risks = high_risk_tasks.intersection(risk_profile)
    risk_penalty = len(critical_risks) * 3

    adjusted_efficiency = efficiency - risk_penalty

    # Logical evaluation with short-circuiting
    is_optimal = adjusted_efficiency >= 88 and len(risk_profile) < 6

    # Dummy logic that doesn't affect final outcome
    if is_optimal or adjusted_efficiency > 100:
        dummy_flag = True
        shadow_efficiency = adjusted_efficiency * 1.1

    # Final scoring with conditional bonus
    if is_optimal:
        final_score = int(adjusted_efficiency * (1 + bonus_rate))
    else:
        final_score = int(adjusted_efficiency * (1 - penalty_rate))

    return final_score

# Main execution
productivity = 20
risk_set = {1, 2, 4, 6}

# Key assignment point
final_score = evaluate_performance(productivity, risk_set)
print(f"Result: {final_score}")