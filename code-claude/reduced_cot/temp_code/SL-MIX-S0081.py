def analyze_energy_consumption(readings, factor=2.5):
    # Normalize readings based on time of day
    time_factors = [0.8, 1.0, 1.2, 1.5, 1.3, 1.1]
    normalized = []
    
    # Calculate average for normalization baseline
    baseline = sum(readings) / len(readings)
    threshold = baseline * 0.75
    
    # Apply time factors to readings
    for i, reading in enumerate(readings):
        time_index = i % len(time_factors)
        adjusted = reading * time_factors[time_index]
        normalized.append(adjusted)
    
    # Track anomalies for reporting (not used in final calculation)
    anomalies = []
    for i, reading in enumerate(readings):
        if reading > baseline * factor:
            anomalies.append((i, reading))
    
    # Process energy readings with a filter
    energy_readings = [r - threshold/2 if r > threshold else r for r in readings]
    
    # Calculate filtered total (key result)
    filtered_total = sum([energy for i, energy in enumerate(energy_readings) if energy > threshold and i % 2 == 0])
    
    # Calculate alternative metrics (not used in final answer)
    alt_metric = sum(normalized) / len(normalized) * 1.5
    efficiency_score = filtered_total / (sum(readings) + 0.001) * 100
    
    print(f"Result: {filtered_total}")
    return filtered_total

# Energy consumption readings over a period
readings = [45, 42, 87, 66, 53, 92, 55, 40]
result = analyze_energy_consumption(readings)