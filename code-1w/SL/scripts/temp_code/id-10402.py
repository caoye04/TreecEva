import math

# Simulated sensor data processing with diagnostic patterns
def analyze_sensor_readings(raw_readings, threshold=0.75):
    normalized = [x / max(raw_readings) for x in raw_readings]
    anomalies = []
    trend_magnitude = 0
    
    for i in range(1, len(normalized)):
        if abs(normalized[i] - normalized[i-1]) > threshold:
            anomalies.append(i)
        trend_magnitude += (normalized[i] - normalized[i-1]) ** 2

    # Irrelevant transformation - red herring
    fft_proxy = [math.sin(math.pi * x / 4) for x in range(len(normalized))]
    masked_signal = [a * b for a, b in zip(normalized, fft_proxy)]

    # Distractor: unused function
    def decoy_calibration(x):
        return (x ** 3 - 2 * x + 1) if x > 0.5 else x

    # Distractor variables
    calibration_factor = sum([math.exp(-i * 0.1) for i in range(10)])
    entropy_proxy = -sum([x * math.log(x + 1e-9) for x in normalized])

    return normalized, anomalies, math.sqrt(trend_magnitude)

# Advanced pattern matching engine
def match_diagnostic_patterns(processed, templates):
    best_match = None
    highest_correlation = -1

    for template in templates:
        # Cross-correlation with circular shift
        for shift in range(len(template)):
            shifted = template[shift:] + template[:shift]
            corr = sum(a * b for a, b in zip(processed, shifted))
            magnitude_a = math.sqrt(sum(a**2 for a in processed))
            magnitude_b = math.sqrt(sum(b**2 for b in shifted))
            if magnitude_a > 0 and magnitude_b > 0:
                normalized_corr = corr / (magnitude_a * magnitude_b)
                if normalized_corr > highest_correlation:
                    highest_correlation = normalized_corr
                    best_match = (shift, template)

    # Decoy logic path - never taken due to constraints
    if len(processed) > 100:
        fallback_score = 0
        for x in processed:
            fallback_score = (fallback_score * 31 + int(x * 1000)) % 997
        return fallback_score  # Dead code in practice

    return best_match, highest_correlation

# Core aggregation logic (relevant)
def aggregate_diagnostic(data_chunk, reference_pattern):
    chunk_avg = sum(data_chunk) / len(data_chunk)
    pattern_sum = sum(reference_pattern)
    
    # Key computation
    weighted_sync = sum(d * reference_pattern[i % len(reference_pattern)] 
                        for i, d in enumerate(data_chunk))
    
    # Redundant but plausible-looking normalization
    noise_floor = sum([abs(d - chunk_avg) for d in data_chunk]) / len(data_chunk)
    enhancement_factor = math.log(1 + noise_floor * 100) if noise_floor > 0.01 else 1
    
    # Distractor: complex but unused metric
    spectral_density = [((i+1)*weighted_sync) % 7 for i in range(5)]
    phantom_metric = sum(s * (idx+1) for idx, s in enumerate(spectral_density)) % 101

    final_score = int(weighted_sync * 100 + pattern_sum - 50)
    return final_score

# Irrelevant helper - simulates hardware interface
def simulate_hardware_response(code, delay_ms=0.5):
    response_map = {
        0: 0xAAAA,
        1: 0x5555,
        2: 0xFFFF,
        3: 0x1234
    }
    return response_map.get(code % 4, 0x0000)

# Unused cryptographic mimicry - distractor
def pseudo_hash_sequence(seq):
    hash_val = 5381
    for item in seq:
        hash_val = ((hash_val << 5) + hash_val + int(item * 1000)) & 0xFFFFFFFF
    return hash_val

# Main execution flow
if __name__ == "__main__":
    # Simulated input data
    sensor_input = [127, 240, 185, 93, 202, 158, 77, 225, 142, 105, 198, 163]
    
    # Step 1: Signal analysis
    cleaned, detected_anomalies, fluctuation_index = analyze_sensor_readings(sensor_input)
    
    # Step 2: Diagnostic pattern bank (Fibonacci ratios)
    golden_pattern = [0.236, 0.382, 0.618, 1.0, 1.618]
    harmonic_pattern = [0.5, 1.0, 1.5, 2.0, 2.5]
    test_templates = [golden_pattern, harmonic_pattern]
    
    # Step 3: Pattern matching
    matched_info, confidence = match_diagnostic_patterns(cleaned, test_templates)
    
    # Step 4: Data filtering based on anomaly detection (critical path)
    if len(detected_anomalies) > 0:
        filtered_indices = [i for i in range(len(cleaned)) if i not in detected_anomalies]
        filtered_data = [cleaned[i] for i in filtered_indices]
    else:
        filtered_data = cleaned.copy()
    
    # Step 5: Base pattern selection
    base_pattern = golden_pattern if matched_info[1] > 0.6 else harmonic_pattern
    
    # Step 6: Final diagnostic score calculation
    filtration_score = aggregate_diagnostic(filtered_data, base_pattern)
    
    # Output result as required
    print(f"Result: {filtration_score}")