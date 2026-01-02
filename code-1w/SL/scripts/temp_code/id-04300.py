def analyze_pattern(seq):
    count_a = sum(1 for c in seq if c == 'A')
    count_t = sum(1 for c in seq if c == 'T')
    ratio = count_a / (count_t + 1e-5)
    return ratio * len(seq)

# Irrelevant DNA pattern analysis (distractor)
dna_seq = 'ATGCTAGCTAACCTA'
pattern_value = analyze_pattern(dna_seq)

# Real task: Signal processing with weighted segment evaluation
def extract_features(data_stream):
    features = []
    for i, val in enumerate(data_stream):
        if i % 3 == 0:
            features.append(val ** 2)
        elif val > 0:
            features.append(abs(val) ** 0.5)
        else:
            features.append(val)
    return features

def compute_checksum(arr):
    # Unused decoy function
    checksum = 0
    for x in arr:
        checksum = (checksum + x) % 97
    return checksum

def validate_sequence(seq):
    # Dead code path - never called
    return all(x >= 0 for x in seq)

# Simulate sensor data segments
segment_data = [
    [1, -2, 3, 4],
    [0, 5, -1, 2],
    [3, 3, -4, 6],
    [-1, 0, 2, 1]
]

# Weight matrix – only first two weights are actually used
weights = [0.8, 1.2, 0.5, 0.1]  # Last two are red herrings

# Preprocessing step with distractors
temp_buffers = []
for seg in segment_data:
    processed = extract_features(seg)
    temp_buffers.append([x * 1.1 for x in processed])  # Slight modification

# Misleading accumulation (not part of final logic)
total_buffer_sum = sum(sum(buf) for buf in temp_buffers)

# Core logic hidden among distractions
def process_segments(segments, w):
    results = []
    for idx, s in enumerate(segments):
        # Only use first two weights cyclically
        weight = w[idx % 2]
        total = 0
        for j, val in enumerate(s):
            if j % 2 == 0:
                total += val * weight
            else:
                total -= val * 0.1
        # Apply non-linear transformation only on even indices
        adjusted = total * (1.1 if idx % 2 == 0 else 1.0)
        results.append(adjusted)
    
    # Accumulate only specific contributions
    cumulative = 0
    for i, r in enumerate(results):
        if i != 2:  # Skip third segment (trap)
            cumulative += r * (i + 1)  # Weight by position index
    return int(cumulative + 0.5)  # Round to nearest integer

# Secondary irrelevant computation (bit manipulation red herring)
def obfuscate_key(n):
    n ^= 0xFF
    n = (n << 2) & 0xFF
    n |= (n >> 4)
    return n

key = 42
obfuscated = obfuscate_key(key)

# Main execution
final_score = process_segments(segment_data, weights)

# Output result as required
print(f"Result: {final_score}")