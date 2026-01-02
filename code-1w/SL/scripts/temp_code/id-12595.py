def analyze_phase_shift(signal, threshold=0.65):
    if len(signal) < 3:
        return 0
    count = 0
    for i in range(1, len(signal) - 1):
        if signal[i-1] < signal[i] > signal[i+1]:
            count += 1
    return count if count > threshold * 2 else int(count * 0.7)


def generate_keyframes(dataset):
    keyframes = []
    for idx, entry in enumerate(dataset):
        if idx % 3 == 0 and entry['status'] == 'active':
            keyframes.append(entry['value'] ** 0.5)
    return [round(k, 2) for k in keyframes]


def merge_diagnostics(a, b):
    s1, s2 = set(a), set(b)
    intersection_score = len(s1 & s2)
    union_score = len(s1 | s2)
    return (intersection_score / union_score) if union_score != 0 else 0


def compute_entropy(sequence):
    from math import log2
    freq = {}
    for item in sequence:
        freq[item] = freq.get(item, 0) + 1
    total = len(sequence)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 4)

# Irrelevant helper (dead path)
def unused_normalizer(x):
    return (x - min(x)) / (max(x) - min(x))

# Misleading metric with no impact
temporal_weights = [0.1, 0.3, 0.6, 0.9]
spectral_buffer = (1.2, 0.8, 1.5, 2.1, 0.7)

# Real data inputs
diagnostic_log = [
    {'id': 'A7', 'status': 'active', 'value': 16},
    {'id': 'B2', 'status': 'inactive', 'value': 25},
    {'id': 'C9', 'status': 'active', 'value': 36},
    {'id': 'D4', 'status': 'active', 'value': 49},
    {'id': 'E1', 'status': 'failed', 'value': 64}
]

signal_waveform = [0.4, 0.9, 0.6, 1.3, 0.8, 1.1, 0.7]
baseline_readings = [4, 5, 6, 7, 8, 9]

# Distractor: complex-looking but unused computation
aggregate_frame = tuple(x * 1.05 for x in baseline_readings)
shifted_grid = [x + 0.1 for x in aggregate_frame if x > 6]

# Core trace data
trace_a = [3, 5, 5, 2, 3, 7, 7, 7]
trace_b = [5, 2, 3, 7, 9, 5, 7]
overlap_metric = merge_diagnostics(trace_a, trace_b)

# Generate relevant intermediate values
key_timepoints = generate_keyframes(diagnostic_log)
phase_count = analyze_phase_shift(signal_waveform)

# Simulated entropy of system states
state_sequence = ['idle', 'run', 'run', 'sleep', 'idle', 'run', 'halt']
process_entropy = compute_entropy(state_sequence)

# Construct signature using correct path
signature_components = []
for val in key_timepoints:
    if val > 3.0:
        signature_components.append(int(val * 2))

# Add phase count adjusted by entropy
adjusted_phase = int(phase_count * (1 + process_entropy))

# Use set operations to filter noise
raw_signature = set(signature_components)
noise_floor = {4, 6, 8}
cleaned_signature = raw_signature - noise_floor

health_signature = tuple(sorted(cleaned_signature))
baseline_traces = tuple(baseline_readings[1::2])  # [5, 7, 9]

# Critical statement
final_diagnostic = process_metrics(health_signature, baseline_traces)

# Definition of required function
def process_metrics(sig, base):
    sum_sig = sum(s * (i+1) for i, s in enumerate(sig))
    sum_base = sum(b * (i+1) for i, b in enumerate(base))
    ratio = sum_sig / sum_base if sum_base != 0 else 0
    return round(ratio * 1000, 0)

print(f"Result: {final_diagnostic}")