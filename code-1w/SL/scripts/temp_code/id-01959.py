def analyze_sensor_data():
    raw_readings = [127, 255, 0, 191, 64, 223, 31, 159]
    baseline_offset = 32
    adjustment_steps = []
    
    # Preprocess readings with slicing and offset correction
    adjusted_readings = [x - baseline_offset for x in raw_readings]
    trimmed_readings = adjusted_readings[1:6]  # Focus on central window
    
    # Compute power metrics
    power_levels = [val ** 2 for val in trimmed_readings]
    total_power = sum(power_levels)
    avg_power = total_power / len(power_levels)
    
    # Distractor: Frequency analysis (not used)
    frequency_bins = {i: 0 for i in range(5)}
    for p in power_levels:
        bin_idx = min(i // 1000 for i in [p])
        if bin_idx < 5:
            frequency_bins[bin_idx] += 1
    
    # Signal filtering logic
    threshold = 2000
    valid_powers = [p for p in power_levels if p > threshold]
    filtered_power = sum(valid_powers) if valid_powers else avg_power
    
    # System state simulation
    system_status_code = 200
    system_active = system_status_code == 200
    
    # Correction mechanism using conditional expression
    temperature = 23.5
    correction_factor = 1.1 if temperature > 20 else 0.9
    
    # Key assignment with conditional expression
    signal_strength = filtered_power * correction_factor if system_active else 0
    
    # Irrelevant secondary computation (dead-end path)
    normalized_signals = [s / max(power_levels) for s in power_levels if s > 0]
    stability_score = len(normalized_signals) - 0.1 * sum(normalized_signals)
    
    # Final output
    print(f"Result: {signal_strength}")

analyze_sensor_data()