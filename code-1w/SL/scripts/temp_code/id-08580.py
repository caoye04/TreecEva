from collections import defaultdict, Counter
from itertools import cycle, islice

def simulate_sensor_drift(readings):
    # Irrelevant function: simulates sensor noise but not used in final calculation
    return [r + 0.01 * i for i, r in enumerate(readings)]

def validate_checksum(sequence):
    # Misleading function: looks important but unused
    return sum(sequence) % 256

def decode_transmission(signal):
    # Dead code path — never called
    return [int(s) for s in signal.split(',') if s.isdigit()]

# Simulated system telemetry
telemetry_stream = [18, 23, 15, 44, 9, 22, 14, 30]

# Distractor variables
redundant_buffer = list(reversed(telemetry_stream))
shadow_copy = [x * 2 for x in telemetry_stream if x < 20]
baseline_offset = sum(telemetry_stream) / len(telemetry_stream)

# Complex data transformation with red herrings
aggregation_map = defaultdict(int)
for idx, val in enumerate(telemetry_stream):
    aggregation_map[idx % 4] += val

# Unused intermediate structure
frequency_count = Counter(telemetry_stream)

# Simulate multi-phase diagnostics
phase_weights = [0.1, 0.3, 0.5, 0.7]
weighted_phases = []
for i in range(4):
    weighted_phases.append(aggregation_map[i] * phase_weights[i])

# Decoy calculation: looks like integrity check but irrelevant
checksum_diagnostic = validate_checksum(telemetry_stream)

# Key logic buried among distractions
active_signals = [v for v in telemetry_stream if v > 15]
masked_array = [a ^ b for a, b in zip(active_signals, cycle([1, 3]))]

# Secondary filtering
filtered_diagnostics = []
for x in masked_array:
    if x % 2 == 0:
        filtered_diagnostics.append(x // 2)
    else:
        filtered_diagnostics.append(x * 3 + 1)

# Nested conditional manipulation
adjusted_diagnostics = []
for num in filtered_diagnostics:
    if num < 10:
        adjusted_diagnostics.append(num ** 2)
    elif num > 20:
        adjusted_diagnostics.append(num - 10)
    else:
        adjusted_diagnostics.append(num + 5)

# Multi-step reduction
rolling_averages = []
window_size = 2
for i in range(len(adjusted_diagnostics) - window_size + 1):
    window_avg = sum(adjusted_diagnostics[i:i+window_size]) / window_size
    rolling_averages.append(round(window_avg, 2))

# Real key computation hidden in middle of noise
system_state = [sum(adjusted_diagnostics), len(rolling_averages), baseline_offset]

# Core answer-generating function
def compute_integrity_score(state):
    raw_score = state[0] * state[1]
    penalty = int(state[2] // 1)
    return raw_score - penalty

# Final execution point
final_diagnostic = compute_integrity_score(system_state)
print(f"Result: {final_diagnostic}")