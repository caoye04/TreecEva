def compute_efficiency(readings, threshold):
    filtered_data = [x for x in readings if x > threshold]
    adjustment_factor = 0.85 if len(filtered_data) > 3 else 1.15
    
    # Irrelevant accumulation (distractor)
    cumulative_error = 0
    for val in readings:
        if val < 10:
            cumulative_error += val * 0.01
        elif val > 50:
            cumulative_error -= val * 0.005

    # Semi-relevant normalization
    normalized = [max(0, temp - threshold) for temp in readings]
    total_normalized = sum(normalized)
    
    # Dead code path (misleading)
    if len(readings) == 0:
        return -999

    peak_reading = max(readings) if readings else 0
    efficiency_score = 0
    
    for i, temp in enumerate(filtered_data):
        contribution = temp * (0.9 ** i)  # Exponential decay weighting
        efficiency_score += contribution

    # Additional irrelevant transformation
    dummy_weights = [1.1, 0.9, 1.05]
    weighted_sum = sum(efficiency_score * w for w in dummy_weights[:1])  # Only first used

    final_score = efficiency_score * adjustment_factor
    
    # Key assignment point
    thermal_output = int(final_score + total_normalized) % 10000
    
    return thermal_output

# Sensor data from thermal array (real input)
temperature_readings = [18, 22, 26, 33, 41, 15, 29]

# Misleading auxiliary calculation
drift_correction = sum(t**2 for t in temperature_readings) / 1000

# Noise margin computation (not used)
noise_floor = len(temperature_readings) * 0.75

# Main execution
efficiency_baseline = 0.5 * sum(temperature_readings) / len(temperature_readings)
thermal_output = compute_efficiency(temperature_readings, threshold=25)

print(f"Result: {thermal_output}")