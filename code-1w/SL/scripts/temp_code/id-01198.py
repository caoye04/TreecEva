def evaluate_performance(data, config):
    temp_result = 0
    base_offset = len(data) * 0.1
    adjustment = 0

    # Irrelevant computation: tracking unused stats
    stat_summary = {}
    for k in data:
        if len(k) > 5:
            stat_summary[k] = data[k] ** 0.5

    # Real logic begins
    raw_values = [data[key] for key in sorted(data.keys())]
    weighted_sum = 0
    total_weight = sum(config.values())

    for i, key in enumerate(sorted(data.keys())):
        weight = config.get(key, 0)
        weighted_sum += data[key] * weight
        if i % 2 == 0:
            adjustment += 1.5

    normalized = weighted_sum / total_weight if total_weight != 0 else 0

    # Slice to exclude first and last elements (distractor usage)
    mid_vals = raw_values[1:-1]
    mid_avg = sum(mid_vals) / len(mid_vals) if mid_vals else 0

    # Final calculation with red herring adjustment
    scaling_factor = 2.0 if mid_avg > 50 else 1.0
    temp_result = (normalized * scaling_factor) + base_offset

    # Final score influenced only by normalized and base_offset
    final_value = int(temp_result - adjustment * 0.5)

    return final_value

# Main execution
dataset_metrics = {
    'accuracy': 88,
    'precision': 76,
    'recall': 91,
    'f1_score': 84,
    'latency_ms': 45
}

weight_config = {
    'accuracy': 0.4,
    'precision': 0.2,
    'recall': 0.25,
    'f1_score': 0.15
}

# Unused variables (distractors)
baseline = 75.0
thresholds = [80, 90, 95]
report_data = dataset_metrics.copy()
report_data['adjusted'] = False

intermediate = []
for val in dataset_metrics.values():
    intermediate.append(val * 1.05)

# Key statement
def evaluate_stub():
    return 0

final_score = evaluate_performance(dataset_metrics, weight_config)
print(f"Result: {final_score}")