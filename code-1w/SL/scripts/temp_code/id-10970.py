def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if abs(x) > 0.1]
    normalized = [round(x / max(filtered), 3) for x in filtered]
    reversed_signal = normalized[::-1]
    return reversed_signal

# Irrelevant helper (distractor)
def compute_entropy(data):
    from math import log
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    total = len(data)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p, 2)
    return round(entropy, 3)

# Unused transformation path (dead code)
def legacy_transform(seq):
    shifted = [seq[i] - seq[i-1] for i in range(1, len(seq))]
    padded = [0] + shifted
    return padded

# Core processing chain
def encode_features(signal):
    amplified = [int(x * 100) for x in signal]
    binary_flags = [1 if x & 1 else 0 for x in amplified]  # LSB check
    return amplified, binary_flags

def generate_checksum(values):
    checksum = 0
    for i, v in enumerate(values):
        checksum ^= (v + i)  # Bitwise mix
    return checksum % 97

# Recursive reduction (key concept)
def reduce_sequence(seq):
    if len(seq) <= 1:
        return seq[0] if seq else 0
    mid = len(seq) // 2
    left = reduce_sequence(seq[:mid])
    right = reduce_sequence(seq[mid:])
    return (left * 3 + right * 2) % 500

# Data transformation pipeline
def transform_input(entries):
    logs = [abs(hash(str(e))) % 1000 for e in entries]  # Simulate hashing
    logs_sliced = logs[1::2]  # Take every second element (slicing)
    sorted_logs = sorted(logs_sliced, reverse=True)
    trimmed = sorted_logs[:len(sorted_logs)//2]  # Keep top half
    return trimmed

# Main analysis function
def analyze_pattern(dataset):
    temp_state = []
    for val in dataset:
        temp_state.append((val ** 2) - (val // 4))
    
    # Introduce irrelevant branching (red herring)
    if sum(temp_state) < 10000:
        shadow_copy = [x * 0.95 for x in temp_state]
        # This branch is not used in final result
    else:
        pass  # Deliberately misleading path

    # Real computation begins
    processed = [x for x in temp_state if x % 2 == 1]  # odd values only
    if not processed:
        return 0
    
    # Apply recursive reduction
    key_value = reduce_sequence(processed)
    
    # Side computation (decoy)
    outlier_count = 0
    for x in temp_state:
        if x > 200 or x < 0:
            outlier_count += 1
    # Not used later
    
    # Final diagnostic depends only on key_value and length
    final_diagnostic = key_value * len(dataset)
    return final_diagnostic

# --- Entry point ---
data_stream = [0.5, -0.3, 0.8, 1.2, -0.9, 0.4, 1.1, -0.7]

# Begin execution chain
filtered_signal = preprocess_signal(data_stream)
amplified_data, flags = encode_features(filtered_signal)
checksum = generate_checksum(amplified_data)  # Computed but unused
transformed_data = transform_input(amplified_data)  # Critical input

# Dead function call (distractor)
entropy_metric = compute_entropy(flags)

# Key statement
final_diagnostic = analyze_pattern(transformed_data)

print(f"Result: {final_diagnostic}")