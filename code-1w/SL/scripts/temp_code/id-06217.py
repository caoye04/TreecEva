def evaluate_performance(weights, data):
    base_multiplier = 1.5
    adjustment_factor = 0.8
    temp_result = 0
    final_score = 0
    
    # Irrelevant preprocessing: character frequency analysis (distractor)
    char_frequencies = {}
    for entry in data['logs']:
        for char in entry.lower():
            if char.isalpha():
                char_frequencies[char] = char_frequencies.get(char, 0) + 1
    
    # Semi-relevant normalization step (not used in final logic)
    max_freq = max(char_frequencies.values()) if char_frequencies else 1
    normalized_freqs = {k: v / max_freq for k, v in char_frequencies.items()}
    
    # Real computation begins
    raw_metrics = {
        'latency': sum(data['metrics']['latency']) / len(data['metrics']['latency']),
        'throughput': sum(data['metrics']['throughput']),
        'error_rate': len([e for e in data['errors'] if e > 0])
    }
    
    # Weighted scoring using dictionary and list comprehension
    weighted_components = [
        raw_metrics[metric] * weight 
        for metric, weight in weights.items() if metric in raw_metrics
    ]
    
    # Apply non-linear transformation via lambda (used in final result)
    transform = lambda x: x ** 1.1 if x > 0 else 0
    transformed = sum(map(transform, weighted_components))
    
    # Additional distraction: unused state tracking
    state_log = []
    for i in range(3):
        state_log.append(f'Stage {i+1}: Active')
    
    # Final calculation with adjustment (this affects output)
    temp_result = transformed * base_multiplier
    final_score = int(temp_result * adjustment_factor)
    
    # Dead code path (never executed)
    if False:
        fallback = sum(normalized_freqs.values()) * 100
        final_score = fallback
    
    return final_score

# Input data setup
metric_weights = {
    'latency': 0.3,
    'throughput': 0.5,
    'error_rate': -0.2
}

raw_data = {
    'metrics': {
        'latency': [120, 140, 110, 135],
        'throughput': [880, 920, 850]
    },
    'errors': [0, 1, 0, 0, 2],
    'logs': ['SystemOK', 'ErrCode1', 'Normal', 'Retry']
}

# Execution point
final_score = evaluate_performance(metric_weights, raw_data)
print(f"Result: {final_score}")