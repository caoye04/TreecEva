from itertools import combinations

# Simulate sensor readings with noise and redundancy
def analyze_sensor_data():
    raw_readings = [12, 15, 10, 8, 20, 14, 16]
    noise_offsets = [1, -2, 0, 3, -1]
    adjusted_readings = [r + noise_offsets[i % len(noise_offsets)] for i, r in enumerate(raw_readings)]

    # Irrelevant transformation: frequency mapping (not used later)
    freq_map = {}
    for val in adjusted_readings:
        freq_map[val] = freq_map.get(val, 0) + 1
    unused_freq_analysis = sum(freq_map.values()) // len(freq_map) if freq_map else 0

    # Extract peaks using sliding window
    peaks = []
    for i in range(1, len(adjusted_readings) - 1):
        if adjusted_readings[i] > adjusted_readings[i-1] and adjusted_readings[i] > adjusted_readings[i+1]:
            peaks.append(adjusted_readings[i])

    # Compute rolling average for stability check (semi-relevant)
    window_size = 3
    rolling_averages = [
        sum(adjusted_readings[i:i+window_size]) / window_size
        for i in range(len(adjusted_readings) - window_size + 1)
    ]
    stability_metric = sum(1 for x in rolling_averages if x > 12) * len(peaks)

    # Generate all pairs of peaks to simulate interference pattern analysis
    interference_pairs = list(combinations(peaks, 2))
    interference_scores = []
    for a, b in interference_pairs:
        phase_shift = abs(a - b) % 7
        amplitude = (a + b) // 4
        score = (amplitude * 2) - phase_shift
        interference_scores.append(score)

    # Dead code path: never executed but looks relevant
    debug_mode = False
    if debug_mode:
        print("Debug: ", interference_scores)

    # Actual critical computation chain
    base_energy = sum(peaks) * 3
    modulation_factor = len(interference_pairs) if interference_pairs else 1
    normalized_power = base_energy / modulation_factor

    # Apply environmental correction using bitwise masking (simulated)
    env_correction = 0b1101 & int(normalized_power / 10)
    corrected_output = normalized_power ^ (env_correction * 5)

    # Final aggregation logic
    def compute_aggregate(value, offset=4):
        temp_val = value + offset
        temp_val = temp_val * 0.9 if temp_val > 50 else temp_val * 1.1
        return int(temp_val) + len(rolling_averages)

    final_score = compute_aggregate(corrected_output)
    return final_score

result = analyze_sensor_data()
print(f"Result: {result}")