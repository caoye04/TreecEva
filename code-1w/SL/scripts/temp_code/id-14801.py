def analyze_sequence(data_stream):
    temp_accum = 0
    for i, val in enumerate(data_stream):
        if i % 3 == 0:
            temp_accum += val * 2
        elif i % 5 == 0:
            temp_accum -= val
    return temp_accum


def compute_entropy(signal):
    entropy = 0.0
    for x in signal:
        if x > 0:
            entropy -= x * math.log(x + 1e-9)
    return entropy

import math

# Simulated system log with timestamped events and noise
log_entries = [
    {'time': 100, 'event': 'READ', 'value': 5},
    {'time': 105, 'event': 'WRITE', 'value': 3},
    {'time': 110, 'event': 'READ', 'value': 8},
    {'time': 115, 'event': 'ERROR', 'value': 1},
    {'time': 120, 'event': 'READ', 'value': 6}
]

# Irrelevant auxiliary data (distractor)
signal_data = [0.1, 0.4, 0.2, 0.3]
noise_floor = compute_entropy(signal_data)

# Complex preprocessing with red herrings
baseline_shift = 0
for entry in log_entries:
    baseline_shift += entry['time'] % 7
    entry['flagged'] = (entry['event'] == 'ERROR')
    entry['adjusted'] = entry['value'] + (entry['time'] % 3)

# Unused transformation path (dead code - distractor)
transformed = []
for idx, e in enumerate(log_entries):
    transformed.append({'index': idx, 'val': e['value'] ** 2})

# Core diagnostic logic buried in noise
checksum = 0
for i, entry in enumerate(log_entries):
    if entry['event'] == 'READ':
        checksum ^= entry['value']  # Bitwise accumulation
    elif entry['event'] == 'WRITE':
        checksum += i * 2

# Secondary metric with partial relevance
read_count = sum(1 for e in log_entries if e['event'] == 'READ')
error_severity = sum(e['value'] for e in log_entries if e['event'] == 'ERROR')

# Distractor: complex but unused combinatorics
pair_count = 0
for i in range(len(log_entries)):
    for j in range(i + 1, len(log_entries)):
        pair_count += 1

# Threshold calculation using modular arithmetic and case logic
system_threshold = (read_count * 10 + error_severity) % 17

# Misleading intermediate (looks important but unused)
avg_adjusted = sum(e['adjusted'] for e in log_entries) / len(log_entries)

# Auxiliary function that seems relevant but is not used in final step
def extract_features(entries):
    features = []
    for e in entries:
        features.append({
            'hash': (e['time'] + e['value']) % 13,
            'type_id': 1 if e['event'] == 'READ' else 2
        })
    return features

# Critical data transformation using zip and enumerate
timestamps = [e['time'] for e in log_entries]
values = [e['value'] for e in log_entries]
weighted_sum = 0
for idx, (t, v) in enumerate(zip(timestamps, values)):
    if t % 2 == 0:
        weighted_sum += v * (idx + 1)

# Another decoy function with recursion (not used)
def recursive_weight(n):
    if n <= 1:
        return n
    return recursive_weight(n - 2) + recursive_weight(n - 1)

# Real processing chain buried in complexity
sequence_data = [e['value'] for e in log_entries if e['event'] != 'ERROR']
processed_signal = analyze_sequence(sequence_data)

# Final computation disguised among distractions
initial_diagnostic = (processed_signal + checksum) % 1000

# Key state mutation
scaling_factor = 3 if read_count >= 2 else 1

# Final answer depends on multiple subtle interactions
final_diagnostic = (initial_diagnostic * scaling_factor) - (system_threshold // 2)

# Decoy output lines (misleading prints)
# print(f'Noise floor: {noise_floor}')
# print(f'Pair count: {pair_count}')
# print(f'Average adjusted: {avg_adjusted}')

# Only this matters
print(f'Target result: {final_diagnostic}')