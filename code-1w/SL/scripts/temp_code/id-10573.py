def analyze_sensor_data():
    raw_readings = [23.5, 45.0, 32.1, 67.8, 54.2]
    baseline = 20.0
    adjusted_readings = [x - baseline for x in raw_readings]
    
    # Irrelevant distraction: noise calibration (unused)
    reference_noise = [0.1, 0.3, 0.2]
    avg_noise = sum(reference_noise) / len(reference_noise)
    
    total_signal = sum(adjusted_readings)
    normalized_scores = [x / total_signal for x in adjusted_readings]
    safety_factor = 1.8
    energy_threshold = max(normalized_scores) * safety_factor
    
    # Additional distraction: secondary metric (not used in main result)
    peak_index = adjusted_readings.index(max(adjusted_readings))
    stability_ratio = min(normalized_scores) / max(normalized_scores)
    
    print(f"Result: {energy_threshold}")

analyze_sensor_data()