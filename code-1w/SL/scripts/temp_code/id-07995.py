def evaluate_performance(metrics, data_map):
    base_threshold = 85
    penalty_factor = 0.9
    bonus_multiplier = 1.2
    temp_result = 0
    final_score = 0
    
    # Irrelevant metric tracking (distractor)
    historical_max = max(data_map['raw_values'])
    normalized_offsets = [x - min(data_map['raw_values']) for x in data_map['raw_values']]
    
    # Real computation begins
    valid_metrics = {'accuracy', 'latency', 'throughput'} & metrics
    
    if 'accuracy' in valid_metrics:
        acc_score = data_map['accuracy_score']
        if acc_score >= base_threshold:
            temp_result += acc_score * bonus_multiplier
        else:
            temp_result += acc_score * penalty_factor

    if 'latency' in valid_metrics:
        latency_norm = 100 - data_map['avg_latency_ms']
        temp_result += latency_norm

    if 'throughput' in valid_metrics:
        throughput_val = data_map['throughput_kops']
        adjustment = 5 if throughput_val > 20 else -3
        temp_result += throughput_val + adjustment

    # Distractor: unused transformation
    inverted_data = data_map['raw_values'][::-1]
    shadow_sum = sum(inverted_data[:3]) * 0.1  # Not used

    # Final aggregation with slicing distraction
    recent_trends = data_map['trend_history'][-4:]
    trend_boost = sum(recent_trends) / len(recent_trends) if recent_trends else 0

    final_score = int(temp_result + trend_boost)

    # Dead code branch (misleading)
    if False:
        fallback_score = sum(data_map['raw_values']) // len(data_map['raw_values'])
        final_score = fallback_score

    return final_score

# Input data setup
metric_set = {'accuracy', 'throughput', 'power_efficiency', 'scalability'}
benchmark_data = {
    'accuracy_score': 88,
    'avg_latency_ms': 12,
    'throughput_kops': 25,
    'raw_values': [76, 88, 91, 84, 90],
    'trend_history': [85, 87, 86, 88, 89]
}

# Execution
final_score = evaluate_performance(metric_set, benchmark_data)
print(f"Result: {final_score}")