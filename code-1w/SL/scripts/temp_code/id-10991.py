def analyze_sensor_readings(readings):
    baseline = 24.5
    offset = 1.3
    adjusted_readings = [r + offset for r in readings]
    
    # Apply calibration factor (simulated)
    calibrated = []
    for val in adjusted_readings:
        if val < 30.0:
            calibrated.append(val * 1.05)
        else:
            calibrated.append(val * 0.98)
    
    # Misleading transformation: not used in final result
    inverted = [100.0 - c for c in calibrated]
    avg_inverted = sum(inverted) / len(inverted) if inverted else 0
    deviation_score = abs(avg_inverted - 70.0)

    # Core processing path
    processed_data = [round(c, 1) for c in calibrated]
    temp_stats = {'min': min(processed_data), 'max': max(processed_data)}
    threshold = (temp_stats['min'] + temp_stats['max']) / 2.5

    # Key statement
    filtered_sum = sum([x for x in processed_data if x > threshold])

    # Dead code branch (never executed)
    debug_mode = False
    if debug_mode:
        print(f'Debug: {deviation_score=}')

    return filtered_sum

# Input data
sensor_inputs = [22.1, 25.3, 27.8, 29.1, 30.5, 26.7, 23.9]
result = analyze_sensor_readings(sensor_inputs)
print(f"Result: {result}")