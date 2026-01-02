def evaluate_performance(output, risk_profile):
    base_efficiency = 85
    overhead = 12
    penalty_factor = 0.0

    # Assess productivity bands
    if output > 90:
        performance_band = 'excellent'
        bonus = 15
    elif output > 75:
        performance_band = 'good'
        bonus = 8
    elif output > 60:
        performance_band = 'adequate'
        bonus = 3
    else:
        performance_band = 'poor'
        bonus = 0
        penalty_factor = 0.15

    # Simulate resource allocation (distractor block)
    allocated_budget = 50000
    team_size = 7
    avg_salary = 7500
    projected_roi = allocated_budget * 0.23  # Not used later

    # Risk adjustment using set operations
    high_risk_factors = {1, 3, 4, 7, 9, 11}
    medium_risk_factors = {2, 5, 6, 8}
    critical_failures = high_risk_factors & risk_profile  # intersection
    system_warnings = medium_risk_factors & risk_profile

    risk_penalty = len(critical_failures) * 5 + len(system_warnings) * 2

    # Secondary distraction: simulate compliance checks
    compliance_log = []
    for factor in sorted(risk_profile):
        if factor % 2 == 0:
            compliance_log.append(f"Audit {factor}: Passed")
        else:
            compliance_log.append(f"Audit {factor}: Flagged")
    # compliance_log is never used again

    # Final efficiency calculation
    raw_score = base_efficiency + bonus - risk_penalty
    adjusted_score = raw_score * (1 - penalty_factor)

    # Additional irrelevant transformation
    normalized = round(adjusted_score / 100, 3)
    scaled_output = int(normalized * 200)  # unused

    # Key result computation
    final_score = int(round(adjusted_score))

    return final_score

# Main execution context
productivity = 82
risk_indicators = {1, 2, 5, 9}
current_load = 4.6  # dead variable
threshold_limit = 95.0  # unused constant
temp_result = productivity * 1.08  # misleading intermediate

final_score = evaluate_performance(productivity, risk_indicators)
print(f"Result: {final_score}")