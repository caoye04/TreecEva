import itertools

# Simulated sensor fusion system for environmental monitoring
# Some sensors are faulty, others require calibration

def analyze_readings(temperature_stream, pressure_stream, humidity_stream):
    sample_count = len(temperature_stream)
    valid_samples = 0
    cumulative_index = 0
    calibration_offset = 0.87
    drift_compensation = []

    # Irrelevant pre-processing: character frequency analysis in dummy labels (distractor)
    label_metadata = "T1_P2_H3 T4_P5_H6 T7_P8_H9"
    char_freq = {}
    for char in label_metadata:
        if char.isalpha():
            char_freq[char] = char_freq.get(char, 0) + 1
    alpha_sum = sum([v for k, v in char_freq.items() if k in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'])

    # Misleading intermediate: entropy-like calculation (dead end)
    entropy_proxy = 0.0
    for i in range(1, min(5, sample_count)):
        diff = abs(temperature_stream[i] - temperature_stream[i-1])
        entropy_proxy += diff * 0.3 if diff > 2 else 0

    # Real logic begins: detect valid synchronized windows
    sync_flags = []
    for t, p, h in zip(temperature_stream, pressure_stream, humidity_stream):
        t_valid = 15 <= t <= 45
        p_valid = 950 <= p <= 1050
        h_valid = 20 <= h <= 80
        sync_flags.append(t_valid and p_valid and h_valid)

    # Compute rolling consistency (key step)
    consistent_windows = 0
    for i in range(0, sample_count - 2):
        if all(sync_flags[i:i+3]):
            consistent_windows += 1

    # Distractor: unused complex transformation using itertools
    expanded_pairs = list(itertools.combinations([0.1, 0.3, 0.6], 2))
    weighted_combinations = []
    for a, b in expanded_pairs:
        weighted_combinations.append((a * 1.5) + (b * 0.7) - 0.1)

    # Decoy function call that does nothing to main result
    def apply_filter(data):
        return [x * 0.99 for x in data if x > 0]
    filtered_temps = apply_filter(temperature_stream)  # Not used later

    # Critical path: calculate base aggregate from consistent segments
    raw_aggregate = 0
    for i in range(sample_count):
        if sync_flags[i]:
            raw_aggregate += (temperature_stream[i] * 0.3) + (pressure_stream[i] * 0.01) + (humidity_stream[i] * 0.2)

    # Apply window-based bonus multiplier
    bonus_factor = 1 + (consistent_windows * 0.05)

    # Hidden adjustment: count how many readings have prime-adjusted indices (real distractor)
    prime_indices = [i for i in range(2, sample_count) if all(i % j != 0 for j in range(2, int(i**0.5)+1))]
    index_correction = len(prime_indices) * 0.01

    # Main computation chain
    adjusted_total = raw_aggregate * bonus_factor
    normalized_score = adjusted_total / sample_count
    stability_penalty = 0.95 if consistent_windows < 3 else 1.0

    # Final scoring with conditional expression (required Python feature)
    final_score = normalized_score * stability_penalty + (index_correction if alpha_sum > 10 else 0)

    # Red herring: string method manipulation with no impact
    log_entry = f"Processed {sample_count} samples with {consistent_windows} valid windows"
    log_words = log_entry.split()
    word_lengths = [len(w) for w in log_words]
    avg_word_len = sum(word_lengths) / len(word_lengths) if word_lengths else 0

    # Output the required result
    print(f"Result: {final_score}")
    return final_score

# Simulated input data streams
temps = [25, 30, 32, 14, 35, 33, 29, 27]
pressures = [1013, 1008, 1015, 940, 1020, 1010, 1005, 1012]
humidities = [45, 50, 52, 85, 48, 55, 53, 47]

# Entry point
result = analyze_readings(temps, pressures, humidities)