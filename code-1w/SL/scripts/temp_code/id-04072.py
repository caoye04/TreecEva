import itertools

def analyze_pattern(sequence):
    if len(sequence) < 3:
        return False
    diffs = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
    return all(d == diffs[0] for d in diffs)

def compute_hash(data_list):
    # Irrelevant hashing function (dead-end)
    acc = 0
    for val in data_list:
        acc = (acc * 31 + val) % 10007
    return acc

def shift_sequence(seq, offset):
    # Unused transformation
    return [(x + offset) % 100 for x in seq]

def extract_features(raw_data):
    # Real feature extraction
    segments = [raw_data[i:i+4] for i in range(0, len(raw_data), 4)]
    valid_segments = []
    for seg in segments:
        if len(seg) == 4 and sum(seg) % 2 == 0:
            valid_segments.append(seg)
    return valid_segments

def evaluate_consistency(features):
    # Check arithmetic consistency in each segment
    results = []
    for f in features:
        results.append(analyze_pattern(f))
    return all(results)

def transform_chain(data_blocks):
    # Complex but partially relevant transformation
    flattened = list(itertools.chain.from_iterable(data_blocks))
    shifted = [x * 2 for x in flattened]
    filtered = [x for x in shifted if x > 50]
    # Decoy accumulation
    temp_sum = 0
    for val in filtered:
        temp_sum += val * 3  # irrelevant
    normalized = [x / max(filtered) for x in filtered]  # this matters later
    return normalized

def derive_key_metric(normalized_values):
    # Red herring metric
    return sum(x ** 2 for x in normalized_values if x > 0.5)

def process_integrity_score(flag, chain):
    base = 1000
    if flag:
        adjustment = sum(chain) * 100
        base += adjustment
    else:
        base -= 500
    # Add decoy manipulation
    noise = 0
    for i in range(len(chain)):
        if i % 2 == 0:
            noise += chain[i] * 10
    # Final result not affected by noise
    return int(base)

# --- Main Execution ---
raw_input_stream = [12, 15, 18, 21, 10, 20, 30, 40, 25, 27, 29, 31]

# Dead path: hash computation with no use
hash_result = compute_hash(raw_input_stream)
offset_data = shift_sequence(raw_input_stream, 5)

# Real processing begins
features = extract_features(raw_input_stream)
consistency_flag = evaluate_consistency(features)

# Transform the valid data chain
normalized_chain = transform_chain(features)

# Derive unused metric (misleading intermediate)
decoy_metric = derive_key_metric(normalized_chain)

# Critical statement
final_diagnostic = process_integrity_score(consistency_flag, normalized_chain)

print(f"Result: {final_diagnostic}")