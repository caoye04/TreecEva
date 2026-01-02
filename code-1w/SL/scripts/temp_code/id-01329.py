def analyze_sensor_data(raw_readings, threshold=50):
    # Simulate preprocessing steps with distractions
    processed = [x * 1.05 for x in raw_readings if x > 0]
    offset = len(processed) % 7
    adjusted = [x + offset for x in processed]

    # Irrelevant transformation: frequency analysis (dead logic)
    freq_map = {}
    for val in adjusted:
        rounded = int(val // 10)
        freq_map[rounded] = freq_map.get(rounded, 0) + 1
    dominant_band = max(freq_map, key=lambda k: freq_map[k]) if freq_map else 0

    # Decoy filtering based on arbitrary criteria
    decoy_filtered = [x for x in adjusted if x % 3 == 1]
    decoy_sum = sum(decoy_filtered) // (len(decoy_filtered) or 1)

    # Actual relevant data path begins here
    candidate_entries = [x for x in raw_readings if x != 0]
    normalized = [x / 2.0 for x in candidate_entries]

    # Conditional filtering using multiple concepts
    outliers = [x for x in normalized if abs(x - sum(normalized)/len(normalized)) > 15]
    valid_entries = []
    for i, val in enumerate(normalized):
        if val in outliers:
            continue
        if i % 2 == 0:
            val = val * 0.9
        else:
            val = val * 1.1
        # Apply threshold condition (key logic)
        if val >= threshold * 0.5:
            valid_entries.append(int(val))

    # Key assignment point
    filtered_sum = sum(valid_entries)

    # More distractions below
    checksum = 0
    for i, (a, b) in enumerate(zip(normalized, processed)):
        checksum += (i + 1) * (int(a) ^ int(b))
    checksum %= 1000

    # Unused recursive helper (red herring)
    def calculate_depth(n):
        return 1 + calculate_depth(n // 2) if n > 1 else 1
    
    depth = calculate_depth(len(raw_readings)) if raw_readings else 0

    # Print final target result
    print(f"Result: {filtered_sum}")
    return filtered_sum

# Main execution
sensor_input = [45, 60, -5, 0, 80, 30, 70, 25, 90, 40]
data_score = analyze_sensor_data(sensor_input, threshold=55)
