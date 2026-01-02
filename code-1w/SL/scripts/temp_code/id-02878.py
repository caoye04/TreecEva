def evaluate_performance(metrics, weights):
    # Precompute transformed metrics with some irrelevant transformations
    transformed = {}
    temp_vals = []
    for k, v in metrics.items():
        if k == 'accuracy':
            transformed[k] = v ** 2
        elif k == 'latency':
            transformed[k] = max(1.0, 100 / (v + 1))
        else:
            transformed[k] = v * 0.5  # Unused path (distractor)
    
    # Irrelevant list processing (distractor)
    for i in range(len(weights)):
        temp_vals.append(weights[i] * (i + 1))
    
    # Real computation begins: weighted sum on selected keys
    score = 0.0
    norm_factor = sum(weights)
    key_order = ['accuracy', 'latency', 'memory']
    
    # Simulate state tracking with red herring counters
    step_count = 0
    debug_log = []
    for idx, key in enumerate(key_order):
        if key in transformed:
            weight = weights[idx]
            contribution = transformed[key] * weight
            score += contribution
            step_count += 1
            debug_log.append(f'Step {step_count}: {key} added')
    
    # Final normalization
    normalized_score = score / norm_factor
    
    # Additional distraction: unused recursive helper
    def _unused_recursive(x):
        return x if x <= 1 else _unused_recursive(x - 1) + _unused_recursive(x - 2)
    
    # Another distraction: lambda that's defined but not used
    impact_factor = lambda x, y: x * y * 0.1
    
    # Final adjustment based on conditional logic (only depends on normalized_score)
    if normalized_score > 50:
        final_adjustment = 10
    else:
        final_adjustment = 5
    
    return int(normalized_score + final_adjustment)

# Main execution
if __name__ == '__main__':
    # Input data
    system_metrics = {
        'accuracy': 8,
        'latency': 20,
        'memory': 150,
        'throughput': 45  # This key will be ignored
    }
    
    # Weights for scoring (aligned with key_order)
    importance_weights = [6, 2, 2]
    
    # Dummy variables to increase cognitive load
    baseline_ref = 75
    calibration_data = [0.1 * i for i in range(10)]
    temp_result = sum(calibration_data)
    
    # Critical statement
    final_score = evaluate_performance(system_metrics, importance_weights)
    
    # Output result
    print(f"Result: {final_score}")