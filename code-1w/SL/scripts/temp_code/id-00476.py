def process_sensor_readings(readings):
    # Normalize readings by scaling factor
    scale_factor = 0.85
    normalized = [r * scale_factor for r in readings]

    # Apply noise filter (simulated with conditional logic)
    threshold = 50
    filtered_data = []
    temp_buffer = []
    overflow_count = 0

    for val in normalized:
        if val > threshold:
            temp_buffer.append(val)
            overflow_count += 1
        else:
            filtered_data.append(round(val + 0.1))

    # Simulate checksum calculation on filtered data
    def calculate_checksum(data):
        base = 17
        checksum = 0
        for i, v in enumerate(data):
            # Mix bitwise and arithmetic ops
            mixed = (v ^ i) + (base & i)
            checksum += mixed
        return checksum % 97

    # Irrelevant secondary processing (distractor)
    secondary_analysis = [x ** 0.5 for x in temp_buffer if x > 60]
    stats_summary = sum(secondary_analysis) if secondary_analysis else 0

    # Key computation
    filtered_checksum = calculate_checksum(filtered_data)

    # More red herring operations
    adjustment = len(temp_buffer) - overflow_count
    final_adjusted = filtered_checksum + (adjustment * 2)

    # Output target result
    print(f"Result: {filtered_checksum}")
    return filtered_checksum

# Input data
sensor_inputs = [58, 42, 67, 33, 71, 25, 12, 88, 19]
process_sensor_readings(sensor_inputs)