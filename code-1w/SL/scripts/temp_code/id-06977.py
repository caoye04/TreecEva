def evaluate_performance(data, config):
    base = 0
    bonus = 0
    penalty = 0
    adjustment_factor = 0.95
    
    # Irrelevant preprocessing (distractor)
    temp_data = {k: v * 1.01 for k, v in data.items()}
    outlier_check = [v for v in temp_data.values() if v > 100]
    if len(outlier_check) > 2:
        adjustment_factor *= 0.9

    # Core logic with lambda (required feature)
    scale = lambda x, w: round(x * w * adjustment_factor, 2)
    
    # Real computation path
    for key, value in data.items():
        weight = config.get(key, 1.0)
        if key.startswith('efficiency'):
            base += scale(value, weight)
        elif key.endswith('accuracy'):
            base += scale(value, weight)
            bonus += value * 0.1  # Minor bonus logic
        elif 'latency' in key:
            if value > 50:
                penalty += (value - 50) * 0.2
    
    # Dead code branch (irrelevant)
    debug_trace = []
    for i in range(3):
        debug_trace.append(f'Step {i}: inactive')
    
    # Secondary distractor: unused helper dict
    stats_summary = {
        'max_val': max(data.values()),
        'min_val': min(data.values()),
        'range': max(data.values()) - min(data.values()),
        'ignored_metric': sum(v**2 for v in data.values()) // len(data)
    }
    
    # Final calculation
    raw_score = base - penalty + bonus
    normalized = max(0, min(100, raw_score))  # Clamp to 0-100
    final_score = int(round(normalized, 0))
    return final_score

# Main execution
metrics = {
    'efficiency_cpu': 85,
    'efficiency_memory': 76,
    'output_accuracy': 92,
    'input_accuracy': 88,
    'latency_response': 65,
    'latency_startup': 40
}

weights = {
    'efficiency_cpu': 1.2,
    'efficiency_memory': 1.1,
    'output_accuracy': 1.3,
    'input_accuracy': 1.0,
    'latency_response': 0.8
}

intermediate_total = sum(metrics[k] * weights.get(k, 1) for k in metrics) / len(metrics)

# Key statement
final_score = evaluate_performance(metrics, weights)

print(f"Result: {final_score}")