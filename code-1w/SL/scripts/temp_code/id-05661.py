def evaluate_performance(temperatures, thresholds):
    above_threshold = [temp for temp in temperatures if temp > thresholds[0]]
    scaled = [t * 0.85 for t in above_threshold]
    normalized = [(val - min(scaled)) / (max(scaled) - min(scaled)) for val in scaled] if len(scaled) > 1 else [0]
    backup_scores = [abs(t - thresholds[1]) for t in temperatures]
    final_score = max(normalized)
    return final_score

# Sensor data from industrial chamber
sensor_readings = [23.5, 27.8, 31.2, 35.6, 29.4, 38.1, 25.0]
threshold_config = [30.0, 25.0]

result = evaluate_performance(sensor_readings, threshold_config)
print(f"Result: {result}")