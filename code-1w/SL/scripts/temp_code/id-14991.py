def evaluate_performance(metrics, data_map):
    base_weights = {'latency': 0.4, 'throughput': 0.35, 'error_rate': 0.25}
    scaling_factor = 1.5
    
    # Irrelevant transformation (distractor)
    temp_adjustment = sum([data_map[k] * 0.1 for k in data_map if 'temp' in k])
    adjusted_latency = data_map['latency'] * (1 + temp_adjustment)
    
    # Real computation starts
    raw_scores = {}
    for metric in metrics:
        if metric == 'latency':
            # Lower latency is better: invert and scale
            raw_scores[metric] = (100 / (adjusted_latency + 1)) * base_weights[metric]
        elif metric == 'throughput':
            raw_scores[metric] = min(data_map[metric] * 0.01, 100) * base_weights[metric]
        elif metric == 'error_rate':
            # Lower error rate is better
            raw_scores[metric] = (100 - min(data_map[metric] * 10, 95)) * base_weights[metric]
    
    # Distractor: unused function and lambda
    validate_entry = lambda x: True if isinstance(x, dict) and 'status' in x else False
    health_check = {k: validate_entry(v) for k, v in data_map.items()}
    
    # Composite score calculation
    composite = sum(raw_scores.values()) * scaling_factor
    
    # Additional logic: bonus for balanced performance
    score_list = [raw_scores[m] for m in ['latency', 'throughput', 'error_rate']]
    variance_penalty = max(score_list) - min(score_list)
    balance_bonus = 5 if variance_penalty < 15 else 0
    
    # Final decision logic with conditional branch
    if composite > 75:
        final_score = int(composite + balance_bonus)
    else:
        final_score = int(composite)
    
    return final_score

# Setup data
benchmark_data = {
    'latency': 24,
    'throughput': 850,
    'error_rate': 1.2,
    'temp_sensor_1': 0.8,
    'temp_sensor_2': 0.6,
    'status': 'active'
}

metric_set = {'latency', 'throughput', 'error_rate'}

# Execution point
final_score = evaluate_performance(metric_set, benchmark_data)
print(f"Result: {final_score}")