import itertools

# Simulated sensor data processing with diagnostic analysis
def preprocess_readings(raw_samples):
    filtered = []
    noise_floor = 0.041
    gain_compensation = 1.87
    for sample in raw_samples:
        adjusted = abs(sample * gain_compensation)
        if adjusted > noise_floor:
            filtered.append(adjusted)
    return filtered[:15]

# Irrelevant helper - dead code path (never called)
def deprecated_normalization(x):
    return x / (1 + abs(x))

# Signal pattern analyzer
def generate_pattern_key(sequence, base_shift):
    key = 0
    for i, val in enumerate(sequence):
        if i % 2 == 0:
            key ^= int(val * 100) << (i % 4)
        else:
            key += int(val * 50) % 7
    return key + base_shift

# Misleading transformation (used only in decoy)
def spectral_entropy(signal):
    total = sum(signal)
    entropy = 0.0
    for x in signal:
        p = x / total if total else 0
n        entropy -= p * __import__('math').log(p) if p > 0 else 0
    return round(entropy, 6)

# Decoy function with plausible but unused logic
def evaluate_coherence(pattern):
    if len(pattern) < 5:
        return 0
    coherence_score = 0
    for a, b in zip(pattern, pattern[1:]):
        if b > a:
            coherence_score += 1
    return coherence_score / (len(pattern) - 1)

# Real processing begins here
raw_sensor_data = [
    0.023, -0.015, 0.034, 0.056, -0.021, 0.072, 0.018,
    0.063, -0.009, 0.044, 0.081, 0.027, 0.052, 0.039, 0.076,
    0.013, -0.011, 0.068, 0.047, 0.059
]

processed_readings = preprocess_readings(raw_sensor_data)

# Extraneous variable manipulation (distractor)
temp_analysis = [x**2 for x in processed_readings if x > 0.05]
mean_square_noise = sum(temp_analysis) / len(temp_analysis) if temp_analysis else 0.0

# Construct threshold map using slicing and set logic
threshold_map = {}
for idx, val in enumerate(processed_readings[::3]):
    band = idx % 3
    if band == 0:
        threshold_map[f'low_{idx}'] = val * 0.92
    elif band == 1:
        threshold_map[f'mid_{idx}'] = val * 1.08
    else:
        threshold_map[f'high_{idx}'] = val * 1.21

# Unused but plausible structure (set operations - distractor)
sparse_indices = set(range(0, len(processed_readings), 4))
dense_indices = set(range(0, len(processed_readings), 2))
overlap_region = sparse_indices & dense_indices
redundant_mask = sparse_indices.symmetric_difference(dense_indices)

# Build pattern buffer using itertools combinations (relevant)
pattern_buffer = []
for combo in itertools.combinations_with_replacement(processed_readings[1:6], 2):
    a, b = combo
    pattern_buffer.append(round((a + b) * 0.618, 5))

# More red herring variables
compression_ratio = len(pattern_buffer) / len(processed_readings)
sparsity_metric = len(redundant_mask) / len(processed_readings)

# Actual diagnostic logic (key path)
def analyze_signal(signal_patterns, thresholds):
    base_value = generate_pattern_key(signal_patterns, 202)
    adjustment = 0
    # Use slice and filtering
    segment = signal_patterns[2:7]
    for val in segment:
        if val > 0.04:
            adjustment += int(val * 1000) % 3
    # Extract specific threshold (only one used)
    relevant_threshold = thresholds.get('mid_1', 0.05)
    if base_value % 5 == 0:
        result = (base_value * 0.7) - (adjustment * 100)
    else:
        result = (base_value * 0.73) + (adjustment * 12)
    return int(result - (relevant_threshold * 200))

# Final computation
final_diagnostic = analyze_signal(pattern_buffer, threshold_map)

print(f"Result: {final_diagnostic}")