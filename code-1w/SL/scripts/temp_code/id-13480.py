def analyze_sensor_array(raw_readings, calibration_factor):
    adjusted_values = [x * calibration_factor for x in raw_readings if x > 0]
    
    # Irrelevant signal smoothing (dead path)
    smoothed = []
    for i in range(len(adjusted_values)):
        if i == 0 or i == len(adjusted_values) - 1:
            smoothed.append(adjusted_values[i])
        else:
            smoothed.append((adjusted_values[i-1] + adjusted_values[i] + adjusted_values[i+1]) / 3)

    # Distractor: Frequency analysis with unused result
    magnitude_spectrum = list(map(lambda val: abs(val) ** 0.5, adjusted_values))
    avg_magnitude = sum(magnitude_spectrum) / len(magnitude_spectrum)
    high_freq_components = [m for m in magnitude_spectrum if m > avg_magnitude]

    # Real processing path begins here
    binary_flags = []
    for val in adjusted_values:
        bit_encoded = int(val) ^ 255  # Bitwise XOR for encoding
        parity = bin(bit_encoded).count('1') % 2
        binary_flags.append(parity)

    # Aggregation using tuple unpacking and conditional logic
    ones_count = sum(binary_flags)
    zeros_count = len(binary_flags) - ones_count
    dominance, ratio = (1, ones_count / zeros_count) if ones_count > zeros_count else (0, zeros_count / ones_count)

    # Nested structure with early exit red herring
    def validate_coherence(data):
        if len(data) < 5:
            return False
        cumulative_xor = 0
        for item in data[:4]:
            cumulative_xor ^= int(item)
        return cumulative_xor == 255  # Unmet condition, never triggers

    coherence = validate_coherence(adjusted_values)  # Always False, misleading

    # Critical data transformation
    aggregated_data = (
        sum(adjusted_values),
        len([v for v in adjusted_values if v > 50]),
        ratio,
        dominance
    )

    # Threshold function with closure (lambda usage)
    base_ref = aggregated_data[0] / (len(adjusted_values) + 1)
    threshold_func = lambda x, offset=3.14: x > (base_ref * 1.2 + offset)

    # Decoy statistical computation (never used)
    z_scores = [(v - base_ref) / (base_ref * 0.1 + 1e-5) for v in adjusted_values]
    outlier_flags = [abs(z) > 2.5 for z in z_scores]
    anomaly_rate = sum(outlier_flags) / len(outlier_flags) if outlier_flags else 0

    # Actual answer computation
    def process_metrics(metrics_tuple, threshold_checker):
        total_signal, strong_readings, dominance_ratio, dominant_bit = metrics_tuple
        
        # Simulated hardware constraint check
        if total_signal < 100:
            return -1
            
        # Multi-step diagnostic logic
        score_a = total_signal // 10
        score_b = strong_readings * 15
        
        temp_result = score_a ^ score_b  # Bitwise combination
        normalized = temp_result & 1023  # Mask to 10 bits
        
        # Conditional amplification
        if threshold_checker(dominance_ratio):
            normalized *= 2
        
        # Final adjustment based on dominance bit
        final_value = normalized + dominant_bit
        
        # Dead branch: power efficiency simulation (unused)
        if dominant_bit == 1:
            efficiency_estimate = normalized / (total_signal * 0.01 + 1)
            calibrated_output = efficiency_estimate * 100

        return final_value

    final_diagnostic = process_metrics(aggregated_data, threshold_func)
    print(f"Result: {final_diagnostic}")