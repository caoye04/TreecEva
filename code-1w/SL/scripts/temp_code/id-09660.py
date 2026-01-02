import math

# Irrelevant helper function (decoy)
def normalize_signal(x):
    return [val / max(x) for val in x]

# Unused transformation (dead code path)
def legacy_transform(data):
    return [d ** 2 + 1 for d in data if d % 3 == 0]

# Simulate sensor readings with noise
raw_readings = [144, 169, 196, 225, 256, 289, 324, 361]

# Extract magnitude peaks (irrelevant to final result)
magnitude_peaks = [math.sqrt(x) for x in raw_readings if x > 200]

# Generate harmonic interference (red herring)
harmonics = set()
for r in raw_readings:
    if r % 2 == 0:
        harmonics.add(r // 2)
    if r % 3 == 0:
        harmonics.add(r // 3)

# Segment data into batches of 4
segment_data = lambda data: [data[i:i+4] for i in range(0, len(data), 4)]

# Core processing pipeline
base_segments = segment_data(raw_readings)

# Noise floor estimation (distractor computation)
noise_floor = sum([sum(seg) for seg in base_segments]) / len(raw_readings)
threshold_adjustment = math.log(noise_floor, 2) if noise_floor > 1 else 0

# Main purification process
process_sequence = lambda segs: [
    int(sum(s) ** 0.5) for s in segs
]

# Validate purity using set intersection logic (key concept)
def validate_purity(values):
    expected = set(range(min(values), max(values) + 1))
    actual = set(values)
    missing = expected - actual
    # Purity score based on completeness
    purity_ratio = len(actual & expected) / len(expected)
    # Secondary check: avoid trivial sequences
    if len(values) < 2:
        return -1
    # Dominant frequency analysis (misleading intermediate)
    freqs = {}
    for v in values:
        freqs[v] = freqs.get(v, 0) + 1
    dominant = max(freqs.values())
    # Final score combines purity and structure
    structural_weight = 1 + (values[-1] % 3) / 10
    return int((purity_ratio * 100) * structural_weight)

# Spurious list transformation (dead path)
decomposed = []
for seg in base_segments:
    for item in seg:
        decomposed.append(item % 7)

# Unused bit manipulation chain (red herring)
bit_signature = 0
for d in decomposed[:5]:
    bit_signature ^= (d << 2) | (d >> 1)

# Critical execution point
filtration_score = validate_purity(process_sequence(segment_data(raw_readings)))

# Output result
print(f"Target result: {filtration_score}")