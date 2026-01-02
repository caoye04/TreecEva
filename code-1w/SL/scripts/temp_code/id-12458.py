def evaluate_performance(log, base):
    adjustments = {'latency': 0.85, 'throughput': 1.15, 'error_rate': 0.9}
    weight_map = {'critical': 3, 'high': 2, 'medium': 1, 'low': 0.5}
    
    temp_vals = []
    for entry in log:
        metric = entry['metric']
        severity = entry['severity']
        raw_value = entry['value']
        
        if metric == 'latency':
            normalized = raw_value / base[metric]
            adjusted = normalized * adjustments[metric]
            weighted = adjusted * weight_map[severity]
            temp_vals.append(weighted)

    # Irrelevant computation block (distractor)
    outlier_count = 0
    for entry in log:
        if entry['value'] > 500 and entry['metric'] == 'throughput':
            outlier_count += 1  # Not used later
    
    avg_temp = sum(temp_vals) / len(temp_vals) if temp_vals else 0
    
    # Another distractor: unused transformation
    transformed_log = [{
        'raw': item['value'],
        'scaled': item['value'] * 0.1 if item['severity'] == 'critical' else item['value'] * 0.05
    } for item in log]
    
    # Actual final computation
    penalty_factor = 0.9 if len(transformed_log) > 3 else 1.0  # Depends on size, not content
    final_score = int(avg_temp * penalty_factor * 100)
    
    return final_score

# Main execution
baseline_config = {'latency': 120, 'throughput': 1000, 'error_rate': 0.02}
metrics_data = [
    {'metric': 'latency', 'value': 110, 'severity': 'high'},
    {'metric': 'latency', 'value': 130, 'severity': 'medium'},
    {'metric': 'latency', 'value': 95, 'severity': 'critical'},
    {'metric': 'latency', 'value': 140, 'severity': 'high'},
    {'metric': 'throughput', 'value': 950, 'severity': 'medium'}  # Not processed in main loop
]

result = evaluate_performance(metrics_data, baseline_config)
Target result: {result}