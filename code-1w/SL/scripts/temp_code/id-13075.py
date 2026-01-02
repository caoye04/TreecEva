import itertools

# Simulated sensor data processing pipeline for aerospace telemetry
raw_readings = [0.88, -1.22, 3.14, 0.0, -2.71, 1.41, 2.22, -0.99]
dummy_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# Irrelevant transformation: misleads with string operations
label_map = {k: v for k, v in enumerate([l * 3 for l in dummy_labels])}
expanded_labels = [label_map[i] for i in range(len(dummy_labels)) if i % 2 == 0]

# Distractor: unused complex zip + enumerate structure
temp_pairs = []
for idx, (val, lbl) in enumerate(zip(raw_readings, dummy_labels)):
    if idx % 3 == 0:
        temp_pairs.append((idx, val ** 2, lbl.lower()))

# Real signal preprocessing path
filtered_readings = [x for x in raw_readings if abs(x) > 1.0]
sorted_magnitude = sorted(filtered_readings, key=abs, reverse=True)

# Misleading intermediate: looks important but unused later
cumulative_shift = 0
for i in range(len(sorted_magnitude)):
    cumulative_shift += sorted_magnitude[i] * (0.9 ** i)

# Actual core logic begins: frame segmentation
def segment_into_frames(data, size=3):
    frames = []
    for i in range(0, len(data), size):
        chunk = data[i:i+size]
        if len(chunk) == size:
            frames.append(chunk)
    return frames

processed_frames = segment_into_frames(sorted_magnitude)

# Decoy function: never called, distracts with bit manipulation
def encrypt_frame(frame):
    acc = 0
    for val in frame:
        shifted = int(abs(val) * 100) ^ 0xAA
        acc ^= shifted >> 4
    return acc

# Another red herring: complex counting with sets that goes unused
duplicate_check = set()
seen_values = set()
repetition_count = 0
for val in itertools.chain.from_iterable(processed_frames):
    if val in seen_values:
        duplicate_check.add(val)
        repetition_count += 1
    else:
        seen_values.add(val)

# Core analysis function — only this contributes to final answer
def compute_coherence(frame):
    product = 1.0
    for val in frame:
        product *= abs(val)
    return product / len(frame) if frame else 0

# Secondary real function buried among noise
def analyze_signal(frames):
    scores = []
    for frame in frames:
        score = 0
        # Use enumerate meaningfully within actual logic
        for i, val in enumerate(frame):
            if i % 2 == 0:
                score += val ** 2
            else:
                score -= val
        # Incorporate coherence as weighting factor
        coherence = compute_coherence(frame)
        scores.append(score * coherence)
    # Final aggregation using sum over filtered contributions
    valid_scores = [s for s in scores if s > 0]
    return int(sum(valid_scores)) if valid_scores else -999

# Critical execution point
final_diagnostic = analyze_signal(processed_frames)

# Output required format
print(f"Result: {final_diagnostic}")