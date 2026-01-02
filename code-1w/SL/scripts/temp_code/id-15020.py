def evaluate_performance(metrics, flags):
    base = sum(metrics)
    adjustment = len(flags) * 2
    penalty = 0
    
    # Irrelevant intermediate computation (distractor)
    temp_analysis = [x ** 0.5 for x in metrics if x > 10]
    avg_temp = sum(temp_analysis) / len(temp_analysis) if temp_analysis else 0
    
    # Real logic starts here
    if len(metrics) > 3:
        penalty += 5
    if adjustment > 10:
        penalty += 3
    
    # Simulated risk mitigation via set operations
    critical_risks = {1, 3, 5, 7}
    active_risks = flags.intersection(critical_risks)
    risk_penalty = len(active_risks) * 4
    
    # More distraction: unused data transformation
    shadow_metrics = [x * 1.5 for x in metrics]
    shadow_metrics = [x for x in shadow_metrics if x < 50]  # dead filtering
    
    final = base - adjustment - penalty - risk_penalty
    return int(final)

# Main execution flow
productivity = [8, 12, 15, 22, 9]
baseline_avg = sum(productivity) / len(productivity)  # distractor
fluctuation = max(productivity) - min(productivity)  # irrelevant stat

# Simulate historical anomalies (not used)
historical_anomalies = set()
for i in range(len(productivity)):
    if productivity[i] % 3 == 0:
        historical_anomalies.add(i)

# Key risk flag set (only this matters)
risk_flags = {2, 3, 5, 8}

# Dummy loop with side-effect-free operations
expanded_data = []
for val in productivity:
    expanded_data.append(val + 1)
    expanded_data.append(val - 1)
expanded_data = [x for x in expanded_data if x != 0]  # unused

# Core evaluation point
final_score = evaluate_performance(productivity, risk_flags)
print(f"Result: {final_score}")