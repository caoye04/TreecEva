from collections import defaultdict, Counter
import itertools

# Simulated sensor data aggregation (distractor: some sensors are irrelevant)
sensor_ids = ['S1', 'S2', 'S3', 'S4', 'S5']
raw_readings = {
    'S1': [0.88, 0.91, 0.87, 0.89],
    'S2': [1.2, 1.5, 1.3, 1.4],
    'S3': [0.45, 0.47, 0.46, 0.48],
    'S4': [2.1, 2.3, 2.2, 2.1],
    'S5': [0.76, 0.78, 0.75, 0.77]
}

# Irrelevant preprocessing: signal smoothing (unused later)
def smooth_signal(signal):
    return [sum(signal[i:i+3]) / 3 for i in range(len(signal) - 2)]

# Dead function - never called
def analyze_pattern(seq):
    trends = []
    for i in range(1, len(seq)):
        trends.append(1 if seq[i] > seq[i-1] else 0)
    return Counter(trends)

# Distractor variables
temp_log = []
debug_mode = True
system_uptime = 1274

# Real processing begins here
health_data = defaultdict(list)
for sid, readings in raw_readings.items():
    avg = sum(readings) / len(readings)
    health_data[sid].append(avg)
    if 'S3' in sid:
        health_data[sid].append(avg * 1.2)  # Special adjustment

# Threshold logic with misleading branches
thresholds = {
    'S1': (0.85, 0.95),
    'S2': (1.0, 1.6),
    'S3': (0.40, 0.50),
    'S4': (2.0, 2.5),
    'S5': (0.70, 0.80)
}

# Complex nested conditionals with red herrings
status_flags = {}
for k, v in health_data.items():
    low, high = thresholds[k]
    val = v[0]
    if val < low:
        status_flags[k] = 'UNDER'
        if debug_mode:
            temp_log.append(f'{k}: below threshold')
    elif val > high:
        status_flags[k] = 'OVER'
        if k == 'S4':
            system_uptime += 10  # Irrelevant side effect
    else:
        status_flags[k] = 'NORMAL'

# Decoy aggregation
summary_stats = {}
for key, values in raw_readings.items():
    summary_stats[key] = {
        'mean': sum(values) / len(values),
        'variance': sum((x - sum(values)/len(values))**2 for x in values) / len(values),
        'peak': max(values)
    }

# Real but hidden logic path: XOR-based anomaly detection on flag patterns
flag_code = 0
for flag in status_flags.values():
    if flag == 'UNDER':
        flag_code ^= 3
    elif flag == 'OVER':
        flag_code ^= 5
    else:
        flag_code ^= 7

# Additional distraction: unused combinatorics
combinations = list(itertools.combinations(sensor_ids, 3))
valid_combos = [c for c in combinations if 'S1' in c and 'S5' not in c]
combo_count = len(valid_combos)

# Core transformation: only S1, S3, S5 contribute to final result via weighted harmonic mean
working_sensors = ['S1', 'S3', 'S5']
reciprocal_sum = 0.0
weight_sum = 0

for s in working_sensors:
    raw_val = health_data[s][0]
    if status_flags[s] == 'NORMAL':
        weight = 2.0
    else:
        weight = 1.0
    reciprocal_sum += weight / raw_val
    weight_sum += weight

weighted_harmonic = weight_sum / reciprocal_sum

# Secondary factor: bit manipulation on flag_code (previously computed)
binary_rep = bin(flag_code)[2:].zfill(4)
bit_score = 0
for i, bit in enumerate(binary_rep):
    bit_score += int(bit) * (2 ** i)  # reverse weighting

# Final computation
final_diagnostic = int(weighted_harmonic * 100) + bit_score * 10

# Distractor print (not affecting result)
if debug_mode:
    print(f'Debug: {combo_count} valid combos')

Result: final_diagnostic