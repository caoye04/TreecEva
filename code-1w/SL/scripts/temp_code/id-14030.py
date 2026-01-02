def calculate_performance(data):
    base_points = 0
    bonus_multiplier = 1.0
    
    # Extract relevant metrics
    accuracy = data['metrics']['accuracy']
    latency = data['metrics']['latency_ms']
    sample_count = data['samples']
    
    # Accumulate base points from correct classifications
    for result in data['results']:
        if result['correct']:
            base_points += 1
    
    # Apply latency-based performance bonus
    if latency < 50:
        bonus_multiplier += 0.2
    elif latency < 100:
        bonus_multiplier += 0.1

    # Adjust for edge case: high accuracy with low samples
    if accuracy > 0.95 and sample_count < 50:
        bonus_multiplier *= 0.9  # Slight penalty for small sample size

    # Calculate final score
    final_score = base_points * bonus_multiplier
    
    # Irrelevant utility (minimal distraction)
    temp_msg = "Processing complete."
    debug_flag = False
    
    return final_score

# Benchmark input data
benchmark_data = {
    'metrics': {
        'accuracy': 0.92,
        'latency_ms': 45
    },
    'samples': 85,
    'results': [
        {'correct': True},
        {'correct': True},
        {'correct': False},
        {'correct': True},
        {'correct': True}
    ]
}

result_value = calculate_performance(benchmark_data)
print(f"Result: {result_value}")