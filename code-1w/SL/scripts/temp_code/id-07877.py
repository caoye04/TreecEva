def evaluate_performance(metrics, weights):
    raw_total = sum(metrics)
    weight_factor = sum(weights) / len(weights)
    adjusted_metrics = [m * w for m, w in zip(metrics, weights)]
    
    # Irrelevant string processing (distractor)
    status_labels = ['low', 'medium', 'high']
    status_map = {i: label.upper() for i, label in enumerate(status_labels)}
    classification = status_map.get(len(metrics), 'UNKNOWN')
    
    # Semi-relevant preprocessing
    normalized = []
    max_metric = max(metrics)
    for val in metrics:
        if val > 0:
            normalized.append(round(val / max_metric, 4))
        else:
            normalized.append(0)
    
    # Core logic hidden among distractions
    scaling_factor = 1.0
    if len(normalized) >= 3:
        mid_values = normalized[1:-1]
        if sum(mid_values) > 1.0:
            scaling_factor = 0.8
    
    # Actual score computation
    base_score = sum(adjusted_metrics)
    penalty = 0
    for i, (m, n) in enumerate(zip(metrics, normalized)):
        if i % 2 == 0 and n < 0.5:
            penalty += m * 0.1
    
    final_score = base_score - penalty
    final_score *= scaling_factor
    
    # Dead code path (irrelevant)
    if classification == 'CRITICAL':
        backup = [x for x in metrics if x > 5]
        final_score += len(backup)

    return int(final_score)

# Main execution
metrics = [8, 5, 12, 7, 3]
weights = [0.2, 0.4, 0.8, 0.5, 0.1]

# Preprocessing distraction
combined = list(zip(metrics, weights))
indices = [i for i, _ in enumerate(combined) if _[0] > 4]
duplicate_check = ''.join(str(int(w * 10)) for w in weights)

# Key statement
final_score = evaluate_performance(metrics, weights)

print(f"Result: {final_score}")