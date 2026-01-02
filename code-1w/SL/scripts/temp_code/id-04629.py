def normalize_values(values):
    min_val = min(values)
    max_val = max(values)
    range_val = max_val - min_val
    if range_val == 0:
        return [1.0 for _ in values]
    return [(v - min_val) / range_val for v in values]

# Simulate sensor data drift correction
def correct_drift(signal, baseline=0.1):
    return [s + baseline * i for i, s in enumerate(signal)]

# Main scoring logic
def calculate_final_score(raw_data, importance_weights):
    # Step 1: Extract and preprocess relevant metrics
    raw_metrics = [raw_data['temp'], raw_data['pressure'], raw_data['humidity']]
    adjusted_metrics = correct_drift(raw_metrics, baseline=0.05)
    
    # Irrelevant transformation (distractor)
    squared_buffer = [x ** 2 for x in adjusted_metrics]
    temp_snapshot = {'reading_' + str(i): val for i, val in enumerate(squared_buffer)}

    # Step 2: Normalize each metric for fair weighting
    normalized = normalize_values(adjusted_metrics)
    
    # Step 3: Apply weight mapping using dictionary lookup
    weighted_scores = {}
    keys = ['temp', 'pressure', 'humidity']
    for i, key in enumerate(keys):
        weighted_scores[key] = normalized[i] * importance_weights[key]
    
    # Misleading intermediate aggregation (not used in final result)
    avg_weighted = sum(weighted_scores[k] for k in keys) / len(keys)
    ceiling_bonus = 1 if avg_weighted > 0.5 else 0  # Dead code - never added
    
    # Step 4: Conditional adjustment based on humidity threshold
    humidity_score = weighted_scores['humidity']
    if humidity_score > 0.3:
        weighted_scores['temp'] *= 1.1  # Boost temp reliability
    
    # Step 5: Final composition
    base_total = sum(weighted_scores[k] for k in keys)
    penalty_factor = 0.95 if raw_data['error_count'] > 0 else 1.0
    final_score = base_total * penalty_factor
    
    # Output target result
    print(f"Result: {final_score}")
    return final_score

# Input data
sensor_readings = {
    'temp': 72,
    'pressure': 1013,
    'humidity': 45,
    'error_count': 1
}

weights_scheme = {
    'temp': 0.4,
    'pressure': 0.35,
    'humidity': 0.25
}

# Execute main logic
final_score = calculate_final_score(sensor_readings, weights_scheme)