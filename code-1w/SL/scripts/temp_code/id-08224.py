def preprocess_signal(raw_data):
    filtered = [x for x in raw_data if x > -50 and x < 50]
    normalized = [round(x / max(filtered), 6) for x in filtered]
    return normalized


def encode_segment(segment, key=7):
    encoded = 0
    for i, val in enumerate(segment):
        shifted = int((val * 100) + i) ^ key
        encoded += shifted << (i % 4)
    return encoded


def analyze_pattern(seq):
    count = 0
    for item in seq:
        if item & 1:
            count += 1
    return count > len(seq) // 2

# Irrelevant helper - dead path
def deprecated_checksum(data):
    return sum(data) % 256

# Unused transformation
def mirror_sequence(arr):
    return arr + arr[::-1]

# Decoy function with misleading name
def compute_entropy(values):
    import math
    total = 0.0
    for v in values:
        if v > 0:
            total -= v * math.log(v)
    return total  # Never used

# Main pipeline
raw_sensor_data = [42, -30, 88, 12, 5, -60, 23, 9, 100, -5, 7]

# Step 1: Filter and normalize
processed = preprocess_signal(raw_sensor_data)

# Step 2: Create segments
segments = [processed[i:i+3] for i in range(0, len(processed), 3)]

# Distractor: unused mirrored version
mirrored_segments = [mirror_sequence(s) for s in segments]

# Step 3: Encode each segment
encoded_segments = []
for seg in segments:
    if len(seg) >= 2:
        code = encode_segment(seg, key=13)
        encoded_segments.append(code)

# Irrelevant statistical red herring
mean_code = sum(encoded_segments) / len(encoded_segments) if encoded_segments else 0
std_deviation = (sum((x - mean_code) ** 2 for x in encoded_segments) / len(encoded_segments)) ** 0.5 if encoded_segments else 0

# Flags based on pattern analysis (only some are used)
flags = []
for code in encoded_segments:
    bit_pattern = [int(b) for b in bin(code)[2:]]
    is_odd_weighted = analyze_pattern(bit_pattern)
    has_high_bit = code & (1 << 10)
    # Only 'is_odd_weighted' is actually used later
    flags.append({'type_a': is_odd_weighted, 'flag_b': has_high_bit})

# Fake entropy distraction
entropy_values = [compute_entropy(s) for s in segments]

# Aggregation logic
sum_contributions = 0
weight_tracker = 0

for i, enc in enumerate(encoded_segments):
    # Extract only bits that were set at even positions during encoding
    contribution = 0
    temp = enc
    pos = 0
    while temp:
        if pos % 2 == 0:
            contribution += temp & 1
        temp >>= 1
        pos += 1
    
    # Weighting by index and flag state
    if flags[i]['type_a']:
        sum_contributions += contribution * (i + 1)
    weight_tracker += i + 1

# Spurious alternate aggregation (never used)
collision_test = sum(encoded_segments) ^ sum(encoded_segments[::-1])

# Critical statement
final_diagnostic = aggregate_metrics(encoded_segments, flags)

# Actual implementation of required function
def aggregate_metrics(codes, metadata):
    result = 0
    for idx, code in enumerate(codes):
        # Recover original segment length effect
        shift_back = (code >> (idx % 3)) & 15
        flag_influence = 2 if metadata[idx]['type_a'] else 1
        result += shift_back * flag_influence
    # Add constant from valid logic chain
    result += len([m for m in metadata if m['type_a']])
    return result

# Print final answer
Target result: {final_diagnostic}