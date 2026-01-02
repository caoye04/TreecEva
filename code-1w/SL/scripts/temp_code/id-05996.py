import itertools

# System health monitoring simulation with signal processing
base_signals = [3, 1, 4, 1, 5, 9, 2, 6]
noise_floor = 0.1
correction_factor = 2.5

# Irrelevant calibration data (distractor)
calibration_map = {i: val ** 0.5 for i, val in enumerate([x * 2 for x in base_signals])}
baseline_offset = sum(calibration_map.values()) / len(calibration_map)

# Real processing begins: filter and normalize signals
filtered = [abs(x - noise_floor) for x in base_signals if x > 1]
scaled_signals = [x * correction_factor for x in filtered]

# Simulate packet fragmentation (bit manipulation red herring)
fragment_mask = 0b1111
packets = [(val & fragment_mask, val >> 4) for val in base_signals]
dropped_fragments = [p[1] for p in packets if p[1] < 3]

# Use of enumerate and zip (required features)
signal_pairs = list(zip(scaled_signals, scaled_signals[1:]))
indexed_ratios = []
for idx, (a, b) in enumerate(signal_pairs):
    if idx % 2 == 0:
        ratio = round((a / b) ** 0.5, 3)
        indexed_ratios.append((idx, ratio))

# Decoy function - never called but looks important
def compute_entropy(data):
    from math import log
    total = sum(data)
    probs = [x / total for x in data]
    return -sum(p * log(p) for p in probs if p > 0)

# Another decoy: complex unused transformation
twist_sequence = lambda seq: [x ^ (i % 7) for i, x in enumerate(itertools.accumulate(seq))]
scrambled = twist_sequence(base_signals)

# Actual relevant logic hidden among distractions
def analyze_peaks(data):
    peaks = []
    for i in range(1, len(data) - 1):
        if data[i] > data[i-1] and data[i] > data[i+1]:
            peaks.append(data[i])
    return peaks

peak_values = analyze_peaks(scaled_signals)

# Hidden accumulator with bitwise distraction
temp_checksum = 0
for val in peak_values:
    temp_checksum ^= int(val)
    temp_checksum = (temp_checksum + (temp_checksum << 1)) & 0xFFFF  # Simple hash-like mix

# Destructuring assignment (valid use)
primary_peak, *other_peaks = peak_values

# Multiple simultaneous assignments (red herring cluster)
shadow_factor, gain_ratio, phase_shift = 1.05, 0.98, 17.3
diagnostic_trace = []
status_flags = [True, False, True]

# Core metric computation disguised as one of many steps
tuned_weights = [primary_peak * 0.7, len(other_peaks) * 1.3, len(indexed_ratios) * 0.5]

# Function with short-circuit logic and mixed type evaluation
def validate_diagnostics(flags, threshold=2):
    return len([f for f in flags if f]) >= threshold and not (False in flags)

# Unused diagnostic path (dead code)
if __debug__:
    debug_snapshot = {"raw": base_signals.copy(), "scaled": scaled_signals[:]}

# Main aggregation function - key to answer
def aggregate_metrics(weights, history):
    base_score = sum(w ** 2 for w in weights)
    adjustment = 0
    for i, item in enumerate(history):
        if isinstance(item, tuple) and item[0] % 2 == 0:
            adjustment += item[1] * 0.1
    return base_score - adjustment

# Generate side diagnostics (looks important but only partially used)
for i, sig in enumerate(filtered):
    if sig > 5:
        diagnostic_trace.append((i, round(sig ** 0.3, 2)))

# Critical execution point
final_diagnostic = aggregate_metrics(tuned_weights, diagnostic_trace)

print(f"Result: {final_diagnostic}")