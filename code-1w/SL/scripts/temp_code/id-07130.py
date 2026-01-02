def analyze_sensor_data(temperatures, threshold):
    temperature_score = 0
    anomaly_count = 0
    baseline = sum(temperatures[:3]) / 3
    
    for i, temp in enumerate(temperatures):
        if temp > threshold:
            deviation = temp - baseline
            adjustment = deviation * 0.8 if deviation > 5 else deviation * 0.5
            temperature_score += int(adjustment)
            
        if i > 0 and (temperatures[i] ^ temperatures[i-1]) > 10:
            anomaly_count += 1
    
    result = temperature_score + anomaly_count
    return result

sensor_readings = [23.5, 25.0, 22.0, 35.0, 19.0, 42.0]
threshold_limit = 30.0
temperature_score = 10
anomaly_count = 2
final_output = analyze_sensor_data(sensor_readings, threshold_limit)
Result: {final_output}