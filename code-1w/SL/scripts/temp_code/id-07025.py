def analyze_sensor_array(raw_readings, calibration_factor):
    # Irrelevant preprocessing block (dead path)
    temp_snapshot = [x * 0.98 for x in raw_readings if x > 50]
    outlier_count = 0
    normalized = []
    for val in raw_readings:
        if val < 0 or val > 1023:
            outlier_count += 1
        else:
            normalized.append(val * calibration_factor)

    # Distractor: unused transformation chain
    shifted = [((x >> 2) & 255) for x in normalized]
    encoded = ''.join([chr(x % 95 + 32) for x in shifted[:10] if x % 2 == 0])
    entropy_approx = sum([shifted[i] ^ shifted[i-1] for i in range(1, len(shifted))]) if len(shifted) > 1 else 0

    # Real processing begins: filter valid sensor indices
    valid_indices = []
    for i, v in enumerate(normalized):
        if v > 100 and i % 2 == 0:
            valid_indices.append(i)

    # Distractor: decoy function call with side effects that don't matter
    def apply_noise_correction(data, level=1):
        return [x + (i % level) for i, x in enumerate(data)]

    decoy_enhanced = apply_noise_correction(normalized, level=3)

    # Actual relevant data extraction
    filtered_data = [normalized[i] for i in valid_indices]

    # Complex mapping setup with red herring entries
    mode_thresholds = {'A': 150, 'B': 200, 'C': 250}
    fallback_config = {'base': 100, 'margin': 15}
    threshold_map = {
        'primary': mode_thresholds['B'],
        'secondary': fallback_config['base'] + 50,
        'spare': sum(fallback_config.values()) * 2  # Distractor value
    }

    # Core logic hidden among noise
    def process_readings(data, limits):
        cumulative = 0
        weights = [1.1, 0.9, 1.2, 0.8][:len(data)]
        for idx, reading in enumerate(data):
            # Key computation step
            if reading > limits['primary']:
                adjustment = (reading - limits['primary']) // 10
                cumulative += adjustment * weights[idx % len(weights)]
            elif reading > limits['secondary']:
                cumulative += 5
        # Additional logic using enumerate and zip
        for i, (a, b) in enumerate(zip(data, data[1:])):
            if a < b and i % 2 == 0:
                cumulative += 2
        return int(cumulative)

    # Decoy aggregation (never used)
    peak_magnitude = max(normalized) - min(normalized)
    trend_score = sum([b - a for a, b in zip(normalized, normalized[1:])])

    # Critical assignment - answer depends on this
    final_diagnostic = process_readings(filtered_data, threshold_map)

    # Red herring output
    debug_info = f"Outliers: {outlier_count}, Entropy: {entropy_approx}, Encoded: {encoded}"
    
    # Correct output
    print(f"Result: {final_diagnostic}")

    return final_diagnostic

# Input data
sensor_input = [200, 85, 320, 90, 150, 700, 410, 60, 505]
calibration = 1.05

result = analyze_sensor_array(sensor_input, calibration)