def analyze_sensor_data(raw_readings):
    offset = 10
    scaling_factor = 2.5
    adjusted_readings = [x + offset for x in raw_readings]
    scaled_values = [x * scaling_factor for x in adjusted_readings]
    
    # Apply moving average as noise reduction (distractor)
    smoothed = []
    for i in range(len(scaled_values)):
        if i == 0 or i == len(scaled_values) - 1:
            smoothed.append(scaled_values[i])
        else:
            avg_val = (scaled_values[i-1] + scaled_values[i] + scaled_values[i+1]) / 3
            smoothed.append(avg_val)
    
    # Normalize values relative to max (irrelevant to final answer)
    max_val = max(smoothed)
    normalized = [x / max_val for x in smoothed] if max_val != 0 else smoothed
    
    # Threshold filtering based on arbitrary criterion
    thresholded = [x for x in scaled_values if x > 30]
    
    # Simulate data packet segmentation (distractor)
    packet_size = 3
    packets = [thresholded[i:i+packet_size] for i in range(0, len(thresholded), packet_size)]
    reassembled = [val for pkt in packets for val in pkt]
    
    # Key processing: reverse and square elements above median
    sorted_vals = sorted(reassembled)
    median_val = sorted_vals[len(sorted_vals)//2] if sorted_vals else 0
    processed_data = []
    for x in reversed(reassembled):
        if x > median_val:
            processed_data.append(x ** 2)
        else:
            processed_data.append(x)
    
    # --- Critical execution point ---
    filtered_sum = sum(processed_data[1::2])  # Sum every second element starting from index 1
    
    # Extra unused variables and computations (distraction)
    checksum = sum(processed_data) % 1000
    outlier_count = len([x for x in processed_data if x > 1000])
    compression_ratio = len(raw_readings) / len(processed_data) if processed_data else 0
    
    print(f"Result: {filtered_sum}")

# Input data
data_stream = [4, 7, 6, 8, 5, 9, 2, 3]
analyze_sensor_data(data_stream)