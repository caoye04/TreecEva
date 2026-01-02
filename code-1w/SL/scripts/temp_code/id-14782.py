def analyze_sensor_data(readings):
    adjusted_readings = [r * 0.95 for r in readings if r > 20]
    filtered_readings = [r for r in adjusted_readings if r < 100]
    
    # Irrelevant auxiliary calculation (minor distraction)
    baseline = sum(readings) / len(readings)
    anomaly_count = len([r for r in readings if r > 120])
    
    energy_threshold = max(filtered_readings)
    return energy_threshold

sensor_inputs = [15, 25, 35, 45, 55, 65, 75, 85, 95, 130]
result = analyze_sensor_data(sensor_inputs)
print(f"Target result: {result}")