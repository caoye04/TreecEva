def evaluate_performance(metrics, weights):
    base_score = 0
    bonus = 0
    penalty = 0
    temp_result = 0

    # Irrelevant preprocessing: normalizing metrics (not used in final logic)
    normalized = {}
    for key in metrics:
        max_val = max(metrics[key])
        normalized[key] = [v / max_val for v in metrics[key]]

    # Distractor computation: calculating variance (unused)
    variances = {}
    for key in metrics:
        mean_val = sum(metrics[key]) / len(metrics[key])
        variances[key] = sum((x - mean_val) ** 2 for x in metrics[key]) / len(metrics[key])

    # Real logic begins: weighted sum on first elements
    for key in weights:
        if key in metrics and len(metrics[key]) > 0:
            base_score += metrics[key][0] * weights[key]

    # Bitwise interference: using XOR to compute 'bonus_trigger' (only one matters)
    bonus_trigger = 0
    for val in metrics['reliability']:
        bonus_trigger ^= int(val)  # XOR all reliability values

    if bonus_trigger > 5:
        bonus = 15
    else:
        bonus = 5  # dead code path (trigger never exceeds 5)

    # Conditional penalty based on latency threshold
    avg_latency = sum(metrics['latency']) / len(metrics['latency'])
    if avg_latency > 80:
        penalty = 20

    # Accumulation with distractor variables
    intermediate = base_score * 0.9 + bonus * 2  # semi-relevant but not final
    final_score = int(base_score - penalty + bonus)

    # Early return red herring (never reached due to structure)
    if final_score < 0:
        return 0

    return final_score

# Input data
metrics = {
    'accuracy': [92, 88, 95],
    'latency': [75, 82, 78],
    'reliability': [3, 4, 2, 1],
    'throughput': [120, 115, 130]
}

weights = {
    'accuracy': 1.5,
    'latency': 0.8,
    'reliability': 1.2
}

# Key execution point
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")