def evaluate_performance(metrics, weights):
    base_score = 0
    adjustment_factor = 0.85
    temp_result = {}
    
    # Irrelevant pre-processing (distractor)
    for k in ['latency', 'throughput', 'error_rate']:
        if k not in metrics:
            metrics[k] = 0
    
    # Real computation begins
    weighted_sum = 0
    weight_total = sum(weights.values())
    
    for key, weight in weights.items():
        normalized_weight = weight / weight_total
        raw_value = metrics.get(key, 0)
        
        # Performance scaling with diminishing returns
        if raw_value > 50:
            scaled = 50 + (raw_value - 50) * 0.6
        else:
            scaled = raw_value
        
        contribution = scaled * normalized_weight
        weighted_sum += contribution
    
    # Secondary adjustment using lambda (relevant)
    apply_bonus = lambda x: x * 1.1 if x > 70 else x
    base_score = apply_bonus(weighted_sum)
    
    # Dead code path (distractor)
    if base_score < 0:
        recovery_mode = True
        base_score = abs(base_score)
    
    # Dictionary-based threshold logic (relevant)
    thresholds = {90: 'A', 80: 'B', 70: 'C', 60: 'D'}
    bonus_awarded = False
    for thresh in sorted(thresholds.keys(), reverse=True):
        if base_score >= thresh:
            if thresh >= 80:
                bonus_awarded = True
            break
    
    final_adjustment = 5 if bonus_awarded else -3
    final_score = int(base_score + final_adjustment)
    
    # Unused tracking variables (distractor)
    debug_log = []
    calculation_trace = {'steps': [], 'intermediates': {}}
    calculation_trace['intermediates']['first_pass'] = weighted_sum
    
    return final_score

# Main execution
metrics_data = {
    'latency': 45,
    'throughput': 85,
    'error_rate': 12
}

weights_config = {
    'latency': 3,
    'throughput': 5,
    'error_rate': 2
}

result_tracker = []
execution_time_snapshot = 1678901234

final_score = evaluate_performance(metrics_data, weights_config)
print(f"Result: {final_score}")