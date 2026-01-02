def evaluate_performance(metrics, weights):
    base_score = 0
    adjustment = 0
    temp_result = {}
    
    # Irrelevant preprocessing: normalize metrics (not actually used in final logic)
    normalized = {k: v / 100 for k, v in metrics.items()}
    
    # Real computation begins
    for key in weights:
        if key == 'accuracy':
            base_score += metrics[key] * weights[key]
        elif key == 'latency':
            # Lower latency is better, so invert impact
            adjustment -= int(metrics[key] / 10) * weights[key]
        elif key == 'throughput':
            base_score += (metrics[key] // 50) * weights[key]

    # Distractor: complex-looking lambda that's not used
    decay_factor = lambda x: x * 0.9 + 10 if x > 50 else x * 1.1
    unused_correction = [decay_factor(v) for v in metrics.values()]

    # Conditional adjustment based on combined threshold
    if metrics['accuracy'] >= 85 and metrics['throughput'] >= 200:
        bonus = 15
        if metrics['errors'] < 5:
            bonus += 10
        adjustment += bonus

    # Another red herring: dictionary operations that don't affect outcome
    temp_result['snapshot'] = {**metrics, 'timestamp': 123456789}
    temp_result['flags'] = [k for k, v in metrics.items() if v > 50]

    # Final score calculation
    final_score = base_score + adjustment
    
    return final_score

# Main execution
metrics = {
    'accuracy': 88,
    'latency': 45,
    'throughput': 220,
    'errors': 3,
    'retries': 7
}

weights = {
    'accuracy': 2,
    'latency': 1,
    'throughput': 3
}

final_score = evaluate_performance(metrics, weights)
print(f"Target result: {final_score}")