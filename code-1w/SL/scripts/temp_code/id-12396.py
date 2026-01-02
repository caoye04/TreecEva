def analyze_data_stream(data_packet):
    raw_checksum = 0
    temp_buffer = []
    for val in data_packet:
        raw_checksum += val * 2
        if val % 3 == 0 and val > 0:
            temp_buffer.append(val)

    # Misleading secondary processing (distractor)
    anomaly_count = 0
    for i in range(len(temp_buffer)):
        if temp_buffer[i] > 50:
            anomaly_count += 1
    normalized_score = anomaly_count * 1.5 if anomaly_count > 0 else 0.0

    # Core logic path
    processed_entries = [x for x in data_packet if x > 10]
    relevant_values = [x for x in processed_entries if x % 4 == 2]
    
    # Red herring: unused transformation chain
    shifted_data = [x >> 1 for x in processed_entries if x < 200]
    aggregated_flag = any((x & 1) for x in shifted_data)

    # Key assignment point
    filtered_sum = sum(relevant_values)
    
    # Final output
    print(f"Result: {filtered_sum}")

# Simulated sensor data stream
sensor_readings = [12, 15, 22, 36, 42, 55, 62, 78, 81, 94]
analyze_data_stream(sensor_readings)