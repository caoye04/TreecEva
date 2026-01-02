def analyze_sensor_data(readings):
    base_offset = 17
    threshold = 42
    adjusted_readings = [r + base_offset for r in readings]
    valid_readings = [val for val in adjusted_readings if val > threshold]
    
    # Apply bitwise filter to isolate odd fluctuation patterns
    processed_readings = []
    for x in valid_readings:
        if (x ^ threshold) & 1:  # Check least significant bit after XOR
            processed_readings.append(x)
    
    # Secondary filtering based on position parity
    filtered_readings = [processed_readings[i] for i in range(len(processed_readings)) if i % 2 == 0]
    energy_threshold = filtered_readings[-1] if filtered_readings else 0
    return energy_threshold

# Simulated input
input_readings = [10, 25, 30, 35, 40]
result = analyze_sensor_data(input_readings)
print(f"Target result: {result}")