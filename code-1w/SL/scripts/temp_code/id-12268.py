import math

# Irrelevant helper function (dead code path)
def unused_signal_filter(x):
    return [v for v in x if v % 3 == 0]

# Decoy transformation with misleading intermediate results
def decoy_enhance(seq):
    shifted = [x << 2 for x in seq]  # Bit manipulation red herring
    normalized = [s / max(shifted) for s in shifted]
    return [round(n * 100) for n in normalized]  # Distracting scaling

# Actual core logic: cycle detection in transformed bit patterns
def extract_cycles(data):
    binary_map = [bin(d & 0b111)[2:].zfill(3) for d in data]  # Keep only 3 least significant bits
    cycle_count = 0
    for b in binary_map:
        if b[0] == b[1] and b[1] == b[2]:  # All bits equal
            cycle_count += 1
    return cycle_count

# Real transformation: applies bit rotation and filtering
def transform_sequence(seq, threshold=15):
    rotated = [(x >> 1) | ((x & 1) << 3) for x in seq]  # 4-bit right rotate
    filtered = [r for r in rotated if r > threshold]
    return rotated, filtered  # Return both for distraction

# Secondary analysis: computes entropy-like metric on bit frequency
def compute_dispersion(values):
    freq = {i: 0 for i in range(8)}
    for v in values:
        bucket = v & 0b111
        freq[bucket] += 1
    nonzero = [f for f in freq.values() if f > 0]
    if len(nonzero) == 0:
        return 0.0
    entropy = -sum(f / len(values) * math.log(f / len(values)) for f in nonzero)
    return round(entropy * 100, 4)

# Main analysis function (called at end)
def analyze_pattern(dataset):
    temp_result = []
    for item in dataset:
        if item & 1:  # Only odd numbers contribute
            temp_result.append(item ^ 0b1010)  # XOR mask as noise
    reduced = [x for x in temp_result if x < 20]  # Final filter
    score = sum(reduced) * len(reduced) if reduced else -1
    return score

# Irrelevant constants and variables (distractors)
CALIBRATION_FACTOR = 0.987
REFERENCE_PATTERN = [1, 1, 2, 3, 5, 8, 13]
MAX_ITERATIONS = 1000
TEMP_BUFFER = [0] * 64

# Primary data input (real initial data)
raw_input = [12, 7, 14, 9, 13, 6, 11]

# Step 1: Transform sequence — returns both full and filtered (only full used)
rotated_data, _ = transform_sequence(raw_input, threshold=10)

# Step 2: Apply irrelevant decoy enhancement on original
enhanced_raw = decoy_enhance(raw_input)  # Not used later

# Step 3: Extract cycles from rotated data — result not directly used but looks important
cycle_diagnostic = extract_cycles(rotated_data)

# Step 4: Compute dispersion on rotated (distraction)
dispersion_metric = compute_dispersion(rotated_data)

# Step 5: Real processing begins — slicing and lambda-based filtering
effective_slice = rotated_data[1:6:2]  # Take indices 1, 3, 5: values are [11, 13, 7]
pre_filtered = list(filter(lambda x: (x & 0b10) != 0, effective_slice))  # Keep if second bit set

# Step 6: Further transformation using XOR and modulus
transformed_data = [(p ^ 5) % 17 for p in pre_filtered]

# Key execution point: final analysis on transformed data
final_diagnostic = analyze_pattern(transformed_data)

print(f"Result: {final_diagnostic}")