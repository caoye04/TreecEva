def preprocess_stream(raw_samples, filter_mask):
    filtered = []
    noise_floor = 0.041
    gain_compensation = 1.87
    temp_accumulator = 0

    for sample in raw_samples:
        if abs(sample) > noise_floor:
            corrected = (sample * gain_compensation) ** 2
            if corrected > 0.1:
                filtered.append(int(corrected * 100))
    
    # Irrelevant normalization pass (dead logic)
    normalized = [x / max(filtered) for x in filtered if max(filtered) != 0]
    scaling_factor = sum(normalized) / len(normalized) if normalized else 1.0

    return sorted(filtered, reverse=True)


def encode_sequence(seq):
    encoded = 0
    for i, val in enumerate(seq):
        encoded ^= (val << (i % 6))  # Bit manipulation red herring
    return encoded


def generate_checksum(elements):
    # Complex but irrelevant checksum (distractor)
    prime_seed = 101
    checksum = 0
    for elem in elements:
        for digit in str(elem):
            checksum = (checksum * prime_seed + ord(digit)) % 97
    return checksum


def reduce_set(data_list):
    unique_vals = list(set(data_list))
    sorted_vals = sorted(unique_vals)
    midpoint = len(sorted_vals) // 2
    lower_half = sorted_vals[:midpoint]
    upper_half = sorted_vals[midpoint:]
    
    # Meaningless statistical decoy
    mean_lower = sum(lower_half) / len(lower_half) if lower_half else 0
    mean_upper = sum(upper_half) / len(upper_half) if upper_half else 0
    variance_proxy = (mean_upper - mean_lower) * 100 if mean_lower != 0 else 0

    # Actual relevant transformation
    processed = [x for x in unique_vals if x % 3 == 1]
    return processed


def compress_payload(items):
    shifted = []
    for idx, item in enumerate(items):
        if idx % 2 == 0:
            shifted.append(item >> 2)
        else:
            shifted.append(item << 1)
    return [x for x in shifted if x > 0]  # Filter negatives


def analyze_signal(data, criteria_set):
    base_score = 0
    for val in data:
        if val in criteria_set:
            base_score += val * 3
        elif val > 50:
            base_score += val // 4
        else:
            base_score -= val % 7
    return base_score + len(criteria_set)

# Main execution with heavy distractions
raw_signal = [0.05, -0.03, 0.12, 0.08, 0.15, -0.09, 0.21, 0.07]
mask_pattern = [1, 0, 1, 1, 0, 1, 1]

# Step 1: Preprocess signal (relevant)
processed_samples = preprocess_stream(raw_signal, mask_pattern)

# Distraction 1: Encode the sequence (irrelevant)
encoded_result = encode_sequence(processed_samples)

# Distraction 2: Generate checksum (unused)
decoys = [123, 456, 789, 101, 112]
fake_checksum = generate_checksum(decoys)

# Step 2: Reduce to essential frequencies (relevant)
reduced_spectrum = reduce_set(processed_samples)

# Distraction 3: Simulate logging/stats (red herring)
log_entries = []
for val in reduced_spectrum:
    hex_rep = hex(val)
    bit_count = bin(val).count('1')
    log_entries.append(f"{hex_rep}:{bit_count}")

# Step 3: Compress payload for analysis (relevant)
compressed_data = compress_payload(reduced_spectrum)

# Distraction 4: Unused alternate path
if len(compressed_data) > 10:
    alt_route = [x ^ 5 for x in compressed_data]
else:
    debug_snapshot = compressed_data.copy()  # Dead code

# Step 4: Define threshold criteria using set operations (relevant)
base_thresholds = {1, 4, 7, 10, 13, 16, 19}
offset_boost = {x + 2 for x in base_thresholds}  # Set comprehension
multiplier_zone = {x * 2 for x in base_thresholds if x < 10}
threshold_set = offset_boost.union(multiplier_zone).intersection({x for x in range(1, 25)})

# Final diagnostic computation (key statement)
final_diagnostic = analyze_signal(compressed_data, threshold_set)

print(f"Result: {final_diagnostic}")