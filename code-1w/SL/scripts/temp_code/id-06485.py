import math

# Irrelevant helper function (dead code path)
def unused_signal_filter(x):
    return [v for v in x if v % 3 == 0]

# Unused transformation (distractor)
def obsolete_transform(seq):
    return [math.sqrt(abs(z)) * 2 for z in seq]

# Misleading intermediate processing
temp_offset = 17
scaling_factor = 0.89
buffer_cache = set()

# Core data generation with red herring elements
raw_readings = [i ^ 13 for i in range(15) if i % 4 != 3]

# Distractor: irrelevant bitwise manipulation
decoy_flags = [(x << 2) ^ 0xA for x in raw_readings]

# Actual meaningful transformation chain
mask = sum([x & 1 for x in raw_readings])  # Count odd values

# Real data flow obscured by noise
noisy_envelope = [x + (i % 7) for i, x in enumerate(raw_readings)]
filtered_band = [y for y in noisy_envelope if y > 5]

# Decoy accumulation (irrelevant)
cumulative_jitter = 0
for val in filtered_band:
    cumulative_jitter += (val * 0.03) ** 2

def apply_calibration(signal, factor=1.1):
    # Unused calibration logic (misdirection)
    return list(map(lambda s: s * factor, signal))

# Critical transformation: only this matters
transformed_data = [x ^ 5 for x in raw_readings]  # XOR with key

# Secondary red herring: complex but unused structure
frequency_map = {i: transformed_data.count(i) for i in set(transformed_data)}
anomaly_threshold = len(transformed_data) // 3

# Bit manipulation used meaningfully here (core logic)
def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

# Real recursive logic (used)
def recursive_entropy(seq, depth=0):
    if depth >= 3 or len(seq) == 0:
        return mask  # Base case ties to earlier computation
    shifted = [count_set_bits(x) for x in seq]
    reduced = [v for v in shifted if v > 1]
    return recursive_entropy(reduced, depth + 1) + sum(shifted[:2])

# Another distractor variable (unused result)
baseline_score = recursive_entropy(raw_readings)

# Set operations used as distraction
exclusion_zone = {1, 3, 5, 7}
safe_band = set(transformed_data) - exclusion_zone

# Lambda and list comprehension combo (meaningful usage)
activation_curve = list(map(lambda z: z * 1.5 if z > 6 else z * 0.7, transformed_data))

# Core analysis function that produces the answer
def analyze_pattern(data):
    total = 0
    for i, x in enumerate(data):
        if i % 2 == 0:
            total += x * 2
        else:
            total -= int(math.log2(x + 1))  # Uses basic log safely
    entropy_contribution = recursive_entropy(data[:len(data)//2])
    return total + entropy_contribution

# Execution point of interest
final_diagnostic = analyze_pattern(transformed_data)

# Final output
print(f"Result: {final_diagnostic}")