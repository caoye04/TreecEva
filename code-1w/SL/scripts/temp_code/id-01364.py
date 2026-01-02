def normalize_readings(readings):
    max_val = max(readings)
    return [round(x / max_val, 6) for x in readings]


def encode_sample_id(sample_str):
    # Irrelevant encoding function (dead path)
    return sum(ord(c) * (7 ** i) for i, c in enumerate(sample_str[:4]))


def shift_window(data, window_size):
    # Unused transformation with misleading intermediate output
    shifted = []
    for i in range(len(data)):
        chunk = data[i:i+window_size]
        if len(chunk) == window_size:
            shifted.append(sum(chunk) % 100)
    temp_result = [x * 1.5 for x in shifted]  # Red herring
    return shifted


def recursive_filter(items, depth=0):
    if depth >= 3 or not items:
        return [x for x in items if x > 0]  # Base case with filtering
    return recursive_filter([x - 1 for x in items], depth + 1)

# Simulated sensor data from environmental monitoring
raw_samples = [89, 101, 42, 115, 73, 68, 94, 55]

detection_threshold = 65

# Decoy data structures
audit_log = {
    'sample_001': {'status': 'valid', 'checksum': 327},
    'sample_002': {'status': 'invalid', 'checksum': 184}
}

readings_set = set(raw_samples)
baseline_offsets = {73, 68, 55}  # Used later in meaningful way

# Apply normalization (relevant)
normalized = normalize_readings(raw_samples)

# Extract significant readings above threshold (relevant)
filtered_normalized = [v for v in normalized if v * 100 >= detection_threshold]

# Simulate data packet reconstruction (distractor)
packet_header = "HDRX"
encoded_id = encode_sample_id(packet_header)

# Perform window shifting on raw (irrelevant)
overlap_values = shift_window(raw_samples, 3)

# Core analysis pipeline
processed_data = []
for val in filtered_normalized:
    scaled = int(val * 100)
    processed_data.append(scaled)

# Add dummy corrections based on baseline (partial red herring)
correction_map = {73: 1.05, 68: 0.98, 55: 1.02}
adjusted_data = []
for d in processed_data:
    # Only apply correction if original base was in offset set
    if d in baseline_offsets:
        factor = correction_map.get(d, 1.0)
        adjusted_data.append(round(d * factor))
    else:
        adjusted_data.append(d)

# Final contamination analysis function
def analyze_contaminants(data, threshold):
    # Convert to set to remove duplicates (meaningful use of set)
    unique_levels = set(data)
    
    # Slice middle portion (slicing operation)
    sorted_vals = sorted(unique_levels)
    mid_range = sorted_vals[1:-1] if len(sorted_vals) > 2 else sorted_vals
    
    # Compute weighted impact score
    score = 0
    for i, level in enumerate(mid_range):
        if level > threshold:
            contribution = (level - threshold) * (1.5 ** i)  # Exponential weighting
            score += contribution
    
    # Dummy dictionary lookup (distractor)
    flags = {k: 'high' for k in unique_levels if k > 80}
    flag_count = len(flags)
    
    # Final adjustment using recursive result
    recursion_anchor = recursive_filter([score, flag_count * 10], 0)
    final_score = int(recursion_anchor[0]) if recursion_anchor else int(score)
    
    return final_score

# Execute critical statement
filtration_score = analyze_contaminants(processed_data, detection_threshold)

# Print result as required
print(f"Result: {filtration_score}")