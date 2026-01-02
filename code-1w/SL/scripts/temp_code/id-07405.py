from collections import defaultdict, Counter
import math

# Simulated sensor data with noise and metadata
timestamps = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008]
signal_raw = [3.2, 4.1, -2.5, 6.7, 8.9, -1.0, 5.3, 7.8]
noise_profile = {1001: 0.12, 1002: -0.05, 1003: 0.31, 1004: -0.18, 1005: 0.09, 1006: 0.22, 1007: -0.11, 1008: 0.07}
correction_factors = [1.02, 0.98, 1.01, 0.99, 1.03, 1.00, 0.97, 1.04]

# Irrelevant auxiliary variables (distractors)
baseline_offset = 0.5
scaling_factor = 1.75
dummy_cache = {'x': [], 'y': set(), 'z': {}}
shadow_buffer = [0] * 10

# Misleading pre-processing path (dead code)
def deprecated_filter(data):
    return [x for x in data if x > 0]

# Unused transformation function (decoy)
transform_op = lambda z: z ** 2 + 1 if z < 5 else z / 2

# Real signal processing begins
adjusted_signal = []
for i, val in enumerate(signal_raw):
    ts = timestamps[i]
    corrected = val - noise_profile[ts]
    scaled = corrected * correction_factors[i]
    adjusted_signal.append(round(scaled, 2))

# Apply moving average filter (3-point window)
smoothed_signal = []
for i in range(len(adjusted_signal)):
    if i < 2:
        smoothed_signal.append(adjusted_signal[i])
    else:
        window_avg = sum(adjusted_signal[i-2:i+1]) / 3
        smoothed_signal.append(round(window_avg, 2))

# Extract statistical features (some are red herrings)
mean_val = sum(smoothed_signal) / len(smoothed_signal)
amplitude_peaks = [x for x in smoothed_signal if x > mean_val + 1.5]
peak_count = len(amplitude_peaks)

# Distractor: unused frequency analysis
frequency_domain = []
for i in range(len(smoothed_signal)):
    angle = 2 * math.pi * i / len(smoothed_signal)
    freq_comp = smoothed_signal[i] * math.cos(angle)
    frequency_domain.append(round(freq_comp, 3))

# Character encoding distraction (irrelevant string manipulation)
status_codes = ['OK', 'ERR', 'OK', 'WARN', 'OK', 'OK', 'INFO', 'ERR']
code_freq = Counter(status_codes)
encoded_flags = ''.join([code[0] for code in status_codes])
flag_ascii_sum = sum([ord(c) for c in encoded_flags])

# Data bucketing with defaultdict (partially relevant)
bucketed = defaultdict(list)
for idx, val in enumerate(smoothed_signal):
    category = 'high' if val > 6 else 'medium' if val > 3 else 'low'
    bucketed[category].append(val)

# Key computation chain starts here
outlier_candidates = [v for v in smoothed_signal if abs(v - mean_val) > 3]
compression_ratio = len(signal_raw) / (len(outlier_candidates) + 1)

# Nested logic with multiple conditions (3-level nesting)
alert_levels = []
for val in smoothed_signal:
    level = 0
    if val > 5:
        level += 2
        if val > 7:
            level += 3
            if val > mean_val * 1.8:
                level += 1
    elif val < 0:
        level += 1
    alert_levels.append(level)

# Bit manipulation decoy (irrelevant)
bitmask = 0
for lvl in alert_levels:
    bitmask ^= (lvl << 2) & 255

# Core diagnostic algorithm (uses list comprehension and lambda)
weights = [0.8, 1.2, 0.9, 1.1, 1.3, 0.7, 1.0, 1.4]
weighted_alerts = [(a * w) for a, w in zip(alert_levels, weights)]
aggregation_func = lambda x: sum(x) / math.sqrt(len(x) + 1)
raw_diagnostic = aggregation_func(weighted_alerts)

# Final processing with modular arithmetic distraction
mod_tracker = 0
for i in range(int(raw_diagnostic)):
    mod_tracker = (mod_tracker + i * 2) % 7

# Actual answer derivation
final_diagnostic = int(round(raw_diagnostic * 100)) + (flag_ascii_sum % 10)  # inject minor influence from distractor

# Red herring: unused recursive function
def trace_path(n):
    if n <= 1:
        return 1
    return trace_path(n-1) + trace_path(n-2)

# Dead code path with misleading name
def compute_robustness_index(data):
    return sum([abs(d) for d in data]) // (len(data) or 1)

# Output the target result
Result: final_diagnostic