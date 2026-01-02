import itertools

# System diagnostic module for signal integrity analysis
def analyze_signal_integrity(raw_samples, threshold=0.75):
    normalized = [x / max(raw_samples) for x in raw_samples]
    anomalies = [i for i, x in enumerate(normalized) if x > threshold]
    return anomalies

# Irrelevant helper - distractor function
def smooth_signal(data, passes=2):
    temp = data.copy()
    for _ in range(passes):
        temp = [(temp[i-1] + temp[i] + temp[(i+1) % len(temp)]) / 3 for i in range(len(temp))]
    return temp

# Core encoding logic with bit manipulation
def encode_segment(segment_data, mode='crc'):
    if mode == 'crc':
        crc = 0
        for val in segment_data:
            crc ^= val << 4
            crc &= 0xFFFF
            crc ^= (crc >> 7)
        return crc
    elif mode == 'parity':
        return sum(segment_data) % 2
    return -1

# Data windowing - legitimate preprocessing
sample_stream = [12, 45, 67, 23, 89, 34, 56, 78, 91, 15]
windows = [sample_stream[i:i+4] for i in range(0, len(sample_stream), 4)]

# Generate encoded segments using CRC - relevant path
encoded_segments = []
for win in windows:
    if len(win) >= 3:
        enc = encode_segment(win, 'crc')
        encoded_segments.append(enc)

# Dead code path - misleading control flow
if len(encoded_segments) > 10:
    encoded_segments = [x for x in encoded_segments if x % 2 == 0]
elif len(encoded_segments) == 3:
    # This branch is taken but leads to irrelevant computation
    temp_weights = [0.1, 0.2, 0.3]
    adjusted = [a * w for a, w in zip(encoded_segments, temp_weights)]
    smoothed = smooth_signal(adjusted)
else:
    # Unused fallback
    encoded_segments.append(encode_segment([0], 'parity'))

# Decoy metrics calculation - looks important but unused
redundancy_score = sum(1 for x in encoded_segments if x > 100)
consistency_ratio = len([x for x in windows if sum(x) > 100]) / len(windows)

# Weight assignment with set operation distraction
all_values = set(itertools.chain.from_iterable([[x] if isinstance(x, int) else x for x in windows]))
dominant_bits = {x for x in all_values if (x & 8) == 8}  # bitmask filter - red herring
weights = [0.5 if v in dominant_bits else 0.25 for v in encoded_segments]

# Real metric aggregation - critical computation
baseline_shift = sum(sample_stream) / len(sample_stream)
offset_factor = (baseline_shift * 0.01) ** 2

# Lambda-based transformation - partially relevant
transform = lambda x, w: round((x * w) + offset_factor)

# Aggregate using weighted transform - this produces the real answer
aggregate_metrics = lambda segments, wts: sum(
    transform(seg, wt) for seg, wt in zip(segments, wts)
)

# Key execution point
final_diagnostic = aggregate_metrics(encoded_segments, weights)

# Output result as required
print(f"Result: {final_diagnostic}")