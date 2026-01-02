def evaluate_performance(data, importance):
    base = 0
    adjustment = 0.0
    temp_result = []
    
    # Irrelevant pre-processing (distractor)
    noise_offset = sum([i * 0.1 for i in range(len(data))])
    dummy_cache = {f'key_{i}': i**2 for i in range(5)}  # Unused dict operation

    for key, value in data.items():
        if key == 'accuracy':
            base += value * importance[key]
        elif key == 'latency':
            # Higher latency reduces score
            adjustment -= (value / 10) * importance[key]
        elif key == 'throughput':
            # Throughput contributes positively
            temp_result.append(value * importance[key])
        elif key == 'energy':
            # Energy consumption penalty
            adjustment -= (value * 0.05) * importance[key]  # Minor penalty

    # Additional irrelevant computation
    outlier_check = [x for x in temp_result if x > 50]  # Not used later
    fallback_value = sum(dummy_cache.values()) / 100  # Dead-end calculation

    # Actual logic contributing to result
    throughput_contribution = sum(temp_result)
    final_score = base + throughput_contribution + adjustment

    # Red herring: conditional that never triggers due to data
    if 'debug_mode' in data and data['debug_mode']:
        final_score *= 1.1

    return final_score

# Main execution
metrics = {
    'accuracy': 92,
    'latency': 45,
    'throughput': 38,
    'energy': 76
}

weights = {
    'accuracy': 0.4,
    'latency': 0.3,
    'throughput': 0.25,
    'energy': 0.05
}

intermediate_calc = (metrics['accuracy'] + metrics['throughput']) // 2  # Distractor
baseline = 100 * 0.6  # Unused baseline

final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")