def evaluate_performance(data, importance):
    # Simulate complex processing with distractions
    temp_results = {}
    adjusted_values = []
    
    # Irrelevant pre-processing (distractor)
    offset = sum(importance) * 0.1
    noise_factor = len(data) % 3

    for key, value in data.items():
        if key.startswith('err'):
            # Misleading transformation
            temp_results[key + '_adj'] = max(0, value - 0.5)
        elif key in ['pct_cpu', 'pct_mem']:
            # Relevant normalization
            temp_results[key + '_norm'] = value / 100.0

    # Real computation begins
    raw_scores = []
    for i, (k, v) in enumerate(data.items()):
        if k == 'throughput':
            raw_scores.append(v * 2)
        elif k == 'latency':
            raw_scores.append(1000 / max(v, 1))  # Avoid division by zero
        elif k == 'pct_cpu':
            raw_scores.append(100 - v)  # Invert usage

    # Use lambda for dynamic weighting (required feature)
    weighted_score = lambda score, weight: score * weight
    
    # Apply weights using dictionary and slicing (required features)
    relevant_weights = list(importance.values())[1:]  # Skip first (distractor)
    final_components = []
    for i in range(len(raw_scores)):
        try:
            w = relevant_weights[i]
            final_components.append(weighted_score(raw_scores[i], w))
        except IndexError:
            final_components.append(weighted_score(raw_scores[i], 1))  # Default

    aggregate = sum(final_components)
    
    # Dummy state tracking (irrelevant)
    status_log = {"processed": len(raw_scores), "aggregated": True}
    
    # Final score with adjustment
    penalty = 0
    if data['latency'] > 50:
        penalty += 5
    final_score = int(aggregate - penalty)

    # Unused dead code path (distractor)
    if False:
        backup_calc = [x ** 0.5 for x in final_components]
        final_score += sum(backup_calc)

    return final_score

# Input data
metrics = {
    'throughput': 45,
    'latency': 60,
    'pct_cpu': 75,
    'pct_mem': 85,
    'errors': 3
}

weights = {
    'base': 1.0,
    'thr': 1.2,
    'lat': 0.8,
    'cpu': 1.0
}

# Execution point
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")