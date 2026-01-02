def main():
    # Simulated sensor data processing with red herrings
    raw_readings = [23.5, 18.2, 99.9, 45.1, 67.3, 12.8, 88.0, 33.6, 54.2, 76.8]
    calibration_offset = 1.27
    scaling_factor = 0.98
    temp_threshold = 85.0
    anomaly_flag = False

    # Irrelevant statistical decoys
    mean_value = sum(raw_readings) / len(raw_readings)
    variance = sum((x - mean_value) ** 2 for x in raw_readings) / len(raw_readings)
    std_deviation = variance ** 0.5

    # Data filtering (only some steps are relevant)
    filtered_data = [x for x in raw_readings if x < temp_threshold]
    scaled_data = [round((x + calibration_offset) * scaling_factor, 2) for x in filtered_data]

    # Misleading transformation branch (dead path)
    if anomaly_flag:
        processed_data = [x * 1.5 for x in scaled_data if x > 50]
    else:
        processed_data = [x for x in scaled_data]

    # Checksum pre-image construction (slicing used here)
    working_slice = processed_data[1:-1]  # Remove first and last
    inverted = [round(100 - x, 2) for x in working_slice]
    doubled = [x * 2 for x in inverted[:len(inverted)//2]]  # First half only

    # Dummy operations to distract
    magnitude_sum = sum(x ** 2 for x in doubled) ** 0.5
    normalized_doubled = [x / magnitude_sum for x in doubled] if magnitude_sum else []

    # Core logic buried among noise
    bitstream = ''.join([bin(int(x))[2:] for x in map(int, inverted)])
    popcount = sum(1 for c in bitstream if c == '1')

    # Buffer preparation with case conversion red herring
    temp_buffer = list(map(int, inverted))
    temp_buffer.append(popcount)

    # Decoy function call (does nothing impactful)
    def analyze_distribution(data):
        return sorted(data)[::2]  # Unused result
    
    analysis_result = analyze_distribution(temp_buffer)  # Dead code

    # Final transform uses slicing and arithmetic
    def final_transform(buf):
        segment_a = buf[:3]
        segment_b = buf[-3:]
        product_a = 1
        for val in segment_a:
            product_a *= val
        sum_b = sum(segment_b)
        return (product_a - sum_b) // 2 if sum_b != 0 else product_a

    checksum = final_transform(temp_buffer)

    # Unrelated string manipulation (distractor)
    status_label = "System OK"
    status_label = status_label.lower()
    status_label = status_label.upper()[::-1]

    # Early return guard (not triggered)
    if len(temp_buffer) > 20:
        return -999

    print(f"Result: {checksum}")

if __name__ == "__main__":
    main()