from collections import defaultdict, Counter
import math

# Irrelevant helper function (decoy)
def compute_entropy(data):
    freqs = Counter(data)
    total = len(data)
    entropy = 0
    for count in freqs.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 3)

# Unused transformation function (dead code path)
def encrypt_sequence(seq, shift=3):
    return [((x << 1) ^ shift) % 256 for x in seq]

# Core data transformation with red herrings
def transform_input(raw_values, mode='A'):
    temp_buffer = []
    overflow_flags = []
    checksum = 0
    
    for idx, val in enumerate(raw_values):
        if val <= 0:
            continue
        adjusted = val * 2 + (idx % 7)
        if adjusted > 100:
            overflow_flags.append(idx)
            adjusted = 100 - (adjusted % 10)
        temp_buffer.append(adjusted)
        checksum ^= adjusted  # misleading accumulation

    # Distractor: multiple intermediate variables
    stats_log = defaultdict(int)
    for item in temp_buffer:
        stats_log['group_' + str(item // 25)] += 1

    # Real transformation begins here
    processed = [x for x in temp_buffer if x % 2 == 1]  # only odd values matter
    normalized = [x - 9 for x in processed if x > 9]   # shift down meaningful values
    return normalized

# Misleading analysis branch (never called)
def legacy_diagnose(arr):
    if len(arr) < 5:
        return sum(arr) * 0.5
    else:
        return max(arr) - min(arr)

# Key pattern analyzer (critical function)
def analyze_pattern(data, reference):
    lookup_map = defaultdict(list)
    for i, v in enumerate(data):
        lookup_map[v % 4].append(i)
    
    # Irrelevant precomputation
    magnitude_score = sum([v**2 for v in data]) / (len(data) + 1e-8)
    sparsity = len([x for x in data if x == 0])

    # Actual logic masked by noise
    match_count = 0
    for i, ref_val in enumerate(reference):
        if i >= len(data):
            break
        # Only every third index contributes
        if i % 3 == 0 and data[i] % 5 == ref_val:
            match_count += 1
    
    # Secondary condition: must have at least one value > 50
    has_high_energy = any(x > 50 for x in data)
    
    # Final computation buried in distractions
    base_result = match_count * 17
    if has_high_energy:
        base_result += 5
    
    # Decoy adjustment (never affects outcome due to logic guard)
    if magnitude_score > 1000:
        base_result = int(math.sqrt(base_result))
    
    return base_result

# Setup: realistic sensor simulation data
raw_sensor_readings = [12, -5, 23, 8, 19, 44, 6, 31, 50, 3, 41, 7, 0, 29]

# Multiple transformations with irrelevant branches
temp_analysis = encrypt_sequence([x % 10 for x in raw_sensor_readings])
entropy_value = compute_entropy(temp_analysis)  # distractor metric

# Critical execution path
transformed_data = transform_input(raw_sensor_readings, mode='A')
key_sequence = [3, 1, 4, 1, 5, 9, 2, 6]  # digits of pi mod 5 as reference

# Final diagnostic using correct logic chain
final_diagnostic = analyze_pattern(transformed_data, key_sequence)

print(f"Result: {final_diagnostic}")