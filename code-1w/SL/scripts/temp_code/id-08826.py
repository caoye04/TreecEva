def evaluate_performance(output, faults):
    base_score = 100
    if output > 80:
        base_score += 20
    elif output > 60:
        base_score += 10

    fault_penalty = len(faults) * 5
    base_score -= fault_penalty

    # Additional adjustment based on pattern in fault types
    critical_errors = [f for f in faults if 'critical' in f]
    if len(critical_errors) > 0:
        base_score -= 15

    return base_score

# Simulated productivity and error log
team_data = {
    'productivity': 75,
    'error_log': ['typo', 'critical_failure', 'format_issue']
}

productivity = team_data['productivity']
errors = team_data['error_log']

# Extract subsystem codes (irrelevant but adds minor interference)
subsystems = ['auth', 'payment', 'logging']
codes = [s[:3].upper() for s in subsystems]  # unused distraction

final_score = evaluate_performance(productivity, errors)
print(f"Result: {final_score}")