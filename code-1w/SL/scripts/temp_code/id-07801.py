import itertools

# Simulated sensor array data with calibration offsets
data_stream = [14, 7, 23, 11, 5, 19, 13, 3, 8, 17]
calibration_map = {'offset_A': 3, 'offset_B': -2, 'gain': 1.5}

# Irrelevant transformation: frequency analysis (dead end)
frequencies = {x: data_stream.count(x) for x in set(data_stream)}
amplitude_spectrum = [abs(x - 10) for x in data_stream if x > 5]

# Core processing path begins here
raw_moving_avg = [sum(data_stream[i:i+3]) / 3 for i in range(len(data_stream) - 2)]
scaled_readings = [(x + calibration_map['offset_A']) * calibration_map['gain'] for x in raw_moving_avg]

# Distractor: unused recursive filter
def recursive_dampen(seq, factor=0.8):
    if len(seq) <= 1:
        return seq[0] if seq else 0
    return factor * seq[-1] + (1 - factor) * recursive_dampen(seq[:-1], factor)

# Actual relevant transformation: sliding window variance detection
variance_peaks = []
for i in range(len(scaled_readings) - 2):
    window = scaled_readings[i:i+3]
    mean_val = sum(window) / 3
    variance = sum((x - mean_val) ** 2 for x in window) / 3
    if variance > 4.0:
        variance_peaks.append(int(mean_val))

# Decoy statistical analysis (never used)
median_val = sorted(variance_peaks)[len(variance_peaks)//2]
mode_val = max(set(variance_peaks), key=variance_peaks.count)

# Set operations: identify anomalous patterns
peak_set_a = set(variance_peaks)
peak_set_b = set(x + 1 for x in variance_peaks)
common_patterns = peak_set_a & peak_set_b  # Shared adjacent values

# Slicing and shifting to generate candidate signatures
candidate_signature = [sum(common_patterns)] + [len(common_patterns)]
candidate_signature.extend([candidate_signature[0] ^ candidate_signature[1]])

# Generate threshold combinations using itertools
threshold_combinations = list(itertools.product([1, 2], repeat=2))
thresholds = [a * b + 5 for a, b in threshold_combinations]  # Evaluates to [5, 7, 7, 9]

# Transform via Cartesian logic masking (complex but only one path matters)
masked_indices = []
for i, val in enumerate(candidate_signature):
    match_found = False
    for t in thresholds:
        if val == t:
            masked_indices.append(i)
            match_found = True
            break
    if not match_found and val > 10:
        masked_indices.append(i)

# Red herring: bit manipulation chain (unused)
bit_cascade = 0
for idx in masked_indices:
    bit_cascade ^= (idx << 2) | (idx >> 1)

# Critical data transformation: inject base pattern into shifted domain
def transform_sequence(seq, shift_by):
    rotated = seq[shift_by:] + seq[:shift_by]
    return [rotated[i] + i for i in range(len(rotated))]

displacement_key = len(common_patterns) % 3
transformed_data = transform_sequence(candidate_signature, displacement_key)

# Core diagnostic engine (only this function contributes to final answer)
def analyze_pattern(signal, limits):
    base_score = 0
    for i, val in enumerate(signal):
        if val in limits and i % 2 == 0:
            base_score += val
        elif val > 20:
            base_score -= 5
    # Final adjustment based on set intersection history
    if len(common_patterns) > 0:
        base_score *= 2
    return base_score + len(masked_indices)

# Execution point of interest
final_diagnostic = analyze_pattern(transformed_data, thresholds)

print(f"Result: {final_diagnostic}")