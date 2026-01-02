def process_sensor_data(raw_readings, threshold, correction_factor):
    filtered_readings = [r for r in raw_readings if r > threshold]
    adjusted_readings = [r * 0.95 + 2.1 for r in filtered_readings]
    
    # Irrelevant tracking variable (minor distraction)
    valid_count = len(filtered_readings)
    
    if len(adjusted_readings) > 3:
        adjusted_readings = adjusted_readings[:3]
    
    # Key computation
    final_temperature = adjusted_readings[-1] * correction_factor
    
    # Additional unrelated transformation (low interference)
    status_flags = [str(temp).startswith('8') for temp in adjusted_readings]
    
    return final_temperature

# Input data
sensor_inputs = [15.4, 8.7, 12.1, 9.5, 6.3, 10.2]
limit = 9.0
correction = 1.05

result = process_sensor_data(sensor_inputs, limit, correction)
print(f"Result: {result}")