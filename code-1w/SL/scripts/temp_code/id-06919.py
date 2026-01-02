def analyze_sensor_data():
    raw_readings = [0.85, 1.2, 0.93, 1.07, 0.68, 1.15, 0.74, 1.3]
    baseline = 1.0
    
    # Normalize readings relative to baseline
    normalized = [x / baseline for x in raw_readings]
    
    # Apply noise filter: only keep values within 20% of baseline
    filtered_readings = [x for x in normalized if 0.8 <= x <= 1.2]
    
    # Sort to identify trend
    filtered_readings.sort()
    
    # Calculate phase correction using bitwise stability flag
    signal_stability = 0b1010
    phase_bits = signal_stability & 0b1100
    phase_correction = (phase_bits >> 2) + 1
    
    # Final threshold computation
    energy_threshold = filtered_readings[-1] * phase_correction
    
    print(f"Result: {energy_threshold}")

analyze_sensor_data()