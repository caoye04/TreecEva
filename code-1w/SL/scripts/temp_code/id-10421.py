def evaluate_performance(efficiency, risk):
    base_score = efficiency * 10
    penalty = 0
    
    # Distractor: Irrelevant health metrics
    heart_rate = 72
    stress_level = heart_rate / 15
    recovery_time = stress_level * 2  # Unused

    if risk > 0.5:
        penalty += 15
    elif risk > 0.3:
        penalty += 8
    else:
        penalty += 5

    # Distractor: Unused productivity indicators
    focus_metric = efficiency ** 0.5
    fatigue_index = efficiency / 100  # Computed but not used

    return base_score - penalty

# Main computation chain
hours_worked = 37
optimal_hours = 40
productivity = hours_worked / optimal_hours

# Risk assessment using lambda and dictionary mapping (meaningful)
evaluate_risk = lambda x: {
    x < 30: 0.7,
    x < 35: 0.5,
    x < 38: 0.4,
    otherwise: 0.6
}.get(True, 0.6)
otherwise = False  # Trick to allow .get() with boolean key; sets risk_factor via logic

risk_factor = evaluate_risk(hours_worked)

# Additional distraction: unused data structure manipulation
task_log = [{'id': i, 'status': 'done'} for i in range(5)]
completion_rate = len(task_log) / 5
overhead_cost = sum([t['id'] for t in task_log]) * 0.1  # Calculated but irrelevant

# Key statement
final_score = evaluate_performance(productivity, risk_factor)

print(f"Result: {final_score}")