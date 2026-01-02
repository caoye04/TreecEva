def analyze_workflow_efficiency(task_load, overhead_penalty=0.15):
    base_efficiency = sum(task_load) / len(task_load) if task_load else 0
    penalty_adjustment = base_efficiency * overhead_penalty
    adjusted_efficiency = base_efficiency - penalty_adjustment
    
    # Distractor: historical average not used in final logic
    historical_avg = (adjusted_efficiency * 0.7) + (base_efficiency * 0.3)
    fluctuation_index = max(task_load) - min(task_load)
    stability_bonus = 0.0 if fluctuation_index > 20 else 2.5

    return adjusted_efficiency, stability_bonus, fluctuation_index


def evaluate_performance(metrics, threshold):
    efficiency, bonus, _ = metrics
    performance_level = 'standard'
    
    if efficiency >= threshold:
        performance_level = 'high'
    elif efficiency >= threshold * 0.85:
        performance_level = 'moderate'
    else:
        performance_level = 'low'
    
    # Key logic: only high and moderate get bonus
    incentive_score = 10 if performance_level == 'high' else (5 if performance_level == 'moderate' else 0)
    base_score = int(efficiency * 2) + incentive_score
    
    # Unrelated debug computation (distractor)
    debug_weight = base_score * 0.01 + incentive_score % 3
    temp_offset = debug_weight - 0.5

    final_evaluation = base_score + bonus  # Bonus only applies here
    return int(final_evaluation)

# Main execution block
workload_data = [12, 15, 18, 22, 14, 20, 16]
threshold = 16.0

# Simulate multiple team evaluations (only last one matters)
for team_id in range(3):
    raw_metrics = analyze_workflow_efficiency(workload_data, overhead_penalty=0.1 + team_id * 0.05)
    productivity_set = raw_metrics  # tuple of (efficiency, bonus, index)

    # Irrelevant intermediate logging
    log_entry = f"Team {team_id}: Efficiency={raw_metrics[0]:.2f}, Index={raw_metrics[2]}"
    dummy_filter = {x for x in workload_data if x > 15}  # set comprehension distractor
    filtered_count = len(dummy_filter)

# Critical statement
final_score = evaluate_performance(productivity_set, threshold)
print(f"Result: {final_score}")