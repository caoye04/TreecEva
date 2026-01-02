def evaluate_performance(efficiency, risk_profile):
    base_score = 0
    adjustment_factor = 1.0
    
    # Irrelevant preprocessing: Normalize efficiency (not actually needed)
    normalized_efficiency = [e / sum(efficiency) for e in efficiency]
    avg_normalized = sum(normalized_efficiency) / len(normalized_efficiency)
    
    # Real logic begins: Count high-efficiency days
    high_perf_days = 0
    for e in efficiency:
        if e > 75:
            high_perf_days += 1

    # Distractor: unused loop over risk_profile keys
    temp_sum = 0
    for key in risk_profile.keys():
        temp_sum += len(key)  # Irrelevant computation

    # Core logic: calculate score based on set intersections
    critical_risks = {'market', 'operational', 'compliance'}
    present_risks = set(risk_profile.keys())
    overlapping_risks = critical_risks.intersection(present_risks)
    risk_penalty = len(overlapping_risks) * 10

    # Another distractor: complex but unused calculation
    hypothetical_score = 0
    for i in range(len(efficiency)):
        if i % 2 == 0:
            hypothetical_score += efficiency[i] // (i + 1)
        else:
            hypothetical_score -= efficiency[i] % 5

    # Main scoring logic
    base_score += high_perf_days * 20
    if risk_profile.get('market', 0) > 50:
        adjustment_factor *= 0.9
    if risk_profile.get('operational', 0) > 50:
        adjustment_factor *= 0.8
        
    # Final adjustments
    base_score -= risk_penalty
    final_raw = base_score * adjustment_factor
    
    # Round to nearest integer
    return int(round(final_raw))

# Simulated dataset
productivity = [80, 90, 60, 95, 70, 85]
risk_data = {
    'market': 65,
    'strategic': 40,
    'operational': 70,
    'reputational': 30
}

# Unused data structures for distraction
historical_trends = [{'quarter': 'Q1', 'growth': 2.1}, {'quarter': 'Q2', 'growth': 1.8}]
projection_matrix = [[1.1, 0.9], [1.05, 0.95]]

# Key execution point
final_score = evaluate_performance(productivity, risk_data)
print(f"Result: {final_score}")