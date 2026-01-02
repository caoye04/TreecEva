def evaluate_performance(metrics, data):
    base_weights = {'accuracy': 0.4, 'latency': 0.3, 'throughput': 0.2, 'energy': 0.1}
    derived_metrics = {k: v * 100 if k == 'accuracy' else v for k, v in data.items()}
    
    # Irrelevant transformation on unused copy
    shadow_data = {k: v * 1.5 for k, v in data.items()}
    shadow_data['dummy'] = 999

    # Semi-relevant filtering
    valid_keys = set(base_weights.keys()) & metrics
    filtered_data = {k: derived_metrics[k] for k in valid_keys}

    # Distractor: complex but unused list comprehension
    outlier_check = [v for k, v in filtered_data.items() if v < 50 and k != 'latency']
    temp_adjustments = [v * 0.95 for v in filtered_data.values() if v > 60]

    # Core logic hidden among noise
    raw_sum = sum(filtered_data.values())
    weight_sum = sum(base_weights[k] for k in valid_keys)
    normalized = raw_sum * (0.8 + 0.2 * (len(valid_keys) / len(base_weights)))

    # Final computation
    adjustment_factor = 1.0
    if 'latency' in valid_keys and data['latency'] < 0.05:
        adjustment_factor = 0.9
    final_score = int(normalized * weight_sum * adjustment_factor)
    
    # Additional red herring variables
    debug_trace = [f"{k}:{v}" for k, v in filtered_data.items()]
    auxiliary_total = sum(v ** 0.5 for v in data.values())
    
    return final_score

# Main execution context
metric_set = {'accuracy', 'throughput', 'energy'}
benchmark_data = {
    'accuracy': 0.92,
    'latency': 0.06,
    'throughput': 450,
    'energy': 88
}

interim_result = sum(benchmark_data[k] for k in ['accuracy', 'throughput'])
diagnostic_log = [x for x in benchmark_data.values() if x > 10]

final_score = evaluate_performance(metric_set, benchmark_data)
print(f"Result: {final_score}")