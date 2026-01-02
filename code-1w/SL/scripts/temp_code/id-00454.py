def analyze_sensor_readings(readings):
    adjusted_readings = [x - 10 for x in readings]
    
    # Irrelevant distraction: temperature offset (not used in final calculation)
    temp_offset = 273.15
    kelvin_values = [x + temp_offset for x in adjusted_readings]  # unused
    
    # Core logic: identify anomalous spikes using bitwise signature
    spike_flags = [(x & 1) ^ 1 for x in adjusted_readings]  # 1 if even, 0 if odd
    
    # Filter data based on spike flags using zip and list comprehension
    paired_data = list(zip(adjusted_readings, spike_flags))
    filtered_data = [val for val, flag in paired_data if flag]
    
    # Compute final score
    filtration_score = sum(filtered_data)
    return filtration_score

# Sensor input (simulated)
data_stream = [15, 22, 30, 17, 44, 19, 50]
result = analyze_sensor_readings(data_stream)
filtration_score = result
print(f"Target result: {filtration_score}")