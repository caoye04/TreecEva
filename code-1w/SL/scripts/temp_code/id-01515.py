import itertools

# Simulated sensor array diagnostics with noise filtering and pattern analysis
sensor_ids = [101, 102, 103, 104]
raw_readings = [
    [5, 8, 12, 10, 15, 7],
    [6, 9, 11, 14, 16, 8],
    [4, 7, 10, 13, 15, 6],
    [5, 8, 12, 11, 14, 9]
]

# Irrelevant baseline calibration (red herring)
baseline_calibrations = {sid: sum(reads) / len(reads) * 0.95 for sid, reads in zip(sensor_ids, raw_readings)}
offset_map = {i: i * 0.05 for i in range(1, len(sensor_ids)+1)}

# Noise reduction using moving average (distraction)
def smooth_signal(signal, window=3):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window + 1)
        end = i + 1
        smoothed.append(sum(signal[start:end]) / (end - start))
    return smoothed

# Apply smoothing (but not used in final path)
smoothed_readings = [smooth_signal(reads) for reads in raw_readings]

# Key transformation: extract rising edge patterns
thresholds = {sid: 10 for sid in sensor_ids}
activation_log = {}

for idx, sid in enumerate(sensor_ids):
    above_threshold = [v >= thresholds[sid] for v in raw_readings[idx]]
    # Count transitions from below to above threshold
    transitions = 0
    for i in range(1, len(above_threshold)):
        if not above_threshold[i-1] and above_threshold[i]:
            transitions += 1
    activation_log[sid] = transitions

# Decoy function: computes unrelated metric
def compute_entropy(values):
    from collections import Counter
    counts = Counter(values)
    total = len(values)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Non-standard pseudo-entropy
    return round(entropy, 4)

entropy_diagnostics = {sid: compute_entropy(raw_readings[i]) for i, sid in enumerate(sensor_ids)}

# Real processing path begins here — hidden among distractions
def generate_combinations(data_list):
    # Generate all 2-element combinations of indices where value >= threshold
    combo_indices = []
    for i, val_i in enumerate(data_list):
        for j, val_j in enumerate(data_list):
            if i < j and val_i >= 10 and val_j >= 10:
                combo_indices.append((i, j))
    return combo_indices

combination_map = {sid: generate_combinations(raw_readings[i]) for i, sid in enumerate(sensor_ids)}
total_combinations = sum(len(combos) for combos in combination_map.values())

# Transform data into frequency of high-magnitude events per sensor
event_frequencies = {sid: sum(1 for v in raw_readings[i] if v >= 10) for i, sid in enumerate(sensor_ids)}
transformed_data = list(event_frequencies.values())

# Secondary decoy: set operations with no impact
all_peaks = set(itertools.chain.from_iterable(
    [i for i, v in enumerate(reads) if v >= 12] for reads in raw_readings
))
shadow_set = set(itertools.combinations_with_replacement([1, 2], 2))

# Critical function: analyzes combinatorial growth pattern
def analyze_pattern(frequencies, threshold_map):
    # Model system stability based on frequency variance and combinatorics
    mean_freq = sum(frequencies) / len(frequencies)
    variance = sum((f - mean_freq) ** 2 for f in frequencies) / len(frequencies)
    
    # Simulate interaction matrix: each frequency contributes squared interactions
    total_interactions = 0
    for r in itertools.combinations(frequencies, 2):
        total_interactions += r[0] * r[1]
    
    # Dummy branch (never taken, misleading)
    if mean_freq > 100:
        scaling = 0.1
    else:
        scaling = 1
    
    # Actual determinant: interaction-to-variance ratio scaled by fixed factor
    if variance == 0:
        return 0
    diagnostic_score = (total_interactions / variance) * 0.73
    return int(diagnostic_score)

# Final computation — answer depends only on this
final_diagnostic = analyze_pattern(transformed_data, thresholds)

# Print result as required
print(f"Result: {final_diagnostic}")