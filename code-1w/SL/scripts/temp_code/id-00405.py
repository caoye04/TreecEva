def preprocess_signal(raw):
    filtered = []
    noise_floor = 0.1
    for x in raw:
        if abs(x) > noise_floor:
            filtered.append(x * 1.2)
    return filtered

raw_measurements = [0.05, 0.3, -0.2, 0.0, 0.7, -0.6, 0.15, 0.08]
baseline_shift = 0.05
adjusted = [x + baseline_shift for x in raw_measurements]
dummy_counter = 0
for val in adjusted:
    if val > 0.1:
        dummy_counter += 1

processed_data = preprocess_signal(adjusted)

# Irrelevant transformation chain
temp_encoded = []
encoding_map = {i: chr(65 + (i % 26)) for i in range(10)}
for i, x in enumerate(processed_data):
    if i % 2 == 0:
        temp_encoded.append(encoding_map.get(int(abs(x)*10), 'X'))

# Dummy string analysis (distraction)
encoded_str = ''.join(temp_encoded)
char_freq = {}
for c in encoded_str:
    char_freq[c] = char_freq.get(c, 0) + 1
repeated_chars = [c for c, cnt in char_freq.items() if cnt > 1]

# Red herring calculation with zip
sync_pattern = [1, 0, 1, 0, 1]
overlap_score = 0
for a, b in zip(sync_pattern, sync_pattern[1:]):
    overlap_score += a ^ b  # XOR to create distraction

# Actual diagnostic logic buried in noise
def analyze_readings(readings, limits):
    count_within = 0
    rolling_peak = 0
    total_energy = 0
    
    # Real computation path
    for i, val in enumerate(readings):
        total_energy += val ** 2
        if limits[0] <= val <= limits[1]:
            count_within += 1
        if abs(val) > rolling_peak:
            rolling_peak = abs(val)
    
    # Secondary red herring: unused branching
    if len(readings) > 10:
        fallback_mode = True
        return -999  # Dead code path

    stability_index = count_within / len(readings) if readings else 0
    energy_normalized = total_energy / len(readings)
    
    # Final decision logic
    if energy_normalized > 0.3 and stability_index > 0.6:
        return int(rolling_peak * 100)
    else:
        return int((energy_normalized + stability_index) * 50)

# Unused helper function (dead code)
def compress_data(seq):
    result = []
    for x in seq:
        if x > 0:
            result.append(round(x**0.5, 3))
    return result

thresholds = (0.12, 0.8)

# Misleading intermediate array
aggregated_stats = []
for i, val in enumerate(processed_data):
    stat = {
        'index': i,
        'value': val,
        'squared': val**2,
        'offset_key': (i * val) % 4
    }
    aggregated_stats.append(stat)

# Another distraction: set operations on indices
valid_indices = set()
for entry in aggregated_stats:
    if entry['squared'] > 0.1:
        valid_indices.add(entry['index'])

ref_set = {0, 2, 4}
intersection_size = len(valid_indices & ref_set)

final_diagnostic = analyze_readings(processed_data, thresholds)
print(f"Result: {final_diagnostic}")