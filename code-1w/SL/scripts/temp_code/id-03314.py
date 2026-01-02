def analyze_sensor_data(raw_readings, thresholds):
    # Irrelevant preprocessing: Normalize readings (unused in final result)
    normalized = [x / max(raw_readings) for x in raw_readings]
    filtered = [x for x in raw_readings if x > thresholds[0]]

    # Misleading statistical block
    mean_val = sum(raw_readings) / len(raw_readings)
    variance = sum((x - mean_val) ** 2 for x in raw_readings) / len(raw_readings)
    entropy_proxy = -sum((x / sum(raw_readings)) * ((x / sum(raw_readings)) + 1e-9) for x in raw_readings)  # Dead end

    # Core logic disguised among distractors
    segment_a = raw_readings[:len(raw_readings)//2]
    segment_b = raw_readings[len(raw_readings)//2:]
    
    # Set-based anomaly detection (only one outcome matters)
    unique_a = set(segment_a)
    unique_b = set(segment_b)
    common_elements = unique_a & unique_b
    anomaly_detected = len(common_elements) < 2

    # Conditional expression with red herring branches
    base_score = 150 if len(segment_a) > 10 else 95
    adjustment = sum(1 for x in segment_b if x % 7 == 0) * 3

    # Decoy function definition (never called)
    def integrate_signal(data):
        return sum(x * i for i, x in enumerate(data))  # Unused

    # Simulated fault counter with misleading increments
    fault_counter = 0
    for val in raw_readings:
        if val < thresholds[1]:
            fault_counter += 1
        elif val > thresholds[2]:
            fault_counter += 2  # This path is irrelevant due to data

    # Critical nested logic determining actual answer
    if anomaly_detected:
        aggregate_score = base_score - adjustment
        temp_history = [(i, v) for i, v in enumerate(raw_readings) if v % 2 == 1]
        index_slice = temp_history[1:4]
        offset_value = sum(idx * val for idx, val in index_slice)
        if offset_value > 100:
            correction_factor = -5
        else:
            correction_factor = 12
    else:
        aggregate_score = base_score + adjustment
        correction_factor = -20  # Dead branch due to input

    # Key statement
    final_diagnostic = aggregate_score + correction_factor

    # Print required output
    print(f"Result: {final_diagnostic}")

    # Unused trailing operations
    checksum = sum(raw_readings[i] for i in range(0, len(raw_readings), 3)) % 17
    metadata_log = {'version': '2.1', 'valid': True, 'checksum': checksum}  # Logged but unused

    return final_diagnostic

# Input data crafted to follow specific execution path
sensor_input = [23, 15, 18, 31, 44, 7, 66, 39, 52, 29, 14, 35]
thresh = [10, 5, 50]

result = analyze_sensor_data(sensor_input, thresh)