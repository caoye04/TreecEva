from collections import defaultdict, Counter

# Simulated sensor data processing with red herrings
def process_sensor_array(raw_readings):
    filtered_data = [x for x in raw_readings if 10 < x < 90]
    offset_map = defaultdict(lambda: 0)
    for i, val in enumerate(filtered_data):
        if i % 3 == 0:
            offset_map['A'] += val // 7
        elif i % 3 == 1:
            offset_map['B'] -= val % 5
        else:
            offset_map['C'] += (val * 2) % 6

    # Irrelevant transformation chain (dead logic path)
    temp_result = list(map(lambda x: (x ** 0.5) * 2, filtered_data))
    normalized = [round(x, 2) for x in temp_result]
    stats_summary = {'mean': sum(normalized) / len(normalized), 'count': len(normalized)}

    # Core logic disguised among distractions
    mode_hint = max(Counter(filtered_data).values())
    base_energy = sum(filtered_data) // len(filtered_data)
    
    # Misleading intermediate (looks important but unused)
    decoy_aggregate = sum([a ^ b for a, b in zip(filtered_data, reversed(filtered_data))]) // 10

    # Actual relevant transformation
    shift_key = sum(offset_map.values()) % 8
    adjustment_sequence = [i * shift_key for i in range(1, 6)]
    
    # Hidden dependency via lambda
    transform_fn = lambda x: x + adjustment_sequence[2] - mode_hint
    aggregate_score = transform_fn(base_energy)

    # Decoy structures and calculations
    metadata_index = {}
    for idx, val in enumerate(['alpha', 'beta', 'gamma', 'delta', 'epsilon']):
        metadata_index[val] = idx * 100 + shift_key
    
    # Character counting red herring
    label_pool = "diagnostic_frame_x12"
    char_freq = Counter(label_pool)
    vowel_count = sum(char_freq[c] for c in 'aeiou' if c in char_freq)

    # Case conversion distraction
    upper_labels = list(map(str.upper, metadata_index.keys()))
    hash_offset = sum(ord(c) for c in upper_labels[0]) % 13

    # Real correction factor derived from multiple subtle sources
    valid_pairs = [(a, b) for a, b in zip(filtered_data, filtered_data[1:]) if a < b]
    rise_count = len(valid_pairs)
    correction_factor = (rise_count * hash_offset) - vowel_count

    # Critical statement: final result assembly
    final_diagnostic = aggregate_score + correction_factor

    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Input data with non-uniform distribution
sensor_input = [12, 45, 67, 88, 23, 54, 15, 76, 33, 55, 82, 11, 41]

# Unused function to add confusion
def diagnostic_override(data):
    return sum(data[i] for i in range(0, len(data), 3)) // 7

# Unused variable cluster
buffer_state = [0] * 5
sync_flag = False
payload_checksum = 0

# Execute main logic
result = process_sensor_array(sensor_input)