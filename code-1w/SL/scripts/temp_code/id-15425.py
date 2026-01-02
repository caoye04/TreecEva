def evaluate_performance(data, importance):
    base = sum(data[metric] * importance.get(metric, 0) for metric in data)
    adjustment = 0
    
    # Irrelevant computation: tracking unused statistics
    temp_values = [data[m] ** 0.5 for m in data if m.endswith('_count')]
    avg_temp = sum(temp_values) / len(temp_values) if temp_values else 0
    dummy_flag = avg_temp > 5
    
    # Conditional logic with red herring branch
    if base > 100:
        adjustment += 10
    elif base < 50:
        adjustment -= 5
    else:
        # This branch looks important but doesn't trigger
        hidden_penalty = lambda x: x * 0.1
        adjustment -= hidden_penalty(base)

    # Key transformation using dictionary and conditional expression
    multiplier = 1.5 if any(data[m] > 20 for m in ['efficiency', 'accuracy']) else 1.0
    
    # Accumulation with distractor variables
    total_ops = data['throughput_count'] + data['latency_count']
    ops_factor = total_ops // 10 if total_ops > 0 else 0  # Unused in final result
    
    # Final score calculation - depends only on base, adjustment, and multiplier
    final_score = (base + adjustment) * multiplier
    
    # Dead code: misleading post-processing
    if final_score < 0:
        final_score = 0
    final_score = round(final_score, 4)
    
    return final_score

# Input data
metrics = {
    'efficiency': 18,
    'accuracy': 22,
    'throughput_count': 45,
    'latency_count': 12,
    'resource_usage': 8
}

weights = {
    'efficiency': 2.0,
    'accuracy': 3.0,
    'throughput_count': 0.5,
    'latency_count': 0.3
}

# Execution point
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")