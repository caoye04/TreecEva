def analyze_sensor_data():
    raw_readings = [105, 210, -98, 45, 150, -200, 305, 64, 88]
    
    # Normalize readings using lambda and handle negative values
    normalized = list(map(lambda x: abs(x) if x < 0 else x // 2, raw_readings))
    
    # Extract critical band using slicing: every second element starting from index 1
    critical_band = normalized[1::2]
    
    # Apply threshold filter and store intermediate result
    threshold = 100
    filtered_results = [val for val in critical_band if val > threshold]
    
    # Compute final score based on filtered data
    filtration_score = sum(filtered_results)
    
    # Irrelevant auxiliary variable (minor distraction, intervention level 5)
    baseline_avg = sum(raw_readings) / len(raw_readings)
    
    print(f"Result: {filtration_score}")

analyze_sensor_data()