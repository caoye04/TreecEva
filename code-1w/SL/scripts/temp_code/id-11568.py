def analyze_metrics(data, thresholds):
    count = 0
    temp_vals = []
    for val in data:
        if val > thresholds['high']:
            count += 1
            temp_vals.append(val * 0.9)
        elif val < thresholds['low']:
            temp_vals.append(val * 1.1)
    return count

# Sensor readings over time
temperature_readings = [23.5, 18.0, 35.2, 41.8, 12.3, 29.7, 33.3]

# Thresholds for anomaly detection
anomaly_levels = {'low': 15.0, 'high': 35.0}

# Analyze anomalies (this call affects state perception but not final result directly)
anomaly_count = analyze_metrics(temperature_readings, anomaly_levels)

# Weighted assessment of performance across systems
assessments = {
    'system_a': [0.8, 0.75, 0.91],
    'system_b': [0.68, 0.82, 0.77],
    'system_c': [0.90, 0.88, 0.85]
}

# Unused backup weights (distractor)
backup_weights = [0.2, 0.2, 0.6]

weights = {'w1': 0.5, 'w2': 0.3, 'w3': 0.2}

# Helper function to compute weighted performance
def aggregate_performance(metrics, weight_dict):
    total = 0.0
    w_sum = weight_dict['w1'] + weight_dict['w2'] + weight_dict['w3']
    scaling_factor = 1.0 if abs(w_sum - 1.0) < 1e-5 else 0.0  # validation check
    
    intermediate_results = {}
    for key, values in metrics.items():
        # Apply weighting scheme
        weighted_val = (
            values[0] * weight_dict['w1'] + 
            values[1] * weight_dict['w2'] + 
            values[2] * weight_dict['w3']
        )
        intermediate_results[key] = weighted_val * scaling_factor
    
    # Aggregate final score
    aggregate = 0.0
    for res in intermediate_results.values():
        aggregate += res
    
    # Additional logic to simulate calibration offset
    calibration_log = []
    for i, reading in enumerate(temperature_readings[::2]):  # slicing every other
        adjusted = reading * 0.98
        calibration_log.append(adjusted)
    
    # Irrelevant transformation on calibration data (dead computation)
    processed_cal = {i: round(c**0.5, 3) for i, c in enumerate(calibration_log)}
    
    # Final adjustment based on valid aggregation only
    final_adjustment = len(processed_cal) % 3  # unused red herring
    return round(aggregate * 100, 2)  # scale to integer-friendly value

# Execute main computation
final_score = aggregate_performance(assessments, weights)

# Print result as required
print(f"Result: {final_score}")