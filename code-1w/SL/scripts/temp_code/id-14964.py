def analyze_sensor_readings():
    raw_readings = [105, 230, 98, 110, 205, 95, 120, 180, 102]
    threshold = 100
    
    # Extract recent high-frequency samples (last 7 entries)
    recent_samples = raw_readings[-7:]
    
    # Identify anomalies above threshold
    anomalies = [x for x in recent_samples if x > 200]
    anomaly_count = len(anomalies)
    
    # Filter valid operational readings below threshold
    filtered_data = [x for x in recent_samples if x < threshold]
    
    # Compute summary statistics
    filtered_sum = sum(filtered_data)
    avg_anomaly = sum(anomalies) / anomaly_count if anomaly_count > 0 else 0
    
    # Output target result
    print(f"Result: {filtered_sum}")

analyze_sensor_readings()