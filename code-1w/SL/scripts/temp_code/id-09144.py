def analyze_sensor_data(readings):
    threshold = 75
    safety_margin = 5
    adjusted_threshold = threshold + safety_margin
    
    # Irrelevant baseline (minimal distraction)
    calibration_offset = 2
    
    # Core logic: filter readings above adjusted threshold
    high_readings = [x for x in readings if x > adjusted_threshold]
    
    # Transform with lambda (non-trivial but relevant)
    processed = list(map(lambda val: val - calibration_offset, high_readings))
    
    # Further filter out values below strict threshold
    filtered_readings = {val for val in processed if val > 70}
    
    # Key computation point
    filtration_score = sum(filtered_readings)
    
    # Unrelated statistic (minor interference)
    peak = max(readings)  # not used further
    
    return filtration_score

# Input data
sensor_log = [68, 76, 82, 79, 88, 65, 90]
result = analyze_sensor_data(sensor_log)
filtration_score = result
print(f"Result: {filtration_score}")