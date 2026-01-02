def evaluate_performance(metrics):
    base_weights = [0.2, 0.3, 0.1, 0.25]
    adjustment_factor = 1.1
    adjusted_values = []

    for i, (name, value) in enumerate(zip(['latency', 'throughput', 'accuracy', 'energy'], metrics)):
        if name == 'latency':
            normalized = max(0, 100 - value) * base_weights[i]
        elif name == 'throughput':
            normalized = min(value, 90) * base_weights[i]
        elif name == 'accuracy':
            normalized = value * base_weights[i] if value >= 85 else 0
        else:
            normalized = (100 - value) * base_weights[i]

        adjusted = normalized * adjustment_factor if value > 0 else 0
        adjusted_values.append(round(adjusted))

    temp_offset = 5  # irrelevant variable
    buffer_flag = False  # distractor

    total_score = sum(adjusted_values)
    return total_score

result = evaluate_performance([85, 75, 92, 60])
print(f"Result: {result}")