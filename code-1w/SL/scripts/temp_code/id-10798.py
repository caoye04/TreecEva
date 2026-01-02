def analyze_sensor_data():
    temperature_readings = [23.5, 19.0, 27.3, 31.2, 25.8, 18.9, 22.1, 29.4]
    thresholds = {'min': 18.5, 'max': 30.0, 'optimal': 25.0}
    
    # Distractor: Initialize unrelated metrics
    humidity_levels = [45, 50, 52, 48, 55, 51, 47, 53]
    pressure_readings = [1013, 1015, 1012, 1010, 1014, 1016, 1011, 1009]
    avg_pressure = sum(pressure_readings) / len(pressure_readings)
    stability_index = 0
    for i in range(len(pressure_readings) - 1):
        stability_index += abs(pressure_readings[i] - pressure_readings[i + 1])
    
    # Real logic begins: Normalize temperatures relative to optimal
    deviation_scores = []
    for temp in temperature_readings:
        if temp < thresholds['min'] or temp > thresholds['max']:
            deviation_scores.append(10)  # Out of range penalty
        else:
            deviation = abs(temp - thresholds['optimal'])
            deviation_scores.append(round(deviation * 2, 2))
    
    # Use enumerate and zip (required Python features)
    adjustment_factors = [0.9, 1.1, 0.95, 1.05, 1.0, 0.88, 0.99, 1.02]
    adjusted_scores = []
    for idx, (score, factor) in enumerate(zip(deviation_scores, adjustment_factors)):
        adjusted = score * factor
        if idx % 2 == 0:
            adjusted -= 0.1  # Even indices get minor correction
        adjusted_scores.append(max(round(adjusted, 2), 0))
    
    # Secondary distractor: Analyze humidity trend (unused)
    increasing_humidity = 0
    for h1, h2 in zip(humidity_levels, humidity_levels[1:]):
        if h2 > h1:
            increasing_humidity += 1
    humidity_trend = increasing_humidity > len(humidity_levels) // 2
    
    # Core computation: Calculate final rating
    base_rating = 100.0
    penalty = sum(adjusted_scores)
    final_score = base_rating - penalty
    
    # Additional red herring: Bitwise manipulation on index count
    active_sensors = len([s for s in adjusted_scores if s > 0])
    checksum = active_sensors ^ 255  # Unused
    mask = checksum & 0xFF  # Dead code path
    
    return round(final_score, 2)

result = analyze_sensor_data()
print(f"Result: {result}")