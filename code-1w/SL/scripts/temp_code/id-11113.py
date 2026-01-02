import itertools

# Simulated sensor data processing with embedded logic chain
raw_samples = [127, 63, 191, 31, 223, 15, 247, 7]
threshold = 100
noise_floor = 10

def filter_outliers(data, limit):
    return [x for x in data if x > limit]

def amplify_signal(sample):
    return sample << 1

def checksum_valid(frames):
    return sum(frames) & 1 == 0

def rolling_window(seq, size=3):
    return list(zip(*[seq[i:] for i in range(size)]))

def extract_features(packets):
    features = []
    for p in packets:
        if len(p) >= 2:
            features.append((p[0] ^ p[1]) + (p[0] & 5))
    return features

def compress_data(seq):
    # Irrelevant compression function (dead path)
    return [sum(seq[i:i+2]) % 256 for i in range(0, len(seq), 2)]

def legacy_mode_adjust(val):
    # Unused function - red herring
    return val // 2 if val > 200 else val * 3

def phase_shift_correction(value):
    # Distractor: looks important but unused
    return (value >> 2) | (value << 6)

# Begin core processing
filtered_samples = filter_outliers(raw_samples, noise_floor)
amplified_samples = list(map(amplify_signal, filtered_samples))

# Introduce misleading intermediate transformations
blended_signal = []
for i, val in enumerate(amplified_samples):
    if i % 2 == 0:
        blended_signal.append(val + (i * 3))
    else:
        blended_signal.append(val - (i * 2))

# Add decoy variables that look like they're used later
baseline_offset = 42
normalization_factor = 0.987
reference_frame = [x % 128 for x in blended_signal]

# Real processing begins here — conditional frame construction
frame_candidates = []
count = 0
for s in blended_signal:
    temp_frame = []
    temp_frame.append(s)
    if s > threshold * 2:
        temp_frame.append(s // 4)
        count += 1
    if s < threshold * 3 and count % 2 == 1:
        temp_frame.append(s ^ 15)
    frame_candidates.append(temp_frame)

# Only frames with exactly two elements are valid
processed_frames = [f for f in frame_candidates if len(f) == 2]

# Extract secondary metrics (distractor)
diagnostic_trace = []
for idx, frame in enumerate(processed_frames):
    metric_a = frame[0] & 7
    metric_b = frame[1] | 3
    diagnostic_trace.append(metric_a * metric_b + idx)

# Use itertools and lambda in non-trivial way
pairwise_deltas = list(map(lambda x: abs(x[0] - x[1]), processed_frames))
windowed_deltas = rolling_window(pairwise_deltas, 2)

def analyze_signal(frames):
    base_score = 0
    for f in frames:
        a, b = f
        base_score += (a >> 1) ^ (b << 1)
    
    # Apply correction based on checksum
    if checksum_valid([f[0] for f in frames]):
        base_score -= 50
    else:
        base_score += 25
    
    # Final adjustment using feature extraction (key step)
    features = extract_features(frames)
    for feat in features:
        base_score = (base_score + feat) % 1000
    
    # Decoy operations below
    dummy_score = 0
    for f in frames:
        dummy_score += f[0] & f[1]
    dummy_score *= 2  # Never used
    
    # More distractions
    temp_result = list(itertools.accumulate([1, 2, 3]))[-1]  # always 6
    normalization_hint = temp_result * 10
    
    return base_score

# Critical execution point
final_diagnostic = analyze_signal(processed_frames)

print(f"Result: {final_diagnostic}")