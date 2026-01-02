def calculate_energy_threshold(readings, min_level=100, adjustment_factor=0.85):
    adjusted_readings = [int(r * adjustment_factor) for r in readings]
    valid_readings = [r for r in adjusted_readings if r > min_level]
    smoothed_readings = []
    for i in range(1, len(valid_readings) - 1):
        avg = (valid_readings[i-1] + valid_readings[i] + valid_readings[i+1]) // 3
        smoothed_readings.append(avg)
    
    # Filter readings above the dynamic threshold
    dynamic_base = sum(smoothed_readings) // len(smoothed_readings) if smoothed_readings else min_level
    filtered_readings = [r for r in smoothed_readings if r >= dynamic_base]
    
    energy_threshold = filtered_readings[-1] if filtered_readings else 0
    return energy_threshold

# Simulated sensor readings
sensor_data = [120, 135, 98, 142, 160, 115, 178, 190, 89, 200]
result = calculate_energy_threshold(sensor_data)
print(f"Result: {result}")