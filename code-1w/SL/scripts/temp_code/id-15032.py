def evaluate_performance(metrics, weights):
    # Normalize metrics using min-max scaling (irrelevant for final logic but adds distraction)
    normalized = {}
    for k, v in metrics.items():
        if v > 0:
            normalized[k] = (v - 0.1) / (1.0 + 0.1) if v < 1.0 else 0.9
        else:
            normalized[k] = 0.0

    # Secondary transformation: amplify certain dimensions (distractor)
    amplified = {k: v * 1.5 for k, v in normalized.items() if k in ['accuracy', 'latency']}

    # Core logic begins: weighted sum on original metrics with selective inclusion
    score_components = []
    for metric_name, weight in weights.items():
        if metric_name not in metrics:
            continue
        raw_value = metrics[metric_name]
        
        # Apply non-linear penalty if latency exceeds threshold
        if metric_name == 'latency' and raw_value > 0.5:
            raw_value = 1 / (1 + raw_value)  # diminishing returns
        
        weighted_contribution = raw_value * weight
        score_components.append(weighted_contribution)

    base_score = sum(score_components)

    # Conditional bonus based on tuple unpacking and slicing condition
    recent_history = [0.6, 0.7, 0.8, 0.75, 0.82, 0.78, 0.85]
    recent_improvement = recent_history[-3:]  # last three values
    improvement_trend = (recent_improvement[2] - recent_improvement[0]) > 0.02

    # Bonus logic with early return red herring
    bonus_applied = False
    if improvement_trend:
        potential_bonus = base_score * 0.1
        if potential_bonus > 0.05:
            base_score += potential_bonus
            bonus_applied = True
        else:
            # Dead code path — never reached due to data constraints
            base_score *= 1.02  # unreachable under current inputs

    # Irrelevant dictionary merging (adds complexity without impact)
    aux_data = {'version': '2.3', 'mode': 'optimized'}
    debug_snapshot = {**metrics, **aux_data}

    # Final adjustment: cap score at 1.0 if above threshold (never triggers here)
    capped_score = min(base_score, 1.0)

    # Key assignment point
    final_score = round(capped_score * 100, 2)  # scale to percentage, 2 decimal places

    return final_score


# Input data
model_metrics = {
    'accuracy': 0.88,
    'latency': 0.65,      # triggers non-linear penalty
    'throughput': 0.92,
    'memory_usage': 0.45
}

weights_config = {
    'accuracy': 0.4,
    'latency': 0.3,
    'throughput': 0.25,
    'energy_efficiency': 0.05  # not in metrics → skipped
}

# Execution entry point
final_score = evaluate_performance(model_metrics, weights_config)
print(f"Result: {final_score}")