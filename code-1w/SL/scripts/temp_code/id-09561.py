def analyze_sensor_readings(readings):
    threshold = 75
    safety_margin = 5
    upper_limit = threshold + safety_margin
    
    # Convert readings to uppercase equivalents (simulated case conversion for digital modes)
    mode_flags = [str(r).upper() for r in [1, 0, 1]]  # Irrelevant string operation - minor distraction
    
    # Define filtering condition using lambda
    is_critical = lambda x: x > upper_limit
    
    # Filter data above critical threshold
    filtered_data = [r for r in readings if is_critical(r)]
    
    # Additional unrelated computation (minor distractor)
    avg = sum(readings) / len(readings) if readings else 0
    deviation = abs(avg - threshold)
    
    # Key statement
    filtration_score = sum(filtered_data)
    return filtration_score

# Sensor readings from industrial equipment
readings = [68, 72, 80, 95, 60, 78]
result = analyze_sensor_readings(readings)
print(f"Target result: {result}")