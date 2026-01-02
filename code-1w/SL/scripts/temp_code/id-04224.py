def process_sensor_readings(readings):
    # Convert readings to absolute values and normalize case (simulated with scaling)
    processed = [abs(x) * 0.1 for x in readings]

    # Define outlier condition using lambda
    is_outlier = lambda x: x > 5.0

    # Filter out outliers
    filtered_data = [x for x in processed if not is_outlier(x)]

    # Additional unrelated but harmless variable
    temp_correction_factor = 1.02

    # Compute sum of filtered data
    filtered_sum = sum(filtered_data)
    
    return filtered_sum

# Simulated sensor input
sensor_input = [-75, 200, -300, 400, 150]
result = process_sensor_readings(sensor_input)
filtered_sum = result
print(f"Result: {filtered_sum}")