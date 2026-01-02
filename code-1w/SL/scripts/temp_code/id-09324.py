def analyze_thermal_readings(sensor_data, thresholds):
    cumulative_shift = 0
    peak_magnitude = 0
    temp_history = []
    adjustment_log = {}

    for i, reading in enumerate(sensor_data):
        if reading > thresholds['high']:
            cumulative_shift += 0.5
        elif reading < thresholds['low']:
            cumulative_shift -= 0.3

        smoothed = reading * (1 + cumulative_shift / 100)
        temp_history.append(smoothed)

        if abs(smoothed) > peak_magnitude:
            peak_magnitude = abs(smoothed)

    normalized_history = [val / peak_magnitude for val in temp_history if peak_magnitude != 0]

    # Simulate windowed analysis
    segment_patterns = {}
    for j in range(0, len(normalized_history) - 3):
        segment = tuple(normalized_history[j:j+3])
        segment_patterns[segment] = segment_patterns.get(segment, 0) + 1

    # Identify most frequent pattern
    dominant_pattern = max(segment_patterns, key=segment_patterns.get) if segment_patterns else (0,)

    # Misleading entropy calculation (not used in final result)
    entropy = 0
    total_freq = sum(segment_patterns.values())
    for freq in segment_patterns.values():
        prob = freq / total_freq
        if prob > 0:
            entropy -= prob * __import__('math').log2(prob)

    # Construct temperature profile with artificial offsets
    temperature_profile = []
    base_offset = 2.1
    for k, val in enumerate(normalized_history):
        adjusted_val = val * (k % 3 + 1) + base_offset
        temperature_profile.append(adjusted_val)
        adjustment_log[f'step_{k}'] = adjusted_val

    # Red herring: character counting in log keys
    char_count = sum(len(key) for key in adjustment_log.keys())
    dummy_score = char_count * 0.01

    # Reference index determined by pattern length
    reference_index = len(dominant_pattern) % len(temperature_profile) if temperature_profile else 0

    # Correction system based on initial thresholds
    high_threshold = thresholds['high']
    low_threshold = thresholds['low']
    spread = high_threshold - low_threshold
    correction_factor = 1.75 if spread > 10 else 0.85

    # Unused intermediate diagnostics
    stability_metric = sum(1 for x, y in zip(temp_history, temp_history[1:]) if abs(x - y) < 0.1)
    fluctuation_rate = stability_metric / len(temp_history) if temp_history else 0

    # Final computation (depends only on temperature_profile, reference_index, correction_factor, and fixed offset)
    offset = -4.2
    final_diagnostic = temperature_profile[reference_index] * correction_factor + offset

    print(f"Result: {final_diagnostic}")

# Execute scenario
sensor_input = [12.1, 8.3, 6.5, 15.2, 9.8, 7.4, 13.0, 11.7]
config = {'high': 10.0, 'low': 7.5}
analyze_thermal_readings(sensor_input, config)