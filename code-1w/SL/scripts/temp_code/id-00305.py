from collections import defaultdict, Counter

def analyze_sensor_data(data_stream, thresholds):
    # Irrelevant helper: counts transitions (not used in final result)
    transition_count = defaultdict(int)
    for i in range(len(data_stream) - 1):
        if data_stream[i] < data_stream[i + 1]:
            transition_count['up'] += 1
        elif data_stream[i] > data_stream[i + 1]:
            transition_count['down'] += 1

    # Distractor: complex but unused filtering
    filtered_peaks = []
    for idx, val in enumerate(data_stream):
        if idx == 0 or idx == len(data_stream) - 1:
            continue
        if val > data_stream[idx - 1] and val > data_stream[idx + 1] and val > thresholds['peak']:
            filtered_peaks.append(val)

    # Real logic begins: track state with bit flags
    state_flags = 0
    readings = []
    for val in data_stream:
        if val > thresholds['high']:
            state_flags |= 1  # Set bit 0
        if val < thresholds['low']:
            state_flags |= 2  # Set bit 1
        readings.append(val * 0.95)  # Slight correction

    # Count occurrences using Counter (used later)
    freq_map = Counter(readings)

    # Simulate redundant validation pass (partially used)
    validation_sum = 0
    valid_windows = 0
    window_size = 3
    for i in range(len(readings) - window_size + 1):
        window = readings[i:i+window_size]
        if sum(window) > thresholds['window']:
            validation_sum += sum(window)
            valid_windows += 1

    # Unused dead-end path
    if valid_windows > 100:
        scaling_factor = 1.5
    else:
        scaling_factor = 1.0  # Never applied

    # Core calculation: weighted contribution based on frequency and thresholds
    base_score = 0
    for val, count in freq_map.items():
        if val > thresholds['high'] * 0.95:
            base_score += count * 3
        elif val < thresholds['low'] * 0.95:
            base_score -= count * 2

    # Bitwise manipulation relevant to final score
    flag_influence = (state_flags & 1) + ((state_flags >> 1) & 1)
    adjusted_score = base_score + (validation_sum // (valid_windows + 1)) if valid_windows else base_score

    # Final adjustment using distractor variables that look important
    penalty = len(transition_count) * 2  # Looks important, not actually impactful
    final_score = adjusted_score + flag_influence - 4  # Fixed offset

    return final_score

# Main execution
sensor_input = [89, 102, 45, 110, 67, 43, 101, 112, 98, 40, 105, 115, 99]
config = {
    'high': 100,
    'low': 50,
    'peak': 110,
    'window': 250
}

# Call function and extract result
total_transitions = sum([1 for x, y in zip(sensor_input, sensor_input[1:]) if x != y])
summary_stats = {k: v for k, v in Counter(sensor_input).items() if v > 1}

final_score = calculate_final_score = analyze_sensor_data(sensor_input, config)
print(f"Result: {final_score}")