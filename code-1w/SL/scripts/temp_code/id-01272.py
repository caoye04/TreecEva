def analyze_signal_integrity(raw_samples, calibration_factor=0.93):
    sample_size = len(raw_samples)
    baseline_shift = 0
    temporal_weights = [0.5 ** i for i in range(sample_size)]
    weighted_sum = sum(s * w for s, w in zip(raw_samples, temporal_weights))
    
    # Irrelevant audio-specific preprocessing (distractor)
    fft_magnitude = [abs(s) ** 2 for s in raw_samples]
    spectral_centroid = sum(i * m for i, m in enumerate(fft_magnitude)) / sum(fft_magnitude) if sum(fft_magnitude) > 0 else 0
    
    # Red herring: unused transformation chain
    transformed_buffer = [s * calibration_factor for s in raw_samples]
    normalized_buffer = [t / max(transformed_buffer) for t in transformed_buffer] if transformed_buffer else []
    string_signature = ''.join([chr(int(abs(t) % 26) + 97) for t in transformed_buffer[:5]])
    signature_length = len(string_signature.strip())
    
    # Actual relevant logic begins here
    valid_readings = [s for s in raw_samples if -4.0 <= s <= 4.0]
    reading_count = len(valid_readings)
    
    # Simulate multi-stage filtering
    filtered_readings = []
    outlier_count = 0
    for idx, r in enumerate(valid_readings):
        if abs(r) > 3.0:
            outlier_count += 1
            continue
        if idx % 3 == 0 and r < 0:
            baseline_shift -= r * 0.1
        filtered_readings.append(r + baseline_shift)
    
    # Compute intermediate metrics (some irrelevant)
    mean_filtered = sum(filtered_readings) / len(filtered_readings) if filtered_readings else 0
    variance_proxy = sum((r - mean_filtered) ** 2 for r in filtered_readings) / len(filtered_readings) if filtered_readings else 0
    peak_deviation = max(filtered_readings, default=0) - min(filtered_readings, default=0)
    
    # Distractor: complex but unused conditional structure
    security_flag = False
    if variance_proxy > 2.0:
        for ch in string_signature:
            if ch in 'aeiou':
                security_flag = True
                break
        if security_flag:
            adjustment_cycle = 0
            while adjustment_cycle < 5:
                adjustment_cycle += 1
                spectral_centroid *= 0.95

    # Core diagnostic logic (buried among distractors)
    aggregate_threshold = 0
    if reading_count > 5:
        aggregate_threshold += 15
    if outlier_count < 3:
        aggregate_threshold += 8
    if peak_deviation < 4.5:
        aggregate_threshold += 12

    # Anomaly scoring based on filtered pattern
    zero_crossings = 0
    for i in range(1, len(filtered_readings)):
        if (filtered_readings[i-1] >= 0) != (filtered_readings[i] >= 0):
            zero_crossings += 1
    anomaly_score = 0
    if zero_crossings > 4:
        anomaly_score += 5
    elif zero_crossings == 0:
        anomaly_score -= 3
    else:
        anomaly_score += 1

    # Key assignment - this is where the answer is determined
    final_diagnostic = aggregate_threshold + anomaly_score
    
    # Dead code path - never executed due to fixed condition (red herring)
    if False:
        backup_system = [f * 1.1 for f in filtered_readings]
        recovery_offset = sum(backup_system) % 7
        final_diagnostic -= recovery_offset
    
    # Output must be printed
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Input data crafted to yield deterministic result
input_samples = [1.2, -2.1, 3.4, -1.8, 0.9, 2.7, -0.5, 1.3, 2.9, -3.2]
analyze_signal_integrity(input_samples)