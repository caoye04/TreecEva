def analyze_sensor_readings(readings):
    threshold = 75
    safety_margin = 5
    
    # Normalize readings using lambda
    normalized = list(map(lambda x: x * 1.1 if x < threshold else x * 0.9, readings))
    
    # Categorize high-risk values
    high_risk = {val for val in normalized if val > threshold + safety_margin}
    
    # Filter valid operational range (ignore high-risk)
    filtered_data = [val for val in normalized if val not in high_risk]
    
    # Compute final score from safe readings
    filtration_score = sum(filtered_data)
    
    # Irrelevant diagnostic variable (minor distraction)
    diagnostic_count = len([x for x in readings if x % 2 == 0])
    
    return filtration_score

# Sensor input data
sensor_inputs = [68, 70, 72, 80, 85]
result = analyze_sensor_readings(sensor_inputs)
filtration_score = result
print(f"Target result: {filtration_score}")