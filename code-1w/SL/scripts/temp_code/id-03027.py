def evaluate_performance(weights, scores):
    # Normalize scores using min-max scaling (irrelevant for final result)
    min_score, max_score = min(scores), max(scores)
    normalized = [(s - min_score) / (max_score - min_score + 1e-8) for s in scores]

    # Apply weight mapping via dictionary
    weighted_components = {}
    for key in weights:
        if key in scores:
            weighted_components[key] = scores[key] * weights[key]
    
    # Misleading transformation: FFT-like frequency simulation (dead code path)
    fake_freq = sum([normalized[i] * (i % 2) for i in range(len(normalized))])
    adjusted_freq = fake_freq * 0.5 if fake_freq > 0.5 else fake_freq * 1.5

    # Real computation: use only specific keys
    relevant_keys = ['accuracy', 'latency', 'memory']
    total_weighted = 0
    total_applied_weight = 0
    
    for k in relevant_keys:
        if k in weighted_components:
            total_weighted += weighted_components[k]
            total_applied_weight += weights[k]
    
    # Final aggregation with rounding logic
    raw_average = total_weighted / (total_applied_weight + 1e-8)
    
    # Bonus logic based on logical conditions
    bonus_trigger = all(scores[k] >= 80 for k in ['accuracy', 'latency']) and scores['memory'] < 90
    bonus = 5 if bonus_trigger else 0

    # Integer division used in threshold check (semi-relevant)
    threshold_penalty = 0
    if scores['accuracy'] // 10 < 9:
        threshold_penalty = -2

    # Final score computation
    final_value = raw_average + bonus + threshold_penalty
    return round(final_value, 2)

# Main execution
metric_weights = {
    'accuracy': 0.5,
    'latency': 0.3,
    'memory': 0.2,
    'throughput': 0.1  # Unused weight (distractor)
}

raw_scores = {
    'accuracy': 92,
    'latency': 85,
    'memory': 88,
    'power': 75  # Irrelevant metric
}

# Lambda function to preprocess (not actually used but looks important)
preprocessor = lambda x: {k: v * 1.01 for k, v in x.items() if k in ['accuracy', 'latency']}
shadow_scores = preprocessor(raw_scores)  # Computed but unused

# Key statement
final_score = evaluate_performance(metric_weights, raw_scores)
print(f"Result: {final_score}")