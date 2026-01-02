def analyze_pattern(seq):
    count = 0
    for i, val in enumerate(seq):
        if i % 2 == 0 and val % 3 == 0:
            count += 1
    return count

# Irrelevant helper (decoy)
def compute_entropy(data):
    import math
    total = 0
    for x in data:
        if x > 0:
            total -= x * math.log(x)
    return total

# Unused transformation (dead code path)
def transform_sequence(s):
    return [x ** 2 - 1 for x in s if x % 2]

# Real logic embedded with distractions
sequence = [12, 15, 18, 21, 24, 27, 30]
offsets = [3, 6, 9, 12, 15, 18, 21]

paired = list(zip(sequence, offsets))

# Distractor: complex-looking but unused calculation
total_momentum = sum(a * b for a, b in paired) / len(paired) if paired else 0

scaling_factor = 0.0
for idx, (val, off) in enumerate(paired):
    if val > 20:
        scaling_factor += off / (idx + 1)

# Another red herring: plausible but irrelevant metric
weighted_avg = sum(i * v for i, v in enumerate(sequence)) / len(sequence)

# Key data processing chain
base_values = [v // 3 for v in sequence if v % 3 == 0]
index_map = {i: base_values[i] for i in range(len(base_values))}

# Misleading intermediate result
counterfeit_index = sum(1 for v in base_values if v % 2 == 0)

# Real signal extraction
def extract_signal(indices, mapper):
    signal = 0
    for k in indices:
        if k < len(mapper) and mapper[k] > 5:
            signal += mapper[k] * (k + 1)
    return signal

signal_strength = extract_signal([1, 2, 3], index_map)

# Decoy function call (looks important)
entropy_proxy = compute_entropy([0.1, 0.2, 0.7])

# Actual core computation begins here
base = signal_strength * 2

# Simulate environmental interference (distraction)
interference_log = []
for i in range(3):
    temp = (base + i * 10) % 7
    interference_log.append(temp)

# Correction mechanism based on pattern analysis
correction_factor = analyze_pattern(sequence) * 1.5

# Final adjustment
final_flux = 0

# Critical statement
final_flux = adjust_flux(base, correction_factor)

# Definition hidden below to increase trace difficulty
def adjust_flux(b, c):
    if b <= 0:
        return 0
    adjusted = b * c
    # Apply dampening if over threshold
    if adjusted > 100:
        adjusted *= 0.9
    return int(adjusted)

# Print result for evaluation
Target result: {final_flux}