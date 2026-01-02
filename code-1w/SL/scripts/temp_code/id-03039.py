def preprocess_signal(raw_data):
    filtered = [x for x in raw_data if x > 0]
    normalized = [x / max(filtered) for x in filtered]
    return [int(x * 100) for x in normalized]


def encrypt_sequence(seq, key):
    return [(x ^ key) % 256 for x in seq]


def analyze_pattern(seq, limit):
    window_size = 4
    slices = [seq[i:i+window_size] for i in range(0, len(seq)-window_size+1)]
    
    # Irrelevant transformation (distractor)
    reversed_slices = [s[::-1] for s in slices]
    mean_vals = [sum(s) / len(s) for s in slices]
    
    # Decoy analysis path (dead code)
    anomaly_score = 0
    for val in mean_vals:
        if val > 150:
            anomaly_score += 1
    
    # Real computation path
    valid_windows = [w for w in slices if sum(w) < limit]
    pattern_entropy = 0
    for win in valid_windows:
        xor_chain = 0
        for val in win:
            xor_chain ^= val
        pattern_entropy += xor_chain
    
    # Misleading intermediate
    fake_diagnostic = len(reversed_slices) * 17
    
    # Actual result
    base_diagnostic = pattern_entropy * len(valid_windows)
    
    # Red herring: unused conditional branch
    if len(str(pattern_entropy)) > 3:
        base_diagnostic -= 999  # never reached due to data range
    
    return base_diagnostic

# Main execution
raw_input_data = [12, 45, 23, 67, 34, 89, 11, 76, 55, 29]
downscaled = preprocess_signal(raw_input_data)

# Bit manipulation decoy (irrelevant)
temporary_key = 0
for val in downscaled:
    temporary_key ^= (val & 25) | (val << 1)
    temporary_key %= 100

encrypted_sequence = encrypt_sequence(downscaled, key=13)

# Spurious sorting operation (no effect on logic)
sorted_for_clarity = sorted(encrypted_sequence, reverse=True)

threshold = 120

# Unused alternative threshold logic (distractor)
if sum(encrypted_sequence) % 2 == 0:
    alt_limit = threshold + 10
else:
    alt_limit = threshold - 5

final_diagnostic = analyze_pattern(encrypted_sequence, threshold)
print(f"Result: {final_diagnostic}")