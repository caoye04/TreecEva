def evaluate_performance(data, config):
    base = 0
    bonus = 0
    penalty = 0
    temp_result = {}

    # Irrelevant preprocessing: normalize unused fields
    normalized = {k: v / max(data.values()) for k, v in data.items()}
    
    # Real computation starts
    efficiency = data['efficiency']
    accuracy = data['accuracy']
    latency = data['latency']
    throughput = data['throughput']

    # Distractor: complex-looking but unused calculation
    projected_growth = sum([efficiency * 0.3, throughput * 0.1, accuracy * 0.2]) * 1.5

    # Actual logic
    if efficiency > 80:
        base += 20
        if accuracy >= 90:
            base += 30
        elif accuracy >= 75:
            base += 15
    else:
        penalty += 10

    if latency < 50:
        bonus += 15
    elif latency > 100:
        penalty += 20

    # Throughput affects score only if efficiency is high
    if efficiency > 70:
        base += min(throughput // 10, 25)

    # Weighted aggregation using lambda
    weight_func = lambda x, w: x * w
    weighted_accuracy = weight_func(accuracy, 0.4)
    weighted_efficiency = weight_func(efficiency, 0.3)

    # Unused dictionary operations (distractors)
    stats_summary = {
        'peak': max(data.values()),
        'deviation': sum(abs(v - 80) for v in data.values()) / len(data),
        'bonus_applied': bonus > 0
    }

    # Final score with modular adjustment
    raw_score = base - penalty + bonus
    final_mod = raw_score % 7
    final_score = int(weighted_accuracy + weighted_efficiency + 20 + final_mod)

    return final_score

# Main execution
metrics = {
    'efficiency': 85,
    'accuracy': 92,
    'latency': 45,
    'throughput': 180
}

weights = {'accuracy': 0.4, 'efficiency': 0.3, 'latency': 0.2, 'throughput': 0.1}

# Dead code path (never called)
def debug_trace():
    return [k for k in metrics.keys() if 'e' in k]

intermediate_value = sum(metrics.values()) / len(metrics)  # Unused

final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")