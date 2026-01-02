from collections import defaultdict, Counter
import math

# Simulated system telemetry data
timing_log = [
    (100, 'sensor_A', 'read'), (150, 'sensor_B', 'read'), (200, 'sensor_A', 'write'),
    (250, 'sensor_C', 'read'), (300, 'sensor_B', 'write'), (350, 'sensor_A', 'read'),
    (400, 'sensor_D', 'read'), (450, 'sensor_C', 'write')
]

system_flags = [True, False, True, True, False]

# Irrelevant statistical counters (distractor)
dummy_counter = Counter()
for entry in timing_log:
    dummy_counter[entry[1]] += 1

dummy_counter['sensor_X'] = 999  # Red herring value

# Fake signal processing chain (dead code path)
def process_signal(data):
    magnitude = sum([x[0] for x in data]) / len(data)
    return math.sin(magnitude) * 0.01

signal_noise = process_signal(timing_log)  # Unused result

# Misleading intermediate aggregation (decoy logic)
legacy_stats = defaultdict(int)
for ts, sensor, op in timing_log:
    legacy_stats[op] += 1
    if sensor == 'sensor_B':
        legacy_stats['special_case'] += 2  # Distraction

legacy_stats['checksum'] = 777  # Decoy value

# Unused recursive function (red herring)
def calculate_depth(n):
    if n <= 1:
        return 1
    return calculate_depth(n-1) + calculate_depth(n-2)

phantom_depth = calculate_depth(5)  # Computed but unused

# Real computation begins here — heavily masked by prior noise
operation_weights = {'read': 3, 'write': 7}
sensor_priority = defaultdict(int)
for ts, sensor, op in timing_log:
    sensor_priority[sensor] += operation_weights[op]

# Secondary real computation: flag modulation
effective_mod = 1
for i, flag in enumerate(system_flags):
    if flag:
        effective_mod *= (i + 2)  # Uses index-based weighting

effective_mod = effective_mod % 100

# Core metric: weighted sensor priority sum filtered by odd timestamps
weighted_sum = 0
for ts, sensor, op in timing_log:
    if ts % 2 == 1:  # Only odd timestamps contribute
        weighted_sum += sensor_priority[sensor]

# Tertiary manipulation: combine with modulated flags
intermediate = weighted_sum + effective_mod

# Final transformation using string decoys to obscure logic
auxiliary_string = "diagnostics_enabled_v2"
if "v2" in auxiliary_string and len(auxiliary_string.split('_')) > 3:
    intermediate -= len("debug")  # Subtract 5

# Critical statement
final_diagnostic = aggregate_metrics(timing_log, system_flags)

# Actual implementation of aggregate_metrics (mimics above logic)
def aggregate_metrics(log, flags):
    weights = {'read': 3, 'write': 7}
    priority = defaultdict(int)
    for t, s, o in log:
        priority[s] += weights[o]
    
    mod = 1
    for idx, f in enumerate(flags):
        if f:
            mod *= (idx + 2)
    mod %= 100
    
    total = 0
    for t, s, o in log:
        if t % 2 == 1:
            total += priority[s]
    total += mod
    if len("diagnostics_enabled_v2") > 10:
        total -= 5
    return total

# Print final result
print(f"Result: {final_diagnostic}")