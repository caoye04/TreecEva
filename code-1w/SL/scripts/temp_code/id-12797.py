def analyze_efficiency(data):
    if not data:
        return 0
    avg = sum(data) / len(data)
    variance = sum((x - avg) ** 2 for x in data) / len(data)
    efficiency = (avg / (variance + 1)) if variance > 0 else avg
    return round(efficiency, 3)

# Simulate system metrics over time
temp_readings = [23.5, 24.1, 22.9, 25.0, 23.8]
pressure_levels = [1013, 1015, 1012, 1016, 1014]
response_times = [120, 115, 130, 125, 118]

# Irrelevant transformation - distractor
decoded_tags = list(map(lambda x: ''.join(reversed(x)), ['sensor_a', 'sensor_b', 'sensor_c']))

# Compute auxiliary stats - semi-relevant but not final
mean_temp = sum(temp_readings) / len(temp_readings)
mean_pressure = sum(pressure_levels) / len(pressure_levels)

# Normalize response times to [0,1] range using min-max scaling
min_rt, max_rt = min(response_times), max(response_times)
normalized_rt = [(t - min_rt) / (max_rt - min_rt + 1e-9) for t in response_times]

# Efficiency scores for each subsystem
thermal_eff = analyze_efficiency(temp_readings)
pressure_eff = analyze_efficiency(pressure_levels)
latency_eff = analyze_efficiency([1/x for x in response_times])  # Inverse for performance

# Weighted combination logic
metrics = [thermal_eff, pressure_eff, latency_eff, mean_temp]
weights = [0.3, 0.2, 0.4, 0.1]

# Misleading intermediate calculation - does not affect final result
temp_bias_correction = sum(1 for t in temp_readings if t > mean_temp) - len(temp_readings) // 2
adjustment_factor = abs(temp_bias_correction) * 0.05

# Core evaluation function
def evaluate_performance(mets, wts):
    if len(mets) != len(wts):
        return -1
    
    # Filter out any metric above threshold (simulating anomaly rejection)
    filtered_pairs = [(m, w) for m, w in zip(mets, wts) if m < 50 or w >= 0.25]
    
    # Apply dynamic weighting adjustment based on string pattern length (distractor)
    key_tag = 'sensor_a'
    modifier = len(key_tag) % 3 / 10.0  # Ranges from 0.0 to 0.6
    
    score = 0.0
    for i, (metric, weight) in enumerate(filtered_pairs):
        # Additional irrelevant conditional expression
        adjusted_weight = weight + modifier if i % 2 == 0 and len(normalized_rt) > 4 else weight
        score += metric * adjusted_weight
        
        # Early break simulation - only processes first three valid pairs
        if i >= 2:
            break
            # Dead code below - never reached
            score += 1000  # Red herring
    
    # Final nonlinear transformation
    final_value = round(score ** 1.1, 4) if score > 0 else 0
    return final_value

# Execute main computation
final_score = evaluate_performance(metrics, weights)

# Output result as required
print(f"Result: {final_score}")