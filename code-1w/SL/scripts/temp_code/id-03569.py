def preprocess_signal(raw_data):
    filtered = [x for x in raw_data if abs(x) > 0.1]
    normalized = [x / max(filtered) for x in filtered]
    return normalized


def encode_features(data_stream):
    encoded = []
    for i, val in enumerate(data_stream):
        if i % 2 == 0:
            encoded.append(int(val * 100) ^ 255)
        else:
            encoded.append(int(val * 50) | 128)
    return encoded


def compute_entropy(sequence):
    from collections import Counter
    counts = Counter(sequence)
    total = len(sequence)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Simulated pseudo-entropy
    return round(entropy, 6)


def generate_checksum(segments):
    checksum = 0
    for seg in segments:
        for val in seg:
            checksum = (checksum ^ val) << 1
            if checksum > 255:
                checksum = checksum & 255
    return checksum


def analyze_pattern(seq):
    transitions = 0
    for i in range(1, len(seq)):
        if (seq[i-1] < 0) != (seq[i] < 0):
            transitions += 1
    return transitions

# Irrelevant auxiliary functions (red herrings)
def unused_helper_1(x): return x ** 2 + 1
def unused_helper_2(lst): return sorted(lst, reverse=True)

def decoy_aggregation(arr):
    temp = 0
    for i in range(len(arr)):
        temp += arr[i] * (i + 1)
    return temp  # Never used

# Main processing chain
raw_input = [0.12, -0.45, 0.67, 0.0, 0.23, -0.11, 0.89, -0.76, 0.03, 0.54]

# Step 1: Filter and normalize
processed_signal = preprocess_signal(raw_input)

# Step 2: Encode features with bitwise ops
encoded_features = encode_features(processed_signal)

# Step 3: Segment into chunks
segment_size = 3
encoded_segments = [encoded_features[i:i+segment_size] for i in range(0, len(encoded_features), segment_size)]

# Misleading intermediate calculations
shadow_copy = [row[:] for row in encoded_segments]
for idx, segment in enumerate(shadow_copy):
    if idx % 2 == 0:
        segment.append(sum(segment) // len(segment))

# Step 4: Compute auxiliary metrics (some irrelevant)
entropies = [compute_entropy(seg) for seg in encoded_segments]
transitions = [analyze_pattern(seg) for seg in encoded_segments]
weights = [len(seg) * entropies[i] for i, seg in enumerate(encoded_segments)]

# Dead code path - never executed due to condition
if len(encoded_segments) < 2:
    weights = [w * 1.5 for w in weights]

# Another red herring: decoy structure
metrics_log = {
    'timestamp': '2024-05-20',
    'version': 'v2.3',
    'unused_score': decoy_aggregation([item for sublist in encoded_segments for item in sublist])
}

# Core logic hidden among distractions
baseline_shift = sum([sum(seg) for seg in encoded_segments]) % 17

# Key transformation
adjusted_weights = [abs(w - baseline_shift) + 1e-6 for w in weights]

# Critical statement
final_diagnostic = aggregate_metrics(encoded_segments, adjusted_weights)

# Actual definition buried late (misdirection)
def aggregate_metrics(segs, wts):
    total = 0.0
    for i, seg in enumerate(segs):
        segment_value = 0
        for val in seg:
            segment_value += val * wts[i]
        total += segment_value * (0.9 ** i)  # Exponential decay factor
    return int(total)  # Deterministic integer output

# Print final result
print(f"Result: {final_diagnostic}")