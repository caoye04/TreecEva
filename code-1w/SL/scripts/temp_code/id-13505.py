def analyze_sensor_readings(readings):
    threshold = 25
    secondary_limit = 15
    temp_buffer = []
    outlier_count = 0
    valid_segments = []

    for i, val in enumerate(readings):
        if val > threshold:
            temp_buffer.append(val)
        elif val < secondary_limit:
            outlier_count += 1
        else:
            if len(temp_buffer) >= 2:
                valid_segments.extend(temp_buffer)
            temp_buffer = []

    if len(temp_buffer) >= 2:
        valid_segments.extend(temp_buffer)

    # Misleading intermediate transformation
    adjusted_values = [x - 5 for x in readings if x % 2 == 0]
    cumulative = 0
    for v in adjusted_values:
        cumulative += v

    # Actual computation path
    clipped_data = [min(x, 30) for x in valid_segments]
    normalized = [x / 1.5 for x in clipped_data]  # This line doesn't affect final answer

    filtered_data = [x for x in clipped_data if x > 10]
    filtered_sum = sum(filtered_data)

    metadata = {
        'total_original': sum(readings),
        'cumulative_even_adjusted': cumulative,
        'outlier_count': outlier_count
    }

    return filtered_sum

# Simulated sensor data sequence
data_stream = [12, 20, 27, 33, 8, 14, 26, 29, 31, 22, 19, 24, 35]
result = analyze_sensor_readings(data_stream)
print(f"Result: {result}")