def evaluate_performance(metrics, weights):
    # Irrelevant transformation: alters copy, not used
    shadow_metrics = {k: v ** 1.5 for k, v in metrics.items()}
    temp_offset = sum([len(str(int(v))) for v in weights.values()])

    # Distractor: complex but unused calculation
    phantom_score = 0
    for i in range(3):
        for j in range(4):
            phantom_score += (i * j) % 3

    # Actual metric processing begins
    adjusted_weights = {}
    for k, v in weights.items():
        if 'precision' in k:
            adjusted_weights[k] = v * 1.2
        elif 'recall' in k:
            adjusted_weights[k] = v * 0.9
        else:
            adjusted_weights[k] = v * 1.0

    # Set-based filtering: only use metrics present in both sets
    valid_keys = set(metrics.keys()) & set(adjusted_weights.keys())
    filtered_metrics = {k: metrics[k] for k in valid_keys}
    filtered_weights = {k: adjusted_weights[k] for k in valid_keys}

    # Conditional scoring with nested logic
    raw_score = 0.0
    for key in filtered_metrics:
        contribution = filtered_metrics[key] * filtered_weights[key]
        if contribution > 15:
            raw_score += contribution * 0.95
        elif contribution < 5:
            raw_score += contribution * 1.1
        else:
            raw_score += contribution

    # String-based adjustment factor (distractor)
    tag_line = "Performance_" + "_".join(sorted(valid_keys))
    adjustment_factor = len(tag_line) % 7

    # Final nonlinear scaling
    final_score = int((raw_score - adjustment_factor) // 1.3)
    
    return final_score

# Base inputs
metric_set = {
    'accuracy': 8.0,
    'precision_main': 12.5,
    'recall_main': 9.2,
    'f1_aux': 6.7
}

base_weights = {
    'precision_main': 2.0,
    'recall_main': 1.8,
    'specificity': 1.5,  # Not in metrics, will be excluded
    'accuracy': 2.2
}

# Execution point of interest
final_score = evaluate_performance(metric_set, base_weights)
print(f"Result: {final_score}")