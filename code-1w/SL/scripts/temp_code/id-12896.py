def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if x > 0.5]
    normalized = [x / max(filtered) for x in filtered]
    return normalized


def compute_checksum(sequence):
    checksum = 0
    for i, val in enumerate(sequence):
        checksum ^= int(val * 100) + i
    return checksum


def generate_sequence(seed, length):
    seq = [seed]
    for _ in range(1, length):
        next_val = (seq[-1] * 1103515245 + 12345) % (2**31)
        seq.append(next_val)
    return seq


def extract_features(data_slice):
    peak = max(data_slice)
    avg = sum(data_slice) / len(data_slice)
    variance = sum((x - avg) ** 2 for x in data_slice) / len(data_slice)
    return peak, avg, variance


def rolling_window(values, window_size):
    return [values[i:i+window_size] for i in range(len(values)-window_size+1)]


def transform_signal(signal):
    doubled = [x * 2 for x in signal]
    shifted = [x >> 1 for x in doubled if x > 1]
    return shifted


def analyze_pattern(dataset, offset):
    segment_a = dataset[:len(dataset)//2]
    segment_b = dataset[len(dataset)//2:]
    
    temp_result = 0
    for i in range(min(len(segment_a), len(segment_b))):
        temp_result += (segment_a[i] - segment_b[i]) ** 2
    
    if temp_result < 100:
        category_flag = 1
    else:
        category_flag = -1
    
    aggregated = 0
    for val in dataset[offset:]:
        if val % 2 == 0:
            aggregated += val // 2
        else:
            aggregated -= val // 3
    
    return int(aggregated * category_flag)

# Irrelevant setup variables (distractors)
baseline_threshold = 0.75
reference_id = 4217
payload_mask = 0xFF00AA

# Simulated sensor readings (irrelevant to final result but looks important)
raw_sensor_data = [0.61, 0.72, 0.48, 0.83, 0.91, 0.55, 0.67]
processed_signal = preprocess_signal(raw_sensor_data)

# Unused feature extraction (dead path)
peaks, means, variances = extract_features(processed_signal)

# Generate cryptographically weak sequence (looks significant, unused)
pseudo_random_seq = generate_sequence(seed=7, length=20)
checksum_value = compute_checksum(pseudo_random_seq)  # Distractor

# Core data pipeline
primary_stream = [12, 8, 15, 3, 10, 7, 14, 6]
sliced_window = rolling_window(primary_stream, 3)  # Not used later
transformed_data = transform_signal(primary_stream)  # Key transformation

# Secondary irrelevant processing
secondary_buffer = [x ^ 0b1010 for x in primary_stream if x < 10]
shadow_copy = secondary_buffer[:]  # Dead code

# Offset calculation with red herring logic
base_offset = len(primary_stream) % 7  # Used in final call
lookup_table = {i: (i**2 + 3*i + 1) % 19 for i in range(15)}  # Unused

# Misleading intermediate analysis
aggregate_score = 0
for chunk in sliced_window:
    aggregate_score += sum(chunk) * chunk[0]  # Looks important, not used

# Final execution point
final_diagnostic = analyze_pattern(transformed_data, base_offset)
print(f"Result: {final_diagnostic}")