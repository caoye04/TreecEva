import itertools
from functools import reduce

# Simulate sensor data log with timestamps and readings
data_log = [
    {'time': 0.1, 'value': 45, 'status': 'active'},
    {'time': 0.25, 'value': 52, 'status': 'active'},
    {'time': 0.33, 'value': 39, 'status': 'idle'},
    {'time': 0.48, 'value': 61, 'status': 'active'},
    {'time': 0.6, 'value': 44, 'status': 'active'},
    {'time': 0.75, 'value': 55, 'status': 'active'},
    {'time': 0.9, 'value': 37, 'status': 'idle'}
]

# Irrelevant auxiliary function (distractor)
def calculate_entropy(vals):
    total = sum(vals)
    probs = [v / total for v in vals if v > 0]
    return -sum(p * __import__('math').log2(p) for p in probs)

# Misleading intermediate variables
total_energy = sum(entry['value'] for entry in data_log)
avg_time_interval = round((data_log[-1]['time'] - data_log[0]['time']) / (len(data_log) - 1), 2)
status_counter = {s: len(list(g)) for s, g in itertools.groupby(data_log, key=lambda x: x['status'])}

# Threshold for filtering relevant high-performance segments
threshold = 48

# Helper lambda to check if reading exceeds threshold
is_significant = lambda x: x['value'] > threshold and x['status'] == 'active'

# Extract valid segments using list comprehension with filtering
efficient_segments = [entry for entry in data_log if is_significant(entry)]

# Compute cumulative performance metric
cumulative_boost = reduce(lambda acc, x: acc + (x['value'] - threshold), efficient_segments, 0)

# Secondary distraction: simulate cache simulation (unused)
cache_states = ['L1', 'L2', 'L3']
miss_penalty = sum([i * 2 for i in range(len(cache_states))])

# Core logic: compute efficiency score based on duration-weighted contributions
durations = [round(b['time'] - a['time'], 2) for a, b in zip(data_log, data_log[1:])]
weighted_contributions = [
    seg['value'] * durations[i] if i < len(durations) else seg['value'] * 0.1
    for i, seg in enumerate(efficient_segments)
]

# Final processing step
baseline_effort = len([e for e in data_log if e['status'] == 'active']) * threshold
raw_score = sum(weighted_contributions) + cumulative_boost
normalization_factor = max(raw_score / 100, 1)
efficiency_score = int((raw_score - baseline_effort) / normalization_factor)

# Red herring: unused transformation pipeline
pipeline = list(itertools.accumulate(
    [entry['value'] // 10 for entry in data_log],
    func=lambda x, y: (x + y) % 7
))

# Final output assignment
def process_metrics(log, thresh):
    # Recompute only essential metrics
    active_high = [e for e in log if e['value'] > thresh and e['status'] == 'active']
    base = len(active_high) * thresh
    boost = sum(e['value'] - thresh for e in active_high)
    weighted = sum(e['value'] * 0.15 for e in active_high)
    return int((boost + weighted - base) / 1.5)

final_output = process_metrics(data_log, threshold)

Result: {efficiency_score}