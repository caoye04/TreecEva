def evaluate_performance(metrics, weights):
    base_score = 0
    penalty = 0
    bonus = 0

    # Irrelevant initialization (distractor)
    temp_data = {'buffer': [0]*5, 'offset': 12}
    checksum = sum(temp_data['buffer']) + temp_data['offset']

    # Real computation begins
    for key in metrics:
        if key in weights:
            base_score += metrics[key] * weights[key]

    # Conditional adjustment based on thresholds (modular arithmetic)
    if base_score % 7 == 0:
        penalty = (base_score // 10) % 5
    elif base_score % 3 == 0:
        bonus = 8

    # Simulated data smoothing (irrelevant to final logic)
    smoothed_values = []
    for i in range(len(metrics)):
        smoothed_values.append((i + 1) * 0.5)  # Dead-end calculation

    # Secondary logic path that looks important but isn't always triggered
    if 'response_time' in metrics and metrics['response_time'] < 200:
        bonus += 5

    # Final score with interference from irrelevant prior steps
    final_score = base_score - penalty + bonus

    # Additional red herring: unused transformation
    transformed_score = round(final_score ** 0.5, 3) if final_score > 0 else 0

    return final_score

# Main execution
metrics = {
    'throughput': 85,
    'accuracy': 92,
    'latency': 45,
    'response_time': 180
}

weights = {
    'throughput': 2,
    'accuracy': 3,
    'latency': 1
}

# Extraneous preprocessing (distractor)
calibration_factor = 1.05
adjusted_metrics = {k: v * calibration_factor for k, v in metrics.items()}

# Key statement
final_score = evaluate_performance(metrics, weights)

print(f"Result: {final_score}")