def analyze_data_stream(data_stream):
    # Simulate processing a stream of sensor readings
    threshold = 42
    offset = 17
    temp_buffer = []
    debug_log = []

    for i, reading in enumerate(data_stream):
        adjusted = reading - offset
        if adjusted > threshold:
            temp_buffer.append(adjusted)
            debug_log.append(f'High at {i}')
        elif adjusted == threshold:
            temp_buffer.append(adjusted * 0.5)
        else:
            temp_buffer.append(0)  # Below threshold, ignore

    # Misleading transformation: looks important but unused
    normalized = [round(x / max(temp_buffer), 2) for x in temp_buffer if x > 0]
    scaling_factor = sum(normalized) if normalized else 1.0

    # Actual logic: extract non-zero values above a secondary threshold
    secondary_threshold = 25
    relevant_values = [v for v in temp_buffer if v > secondary_threshold]
    
    # Red herring: complex-looking but unused conditional chain
    if len(relevant_values) > 3:
        fallback = [x for x in temp_buffer if x % 5 == 0]
        alternative_sum = sum(fallback)
        if alternative_sum > 100:
            relevant_values = relevant_values[:3]

    filtered_sum = sum(relevant_values)
    
    # Dead code: never executed but adds cognitive load
    if False:
        post_processed = [x << 1 for x in filtered_sum]

    return filtered_sum

# Input data
data_points = [60, 85, 52, 90, 38, 77, 45, 105]
result = analyze_data_stream(data_points)
print(f'Result: {result}')