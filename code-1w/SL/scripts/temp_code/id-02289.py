def evaluate_performance(metrics, weights):
    base_score = 0
    bonus_factor = 1.0
    penalty_applied = False

    temp_values = []
    for i, (key, value) in enumerate(zip(metrics.keys(), metrics.values())):
        if i % 2 == 0 and value > 50:
            base_score += value * weights[key] * 0.1
            temp_values.append(value * 0.1)
        else:
            adjusted = value * 0.05
            temp_values.append(adjusted)

    # Irrelevant aggregation
    avg_temp = sum(temp_values) / len(temp_values) if temp_values else 0
    dummy_counter = 0
    for val in temp_values:
        if val > avg_temp:
            dummy_counter += 1

    # Actual logic continues
    outlier_count = 0
    for value in metrics.values():
        if value < 30 or value > 90:
            outlier_count += 1

    if outlier_count >= 3:
        penalty_applied = True
        bonus_factor = 0.8

    consistency_bonus = 1.0
    sorted_vals = sorted(metrics.values())
    for i in range(1, len(sorted_vals)):
        if sorted_vals[i] - sorted_vals[i-1] < 5:
            consistency_bonus += 0.02

    # Main computation
    for key, value in metrics.items():
        weight = weights.get(key, 0.1)
        contribution = value * weight
        base_score += contribution * 0.2

    final_score = base_score * bonus_factor * consistency_bonus

    # Dead code - misleading
    if penalty_applied:
        redundant_adjustment = final_score * 0.95
        final_score = final_score  # no-op

    return final_score

# Input data
metrics = {
    'accuracy': 85,
    'latency': 45,
    'throughput': 95,
    'memory_usage': 60,
    'cpu_efficiency': 70,
    'error_rate': 20
}
weights = {
    'accuracy': 0.3,
    'latency': 0.15,
    'throughput': 0.25,
    'memory_usage': 0.1,
    'cpu_efficiency': 0.15,
    'error_rate': 0.05
}

intermediate_result = [x * 0.5 for x in metrics.values()]
dummy_sum = sum(intermediate_result)

final_score = evaluate_performance(metrics, weights)
print(f"Target result: {final_score}")