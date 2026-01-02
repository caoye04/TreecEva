def analyze_sensor_readings(raw_readings):
    filtered_data = [x for x in raw_readings if x > 0]
    offset = sum(filtered_data) // len(filtered_data) if filtered_data else 0
    
    # Irrelevant transformation (distractor)
    inverted = list(map(lambda x: 1 / (x + 1), filtered_data))
    cumulative_noise = sum(inverted[:len(inverted)//2])

    # Key data manipulation
    shifted = [x - offset for x in filtered_data]
    squared_devs = [(x - offset) ** 2 for x in filtered_data]
    variance_estimate = sum(squared_devs) / len(squared_devs) if squared_devs else 0

    # Secondary processing with slicing
    windowed_avg = sum(shifted[:5]) / len(shifted[:5]) if len(shifted) >= 5 else sum(shifted)
    
    # Distractor: unused intermediate calculation
    peak_magnitude = max(shifted, default=0) * min(shifted, default=1)
    normalized = [x / (max(shifted) + 1e-5) for x in shifted]

    # Core logic path
    processed_data = [int(x * windowed_avg) for x in normalized if x > 0.1]
    
    # Another red herring
    checksum = sum([processed_data[i] ^ i for i in range(len(processed_data))]) if processed_data else 0

    # Final computation chain
    adjustment = abs(variance_estimate - cumulative_noise)
    correction_factor = int(abs(windowed_avg) ** 0.5) + 1
    final_output = processed_data[0] * correction_factor if processed_data else -1
    
    return final_output

# Simulated sensor input
sensor_input = [12, -5, 18, 23, -1, 7, 15, 0, 11, 19]
result = analyze_sensor_readings(sensor_input)
final_output = result
print(f"Target result: {final_output}")