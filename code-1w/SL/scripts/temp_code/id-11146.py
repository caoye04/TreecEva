def analyze_signal_strength(readings):
    total = sum(readings)
    average = total / len(readings)
    
    # Normalize readings around average
    normalized = [round((x - average) * 2.5, 2) for x in readings]
    
    # Irrelevant metadata (minimal distraction)
    device_id = "SENSOR_XT9"
    calibration_offset = 0.05
    
    midpoint = len(normalized) // 2
    left_half = normalized[:midpoint]
    right_half = normalized[midpoint:]
    
    # Key computation
    threshold_score = max(normalized[:midpoint]) * min(normalized[midpoint:])
    
    # Additional unused variable (low interference)
    stability_index = sum(left_half) >= sum(right_half)
    
    return threshold_score

# Input data
sensor_readings = [12, 15, 18, 10, 22, 8, 14, 19]

result = analyze_signal_strength(sensor_readings)
print(f"Target result: {result}")