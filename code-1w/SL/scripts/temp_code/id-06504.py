import math

# Simulated sensor data with timestamps and readings
data_log = [
    {'time': 0.1, 'value': 45, 'sensor_id': 101},
    {'time': 0.2, 'value': 52, 'sensor_id': 101},
    {'time': 0.3, 'value': 48, 'sensor_id': 102},
    {'time': 0.4, 'value': 55, 'sensor_id': 102},
    {'time': 0.5, 'value': 60, 'sensor_id': 101},
    {'time': 0.6, 'value': 58, 'sensor_id': 103},
    {'time': 0.7, 'value': 63, 'sensor_id': 103},
    {'time': 0.8, 'value': 61, 'sensor_id': 101}
]

# Auxiliary function to compute time gaps (distractor: not used in final logic)
def compute_drift(log):
    times = [entry['time'] for entry in log]
    return sum(times[i] - times[i-1] for i in range(1, len(times)))

# Misleading preprocessing step
baseline_shift = sum(entry['value'] for entry in data_log if entry['sensor_id'] == 101) / 4
offset_map = {101: baseline_shift * 0.1, 102: baseline_shift * 0.05, 103: 0}

# Red herring: unused transformation
transformed_log = [
    {**entry, 'adjusted': entry['value'] + offset_map[entry['sensor_id']]}
    for entry in data_log
]

# Real processing begins here
sensor_stats = {}
for entry in data_log:
    sid = entry['sensor_id']
    if sid not in sensor_stats:
        sensor_stats[sid] = {'count': 0, 'total': 0, 'max_val': 0}
    sensor_stats[sid]['count'] += 1
    sensor_stats[sid]['total'] += entry['value']
    if entry['value'] > sensor_stats[sid]['max_val']:
        sensor_stats[sid]['max_val'] = entry['value']

# Compute average per sensor
averages = {sid: info['total'] / info['count'] for sid, info in sensor_stats.items()}

# Define efficiency metric using only sensors above threshold (logic dependency)
active_sensors = [sid for sid, avg in averages.items() if avg > 50]

# Distractor: complex lambda that's partially unused
aggregator = lambda x, y: x * 1.1 + y * 0.9
shadow_value = aggregator(baseline_shift, len(transformed_log))

# Core calculation chain
base_efficiency = 0
for sid in active_sensors:
    peak = sensor_stats[sid]['max_val']
    base_efficiency += math.sqrt(peak) * 10

# Introduce irrelevant combinatorics (distractor)
from itertools import combinations
pair_count = len(list(combinations(active_sensors, 2)))
phantom_factor = pair_count if pair_count > 2 else 1

# Final metric computation
scaling_factor = len(active_sensors) or 1
intermediate = base_efficiency / scaling_factor

# Key variable assignment
efficiency_score = round(intermediate + 5, 2)

# Unused state tracking
history = [{'step': 'init', 'val': 0}, {'step': 'proc', 'val': efficiency_score}]

# Critical execution point
final_output = process_metrics(data_log)

# Dummy function to simulate API (must be defined)
def process_metrics(log):
    return efficiency_score

print(f"Result: {efficiency_score}")