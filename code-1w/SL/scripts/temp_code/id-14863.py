import math

# Simulated sensor data with noise and metadata
data_stream = [
    {'id': 1, 'val': 3.2, 'type': 'A', 'active': True},
    {'id': 2, 'val': -1.5, 'type': 'B', 'active': False},
    {'id': 3, 'val': 4.8, 'type': 'A', 'active': True},
    {'id': 4, 'val': 2.1, 'type': 'C', 'active': True},
    {'id': 5, 'val': -3.3, 'type': 'A', 'active': True},
    {'id': 6, 'val': 0.0, 'type': 'B', 'active': True},
    {'id': 7, 'val': 5.5, 'type': 'A', 'active': False}
]

# Irrelevant auxiliary data (distractor)
system_logs = [
    {'ts': 100, 'event': 'init', 'level': 'INFO'},
    {'ts': 105, 'event': 'poll', 'level': 'DEBUG'},
    {'ts': 110, 'event': 'reset', 'level': 'WARN'}
]

# Decoy function – looks important but unused in main logic
def analyze_log_integrity(logs):
    return sum(1 for log in logs if log['level'] == 'ERROR')

# Misleading transformation chain (dead path)
temp_amplitudes = list(map(lambda x: abs(x['val']) ** 0.5, filter(lambda x: x['type'] == 'C', data_stream)))
baseline_correction = [a * 1.05 for a in temp_amplitudes]  # Not used later

# Real processing begins here
valid_entries = [entry for entry in data_stream if entry['active'] and entry['val'] != 0]

# Extract indices and values using enumerate (relevant)
indexed_vals = [(i, d['val']) for i, d in enumerate(valid_entries)]

# Apply dynamic gain based on position (even index: x2, odd: x0.5)
gained_vals = []
for idx, val in indexed_vals:
    if idx % 2 == 0:
        gained_vals.append(val * 2)
    else:
        gained_vals.append(val / 2)

# Filter out negative values (important step)
positive_gained = [v for v in gained_vals if v > 0]

# Simulate frequency weighting using zip with offset neighbors (relevant)
shifted = positive_gained[1:] + [0]
weighted = [a * 0.7 + b * 0.3 for a, b in zip(positive_gained, shifted) if a != 0]

# Secondary filter based on magnitude threshold (triggers at > 1.0)
filtered_data = list(filter(lambda x: x > 1.0, weighted))

# Auxiliary computation (distractor): harmonic mean of inactive elements (never used)
inactive_vals = [d['val'] for d in data_stream if not d['active'] and d['val'] != 0]
harm_mean = len(inactive_vals) / sum(1 / abs(v) for v in inactive_vals) if inactive_vals else 0

# Core signal processor: applies exponential smoothing
alpha = 0.3
def process_signals(seq):
    if not seq:
        return 0.0
    smoothed = seq[0]
    for i in range(1, len(seq)):
        smoothed = alpha * seq[i] + (1 - alpha) * smoothed
    return round(smoothed, 6)

# Additional red herring: recursive checksum (unused)
def calc_checksum(arr, depth=0):
    if depth >= 3 or not arr:
        return 0
    return (arr[0] ** 2) % 7 + calc_checksum(arr[1:], depth + 1)

# Critical execution point
final_output = process_signals(filtered_data)

# Print result as required
print(f"Result: {final_output}")