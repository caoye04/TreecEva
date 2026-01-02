def analyze_pattern(sequence, depth=0):
    if depth >= 3:
        return sum(sequence) % 7
    transformed = [(x * 2 + 1) % 13 for x in sequence]
    return analyze_pattern(transformed, depth + 1)


def accumulate_diagnostic(signal):
    temp_vals = []
    for i, val in enumerate(signal):
        if i % 3 == 0:
            temp_vals.append(val ^ (i + 5))
        elif i % 4 == 1:
            temp_vals.append(val + len(signal))
        else:
            temp_vals.append(val * 2)
    return sum(temp_vals) // len(temp_vals)


def decode_segments(packets):
    segment_sum = 0
    for idx, pkt in enumerate(packets):
        for j, byte in enumerate(pkt):
            if idx % 2 == 0:
                segment_sum += byte ^ (j * 3)
            else:
                segment_sum += byte + (j << 1)
    return segment_sum


def generate_reference_keys(base_seed):
    keys = []
    for i in range(8):
        key = (base_seed ^ i) * 17
        key ^= (key << 3) & 0xFF
        key = (key >> 4) | (key << 4)  # Rotate 4 bits
        keys.append(key % 251)
    # Dead path: unused computation
    dummy_calc = [k ** 2 + 3 for k in keys if k % 2 == 1]
    return keys


def compute_integrity_value(stream, mode="basic"):
    length = len(stream)
    xor_fingerprint = 0
    sum_mod = 0
    
    for i, chunk in enumerate(stream):
        for j, val in enumerate(chunk):
            if mode == "hybrid":
                rotated = ((val ^ i) << 2) % 256
                rotated = (rotated | (rotated >> 8)) & 0xFF
                xor_fingerprint ^= rotated
                sum_mod += (val * j) % 97
            elif mode == "fast":
                xor_fingerprint ^= (val + i + j) % 256

    hybrid_factor = 1
    if mode == "hybrid":
        hybrid_factor = (length * 3 + 5) % 19

    base_score = xor_fingerprint * hybrid_factor
    adjustment = sum_mod % 101
    
    # Distractor: irrelevant transformation chain
    decoy_signal = [base_score % (i+1) for i in range(1, 10)]
    decoy_signal = [d ^ 7 for d in decoy_signal if d > 3]
    final_adjustment = len(decoy_signal) * 2
    
    return (base_score - adjustment + final_adjustment) % 99991

# Main execution block
raw_data = [
    [12, 45, 67, 23],
    [89, 10, 34, 56],
    [21, 78, 90, 11],
    [35, 67, 82, 44]
]

# Irrelevant preprocessing (red herring)
data_profile = []
for i, row in enumerate(raw_data):
    profile_entry = {
        'index': i,
        'sum': sum(row),
        'peak': max(row),
        'entropy': len([x for x in row if x % 2 == 1])
    }
    data_profile.append(profile_entry)

# Unused function call (misleading path)
diag_result = accumulate_diagnostic([13, 44, 25, 66, 77])

# Generate but do not use reference keys (dead code distractor)
ref_keys = generate_reference_keys(42)

# Critical data transformation
processed_chunks = []
for i, segment in enumerate(raw_data):
    shifted = [(x + i * 2) % 256 for x in segment]
    processed_chunks.append(shifted)

# Another red herring: pattern analysis with no downstream effect
pattern_code = analyze_pattern([len(chunk) for chunk in raw_data] + [sum(sum(r) for r in raw_data)])

# Key operation: checksum computation using hybrid mode
data_stream = processed_chunks
final_checksum = compute_integrity_value(data_stream, mode="hybrid")

# Unrelated segment decoding (no impact on final result)
segment_total = decode_segments(raw_data)

# Output the target result
print(f"Result: {final_checksum}")