def analyze_sensor_data():
    raw_readings = [105, 202, 187, 93, 256, 77, 150, 301]
    anomaly_threshold = 100
    safety_factor = 1.5

    # Normalize readings and flag anomalies
    normalized = [x / safety_factor for x in raw_readings]
    
    # Identify anomalies above adjusted threshold
    adjusted_threshold = anomaly_threshold * 0.8
    is_anomaly = [val > adjusted_threshold for val in normalized]
    
    # Extract anomalous values
    filtered_anomalies = [int(normalized[i]) for i in range(len(normalized)) if is_anomaly[i]]
    
    # Compute final score
    filtration_score = sum(filtered_anomalies)
    
    # Irrelevant tracking variable (minor distraction)
    reading_count = len(raw_readings)
    
    print(f"Result: {filtration_score}")

analyze_sensor_data()