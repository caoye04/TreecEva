def evaluate_performance(metrics, weights):
    # Preprocessing: Normalize metrics
    normalized = {}
    temp_sum = 0
    for k in metrics:
        temp_sum += metrics[k] ** 2
    norm_factor = temp_sum ** 0.5
    
    for k in metrics:
        normalized[k] = metrics[k] / norm_factor
    
    # Irrelevant distraction: Calculate variance (not used later)
    mean_val = sum(metrics.values()) / len(metrics)
    variance = sum((v - mean_val) ** 2 for v in metrics.values()) / len(metrics)
    std_dev = variance ** 0.5
    pseudo_z_scores = {k: (v - mean_val) / std_dev for k, v in metrics.items()}

    # Weighted scoring with slicing-based weight adjustment
    adjusted_weights = weights[1:] + [weights[0]]  # Rotate weights
    sliced_metrics = list(metrics.values())[::2]  # Take every other metric

    # Core logic: compute dot product of normalized metrics and adjusted weights
    raw_score = 0
    for i, key in enumerate(normalized):
        if i < len(adjusted_weights):  # Avoid index error
            raw_score += normalized[key] * adjusted_weights[i]

    # Additional logic: apply non-linear boost if certain condition met
    stability_ratio = metrics['consistency'] / (metrics['errors'] + 1)
    bonus_factor = 0
    if stability_ratio > 2.0:
        bonus_factor = 0.1 * raw_score
    elif stability_ratio > 1.5:
        bonus_factor = 0.05 * raw_score

    final_score = raw_score + bonus_factor
    
    # Dead code path: never executed due to prior logic
    if std_dev < 0:
        final_score *= 0.9  # This will never happen

    return final_score

# Main execution
metrics = {
    'accuracy': 85,
    'consistency': 92,
    'speed': 78,
    'errors': 30
}

weights = [0.4, 0.3, 0.2, 0.1]

# Key computation point
final_score = evaluate_performance(metrics, weights)

print(f"Result: {final_score}")