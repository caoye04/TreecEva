import math

# Simulated sensor array data processing pipeline
raw_readings = [384, 192, 448, 512, 256, 320, 368, 400, 288, 224]
offsets = [12, -8, 15, -20, 5, 0, -10, 7, -3, 18]
calibration_map = {i: round(math.log(i + 1) * 1.7, 4) for i in range(100, 600, 50)}

# Irrelevant preprocessing: spectral weights (dead-end computation)
spectral_weights = [round(math.sin(i / 30) ** 2, 3) for i in range(len(raw_readings))]
weighted_spectrum = [raw_readings[i] * spectral_weights[i] for i in range(len(raw_readings))]
dispersion_factor = sum(weighted_spectrum) / len(weighted_spectrum) if weighted_spectrum else 0

# Signal normalization with offset correction and mapped calibration
adjusted_signals = []
for idx, reading in enumerate(raw_readings):
    adj_val = reading + offsets[idx]
    closest_calib_key = min(calibration_map.keys(), key=lambda x: abs(x - adj_val))
    adj_val = int(adj_val * calibration_map[closest_calib_key] / 100)
    adjusted_signals.append(adj_val)

# Red herring: frequency harmonics analysis (unused)
harmonic_components = []
for val in adjusted_signals:
    components = []
    for h in range(1, 4):
        comp = val * (h / (h + 1))
        if comp > 100:
            components.append(round(comp, 2))
    harmonic_components.append(components)

temporal_gradient = [adjusted_signals[i+1] - adjusted_signals[i] for i in range(len(adjusted_signals)-1)]
spike_count = sum(1 for g in temporal_gradient if abs(g) > 15)

# Real processing begins: filtering and windowing
filtered_signals = [x for x in adjusted_signals if 50 < x < 300]
window_size = 3
sliding_windows = [filtered_signals[i:i+window_size] for i in range(len(filtered_signals)-window_size+1)]

# Compute rolling mean deviation from median baseline
median_baseline = sorted(filtered_signals)[len(filtered_signals)//2]
mean_deviation = sum(abs(x - median_baseline) for x in filtered_signals) / len(filtered_signals)

# Normalize signals relative to dynamic threshold envelope
dynamic_amplitude = max(filtered_signals) - min(filtered_signals)
effective_gain = 1.0 + (mean_deviation / (dynamic_amplitude or 1))
normalized_signals = [round((x - min(filtered_signals)) * effective_gain, 3) for x in filtered_signals]

# Threshold logic with bit-flagged conditions
thresholds = {
    't1': 12.5,
    't2': 25.0,
    't3': 40.0,
    't4': 60.0
}

# Decoy function: never called
def compute_entropy(seq):
    from collections import Counter
    counts = Counter(seq)
    total = len(seq)
    return -sum((count/total)*math.log2(count/total) for count in counts.values())

# Another decoy: complex transformation chain (unreferenced)
power_hierarchy = []
for i in range(len(normalized_signals)):
    base = normalized_signals[i]
    hierarchy = []
    for level in range(4):
        base = (base ** 0.5) * (level + 1)
        hierarchy.append(round(base, 3))
    power_hierarchy.append(hierarchy)

# Actual aggregation logic
flag_state = 0
acc_metric = 0.0

for val in normalized_signals:
    # Bitwise flag updates based on multiple thresholds
    if val > thresholds['t1']:
        flag_state |= 1
    if val > thresholds['t2']:
        flag_state |= 2
    if val > thresholds['t3']:
        flag_state |= 4
    if val > thresholds['t4']:
        flag_state |= 8
    
    # Accumulate transformed values only when certain flags are set
    if flag_state & 3:  # at least t1 and t2 exceeded
        acc_metric += math.log(val + 1) * (flag_state & 7)

# Secondary adjustment using slice-based statistics
recent_contributions = acc_metric / len(normalized_signals) if normalized_signals else 0
slice_peaks = [max(normalized_signals[i:i+2]) for i in range(0, len(normalized_signals), 2) if normalized_signals[i:i+2]]
peak_influence = sum(p > thresholds['t3'] for p in slice_peaks)

# Final diagnostic calculation
baseline_score = acc_metric + recent_contributions
adjustment_penalty = (peak_influence * flag_state) / (effective_gain or 1)
final_diagnostic = int(baseline_score - adjustment_penalty)

# Misleading print (debug remnant)
# print(f'Debug: dispersion={dispersion_factor}, spikes={spike_count}')

Result: final_diagnostic