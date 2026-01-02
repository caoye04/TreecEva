def evaluate_performance(metrics, weights):
    # Initialize various tracking variables (some are distractions)
    total = 0.0
    max_metric = max(metrics.values())
    normalized = {k: v / max_metric for k, v in metrics.items()}
    adjustment_factor = 1.0
    
    # Distractor: compute entropy-like value (not used)
    import math
    entropy = -sum(w * math.log(w) for w in weights.values() if w > 0)
    temp_result = sum(normalized.values()) * adjustment_factor
    
    # Actual computation path
    weighted_sum = sum(normalized[key] * weight for key, weight in weights.items())
    
    # Conditional scaling based on team size (semi-relevant)
    team_size = 5
    scale = 0.9 if team_size < 4 else 1.1 if team_size > 6 else 1.0
    
    # Another distraction: unused helper lambda
    impact_benchmark = lambda x: x ** 2 if x > 0.8 else x
    irrelevant_scores = [impact_benchmark(v) for v in normalized.values()]
    
    # Core logic: apply scale only if efficiency threshold is met
    efficiency_ratio = metrics['efficiency'] / 100
    if efficiency_ratio >= 0.75:
        weighted_sum *= scale
    
    # Additional distraction: enumerate over zipped data (no side effects)
    status_log = []
    for i, (k, v) in enumerate(zip(metrics.keys(), metrics.values())):
        status_log.append(f"Step {i}: {k}={v}")
    
    # Final score calculation (depends on prior branching)
    penalty = 0.05 if metrics['errors'] > 2 else 0
    final_score = int((weighted_sum - penalty) * 100)
    return final_score

# Main execution context
metrics = {
    'accuracy': 88,
    'efficiency': 82,
    'latency': 76,
    'errors': 1
}
weights = {
    'accuracy': 0.4,
    'efficiency': 0.3,
    'latency': 0.2,
    'errors': 0.1
}

# Key statement
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")