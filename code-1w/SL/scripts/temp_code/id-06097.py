def evaluate_performance(metrics, weights):
    # Normalize metrics (irrelevant for final result but adds computation)
    normalized = {}
    total_metric = sum(metrics.values())
    for k, v in metrics.items():
        normalized[k] = v / total_metric if total_metric != 0 else 0

    # Calculate weighted score - this is where final_score is determined
    raw_scores = {k: metrics[k] * weights.get(k, 1) for k in metrics}
    adjustment_factor = 1.2 if sum(raw_scores.values()) > 50 else 0.9
    
    # Distractor: complex conditional updates that don't affect final path
    temp_state = {'active': True, 'stage': 2}
    if temp_state['active'] and temp_state['stage'] == 2:
        temp_state['counter'] = 0
        for i in range(3):
            temp_state['counter'] += i ** 2

    # Irrelevant set operations
    used_keys = set(metrics.keys())
    required_keys = {'accuracy', 'latency', 'throughput'}
    missing = required_keys - used_keys
    extra = used_keys - required_keys
    completeness = len(required_keys - missing) / len(required_keys)

    # Actual score calculation (depends on raw scores and adjustment)
    base_score = sum(raw_scores.values())
    adjusted_score = base_score * adjustment_factor
    
    # Additional distraction: unused branching logic
    if completeness < 0.8:
        fallback = 0
        for k in sorted(raw_scores):
            fallback += raw_scores[k] * 0.5
        adjusted_score = fallback  # not taken due to data

    # Final scoring with clamped bonus
    bonus = 5 if adjusted_score > 70 and 'throughput' in metrics else 0
    final_score = int(adjusted_score + bonus)

    return final_score

# Main execution
if __name__ == '__main__':
    # Input data
    system_metrics = {
        'accuracy': 85,
        'latency': 12,
        'throughput': 45,
        'energy': 67,
        'robustness': 34
    }
    
    importance_weights = {
        'accuracy': 1.1,
        'latency': 0.8,
        'throughput': 1.3
    }
    
    # Dead code - never called
    def debug_print(state):
        return {k: f'{v:.2f}' for k, v in state.items()}
    
    # Intermediate variables for distraction
    avg_metric = sum(system_metrics.values()) / len(system_metrics)
    metric_variance = sum((v - avg_metric) ** 2 for v in system_metrics.values()) / len(system_metrics)
    
    # Key statement
    final_score = evaluate_performance(system_metrics, importance_weights)
    
    print(f"Result: {final_score}")