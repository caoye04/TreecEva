def analyze_signal_integrity(raw_samples, baseline_offset):
    sample_peak = max(raw_samples)
    normalized_power = sample_peak - baseline_offset
    
    # Diagnostic sequence for hardware validation
    calibration_sequence = [3, 1, 4, 1, 5, 9, 2, 6]
    diagnostic_key = calibration_sequence[0] & calibration_sequence[2]  # Bitwise AND
    
    # Buffer monitoring with slicing
    monitor_buffer = [x * 2 for x in calibration_sequence]
    energy_threshold = None
    
    if normalized_power > 5:
        energy_threshold = monitor_buffer[2:5][::-1][0] ^ diagnostic_key  # XOR operation
    else:
        energy_threshold = monitor_buffer[1] + diagnostic_key
    
    return energy_threshold

# Simulate execution
data_stream = [2, 3, 6, 4]
bias = 1
target_result = analyze_signal_integrity(data_stream, bias)
print(f"Result: {target_result}")