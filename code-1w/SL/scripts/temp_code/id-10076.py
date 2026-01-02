def evaluate_performance(metrics, flags):
    base = sum(metrics)
    penalty = 0
    
    # Analyze risk flags using set operations
    high_risk = {'critical', 'urgent', 'blocked'}
    active_risks = flags.intersection(high_risk)
    if len(active_risks) > 0:
        penalty += 15

    # Conditional adjustment based on metric patterns
    threshold_met = [m >= 75 for m in metrics]
    if all(threshold_met):
        penalty -= 5

    # Irrelevant distraction: tracking unused phases
    phase_log = []
    for i, val in enumerate(metrics):
        status = 'passed' if val > 50 else 'review'
        phase_log.append((i, status, val * 0.1))  # Not used later

    # Secondary distraction: redundant calculation
    temp_result = 0
    for a, b in zip(metrics, metrics[1:] + [metrics[0]]):
        temp_result += (a - b) ** 2  # Computed but not impacting final score

    # Main scoring logic
    adjustment = -penalty if base > 200 else +penalty
    return base + adjustment

# Simulated data input
productivity = [88, 92, 76, 81]
risk_indicators = {'pending', 'critical', 'resolved'}
overhead_cost = sum([x**2 for x in range(5)])  # Dead computation
reference_snapshot = {1, 2, 3}.union({4, 5})  # Unused set

# Key execution point
final_score = evaluate_performance(productivity, risk_indicators)
print(f"Result: {final_score}")