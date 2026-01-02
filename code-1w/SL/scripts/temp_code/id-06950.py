def calculate_final_score(records, importance_weights):
    base_adjustment = 0.0
    temp_offset = 0.0
    
    # Irrelevant preprocessing: normalize names (not used in score)
    normalized_names = [name.strip().title() for name in records.get('participants', [])]
    
    # Distraction: unused transformation of weights
    _ = [(k, v * 1.5) for k, v in importance_weights.items() if v > 0.2]
    
    raw_values = records.get('metrics', {})
    
    # Real computation begins
    weighted_sum = sum(
        raw_values.get(key, 0) * importance_weights.get(key, 0)
        for key in ['accuracy', 'latency', 'throughput', 'energy']
    )
    
    # Secondary adjustment based on thresholds
    threshold_bonus = 0
    if raw_values.get('accuracy', 0) >= 0.85:
        threshold_bonus += 10
    if raw_values.get('latency', float('inf')) <= 50:
        threshold_bonus += 5
    
    # Dummy loop with side-effect-free operations
    debug_logs = []
    for i in range(3):
        temp = (i + 1) * 100
        debug_logs.append(f'Simulated debug {temp}')

    # Final composition
    base_adjustment = weighted_sum * 10
    final_score = base_adjustment + threshold_bonus

    return int(final_score)

# Input data
experiment_data = {
    'participants': [' alice ', 'BOB', 'charlie '],
    'metrics': {
        'accuracy': 0.88,
        'latency': 45,
        'throughput': 120,
        'energy': 75
    }
}

weights_scheme = {
    'accuracy': 0.4,
    'latency': 0.3,
    'throughput': 0.2,
    'energy': 0.1
}

# Execution point
final_score = calculate_final_score(experiment_data, weights_scheme)
print(f"Result: {final_score}")