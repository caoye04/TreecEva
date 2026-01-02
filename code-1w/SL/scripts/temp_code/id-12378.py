def analyze_sensor_data(raw_data):
    # Simulate preprocessing steps with distractors
    temp_buffer = [x * 0.95 for x in raw_data if x > 0]
    offset_correction = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0

    # Irrelevant transformation: frequency analysis (dead-end)
    freq_map = {}
    for x in raw_data:
        rounded = round(x / 10)
        freq_map[rounded] = freq_map.get(rounded, 0) + 1
    dominant_freq = max(freq_map.values()) if freq_map else 0

    # Decoy filtering: applies incorrect condition
    decoy_filtered = [x for x in raw_data if x % 7 == 0]
    decoy_sum = sum(decoy_filtered) * 0.1  # red herring

    # Actual signal extraction: only values matching precise pattern
    valid_patterns = []
    for x in raw_data:
        as_str = str(abs(x))
        if len(as_str) == 3 and as_str[0] != as_str[1] and as_str[1] != as_str[2]:
            digit_sum = sum(int(d) for d in as_str)
            if digit_sum % 4 == 0:
                valid_patterns.append(x)

    # Secondary filter based on position and parity
    indexed_pairs = [(i, v) for i, v in enumerate(valid_patterns)]
    paired_shifts = []
    for i, val in indexed_pairs:
        shifted = val ^ i  # XOR index for obfuscation
        paired_shifts.append(shifted)

    # Reconstruct using slice logic and reverse engineering
    reconstructed = []
    for s in paired_shifts:
        original_index = s & 0b111  # extract lower 3 bits as fake index
        if original_index < len(valid_patterns):
            reconstructed.append(valid_patterns[original_index])

    # Distractor: string-based checksum
    checksum_str = ''.join([str(abs(v))[-1] for v in valid_patterns if v > 50])
    checksum = int(checksum_str) if checksum_str else 0
    checksum *= 0.01  # meaningless scaling

    # Core logic: find values that survived all filters
    surviving = []
    for v in reconstructed:
        if v in valid_patterns and abs(v) > 10:
            surviving.append(v)

    # Final cleansing using slicing and reversal
    sorted_surviving = sorted(surviving)
    trimmed = sorted_surviving[1:-1] if len(sorted_surviving) > 2 else sorted_surviving

    # Apply threshold filter based on dynamic midpoint
    if trimmed:
        mid_val = trimmed[len(trimmed) // 2]
        relevant_values = [v for v in trimmed if (v >= 0) != (mid_val < 0)]  # opposite sign logic
    else:
        relevant_values = []

    filtered_sum = sum(relevant_values)
    
    # Print required output
    print(f"Result: {filtered_sum}")
    return filtered_sum

# Simulated sensor input (deterministic)
data_stream = [123, -456, 789, 112, 131, 994, 202, 303, 414, 525, 636, 747, 858, 969]
result = analyze_sensor_data(data_stream)