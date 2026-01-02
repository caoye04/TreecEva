def calculate_system_state():
    # Simulate sensor readings with noise
    raw_readings = [105, 210, 98, 207, 102, 215, 95]
    
    # Derived values from hardware calibration
    base_offset = 100
    gain_factor = 1.05
    temperature_drift = 2.3
    
    # Apply gain and drift correction (some sensors)
    corrected = [(x * gain_factor) + temperature_drift for x in raw_readings]
    
    # Reference thresholds (used in diagnostics, not final calculation)
    warning_threshold = 110
    critical_threshold = 120
    diagnostic_flags = [1 if val > warning_threshold else 0 for val in corrected]
    
    # Extract differential changes between consecutive readings
    deltas = []
    for i in range(1, len(corrected)):
        deltas.append(corrected[i] - corrected[i-1])
    
    # Filter small fluctuations below sensitivity threshold
    sensitivity_floor = 4.0
    filtered_deltas = [d for d in deltas if abs(d) > sensitivity_floor]
    
    # Offset based on system baseline
    offset = sum([base_offset * 0.01 for _ in range(len(raw_readings))])  # Small cumulative effect
    
    # Secondary derived metric (unused red herring)
    peak_deviation = max([abs(x - base_offset) for x in raw_readings])
    stability_score = len([x for x in deltas if abs(x) < 10])  # Not used
    
    # Key computation point
    net_flux = sum(filtered_deltas) - offset
    
    # Diagnostic log output (irrelevant to result)
    avg_corrected = sum(corrected) / len(corrected)
    variance = sum((x - avg_corrected) ** 2 for x in corrected) / len(corrected)
    
    print(f"Result: {net_flux}")

calculate_system_state()