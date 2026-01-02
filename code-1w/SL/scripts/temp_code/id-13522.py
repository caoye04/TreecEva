def analyze_sensor_data(readings):
    min_signal = 1.5
    max_noise = 10.0
    scaling_factor = 2.3
    adjusted_readings = [x * scaling_factor for x in readings]
    
    # Filter out low-quality sensor readings
    filtered_readings = [r for r in adjusted_readings if r > min_signal and r < max_noise]
    
    # Determine energy threshold based on valid readings
    energy_threshold = max(filtered_readings) if filtered_readings else 0
    
    # Irrelevant auxiliary variable (minor distraction)
    avg_reading = sum(readings) / len(readings) if readings else 0
    
    return energy_threshold

# Main execution
sensor_inputs = [0.8, 1.2, 2.1, 3.5, 0.9]
result = analyze_sensor_data(sensor_inputs)
print(f"Result: {result}")