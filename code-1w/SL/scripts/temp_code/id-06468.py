def analyze_pattern(data):
    """Irrelevant helper that appears useful but isn't on critical path"""
    return [x ** 0.5 for x in data if x % 3 == 0]


def generate_lookup(keys):
    """Decoy function - never called in execution"""
    return {k: k * 2 + 1 for k in keys}

# Misleading intermediate arrays
temp_buffer = [18, 27, 36, 45, 54]
diagnostic_trace = [0] * 5

for i in range(len(temp_buffer)):
    diagnostic_trace[i] = (temp_buffer[i] // 9) * 3

# Real data input disguised among noise
raw_signal = [12, 15, 22, 28, 33, 35, 40]
noise_floor = 17
amplitude_mask = [x > noise_floor for x in raw_signal]

# Bit manipulation red herring
bit_flags = 0
for val in raw_signal[:3]:
    bit_flags ^= (val & 7) | (val << 2)

# Character counting decoy (strings seem related to signal processing)
system_log = "calibration phase sync complete at zone 5"
char_count = sum(1 for c in system_log if c in 'aeiou')

# Threshold map with meaningful structure but partial relevance
threshold_map = {
    'low': 20,
    'optimal': 30,
    'high': 38
}

# Key sequence derived via list comprehension and zip
indices = list(range(len(raw_signal)))
weighted_pairs = list(zip(raw_signal, indices))
sequence = [a * (b + 1) for a, b in weighted_pairs if a > 15]

# Linear search simulation (distractor)
search_hits = []
for idx, val in enumerate(sequence):
    if val % 4 == 0:
        search_hits.append(idx)

# Unused recursive attempt (dead code path)
def recursive_dampen(x, depth):
    if depth <= 0 or x < 10:
        return x
    return recursive_dampen(x // 2, depth - 1)

# Core validation logic - only this matters
filtered_sequence = [x for x in sequence if x > threshold_map['optimal']]
penalty = 0
for item in filtered_sequence:
    if item >= threshold_map['high']:
        penalty += 1

baseline_score = len(filtered_sequence) * 5
adjustment = sum(1 for x in sequence if x <= threshold_map['low'])

# Critical statement with answer-determining computation
filtration_score = validate_calibration(sequence, threshold_map)

# Supporting function defined after use (another distraction)
def validate_calibration(seq, thresholds):
    upper_bound = thresholds['high']
    lower_bound = thresholds['optimal']
    count_valid = 0
    total_contribution = 0.0

    for val in seq:
        # Only values in optimal-high range contribute
        if lower_bound < val <= upper_bound:
            count_valid += 1
            total_contribution += val / 2.5
    
    # Final score combines count and scaled contribution
    if count_valid == 0:
        return 0
    return int((count_valid * 7) + round(total_contribution))

# Print result for evaluation
Result: filtration_score