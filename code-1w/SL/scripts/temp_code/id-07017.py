def compute_filtration_score(readings):
    threshold = 75
    anomaly_mask = [x > threshold for x in readings]
    anomalies = [readings[i] for i in range(len(readings)) if anomaly_mask[i]]
    
    # Irrelevant distraction: temporal buffer (unused)
    temporal_buffer = [anomalies[-i-1] for i in range(len(anomalies))] if anomalies else []
    
    anomaly_set = set(anomalies)
    base_range = set(range(50, 100))
    critical_range = set(range(70, 86))
    overlap_zone = base_range & critical_range
    
    # Key computation
    filtration_score = len(anomaly_set & critical_range)
    
    # Additional slicing operation (moderate complexity)
    recent_anomalies = sorted(anomaly_set)[::-1][:3]  # Top 3 most severe
    severity_cap = sum(recent_anomalies) // len(recent_anomalies) if recent_anomalies else 0
    
    return filtration_score

# Simulated sensor readings
sensor_readings = [68, 76, 85, 92, 79, 81, 64, 88]
result = compute_filtration_score(sensor_readings)
print(f"Result: {result}")