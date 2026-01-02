from collections import defaultdict, Counter
import math

# Simulated sensor array data from a spacecraft subsystem
sensor_ids = ['S1', 'S2', 'S3', 'S4', 'S5']
base_readings = [78, 85, 92, 67, 73]
calibration_offsets = [1.2, -0.8, 1.5, -1.1, 0.9]
status_flags = [True, False, True, True, False]

# Irrelevant auxiliary mappings (distractor)
task_priorities = {'S1': 3, 'S2': 1, 'S3': 4, 'S4': 2, 'S5': 5}
system_weights = defaultdict(lambda: 1.0)
for sid in sensor_ids:
    system_weights[sid] = 0.9 + (ord(sid[-1]) % 7) * 0.1

# Generate raw readings with calibration (relevant)
raw_data = [base_readings[i] + calibration_offsets[i] for i in range(len(base_readings))]

# Misleading health score calculation (red herring)
health_score = sum(1 for x in raw_data if x > 75) * 10
aux_score = sum([int(flag) for flag in status_flags]) * 5
fake_diagnostic = health_score - aux_score + len(sensor_ids)

# Complex transformation chain (relevant but obfuscated)
def transform_signal(x, idx):
    if idx % 2 == 0:
        return x * math.cos(math.pi / (idx + 2))
    else:
        return x * math.sin(math.pi / (idx + 3))

transformed = [transform_signal(raw_data[i], i) for i in range(len(raw_data))]

# Decoy function with unused recursion (dead path)
def recursive_dampener(n, depth=0):
    if depth >= 3 or n <= 1:
        return n
    return recursive_dampener(n // 2, depth + 1) + recursive_dampener(n - 2, depth + 1)

# Simulate packet loss and recovery (irrelevant)
packet_sequence = list(enumerate(['OK', 'OK', 'LOST', 'OK', 'RETRY', 'OK']))
recovery_log = []
for idx, status in packet_sequence:
    if status == 'LOST':
        recovery_log.append(f'Retrying packet {idx}')
    elif status == 'RETRY':
        recovery_log.append(f'Successful retry at {idx}')

# Core diagnostic logic (critical path)
readings = dict(zip(sensor_ids, transformed))

# Flag-based filtering mask (misleading intermediate)
valid_mask = [flag for flag in status_flags]
active_sensors = [sid for i, sid in enumerate(sensor_ids) if valid_mask[i]]

# Health signature generation via frequency analysis (relevant)
frequency_map = defaultdict(int)
for val in raw_data:
    bucket = int(val // 5)
    frequency_map[bucket] += 1

sorted_freq = sorted(frequency_map.items(), key=lambda x: x[1], reverse=True)
dominant_band = sorted_freq[0][0] * 5 + 2.5  # Center of dominant 5-unit band

# Secondary decoy structure (unused)
correlation_matrix = [[0 for _ in range(5)] for _ in range(5)]
for i in range(5):
    for j in range(i+1, 5):
        correlation_matrix[i][j] = abs(raw_data[i] - raw_data[j])
        correlation_matrix[j][i] = correlation_matrix[i][j]

# Real processing function with multiple concepts
health_signature = []
for i, (sid, val) in enumerate(readings.items()):
    deviation = abs(val - base_readings[i])
    if status_flags[i]:
        adjusted_val = val * (1 + math.log(2 + i) / 10)
    else:
        adjusted_val = val * 0.85
    health_signature.append((sid, adjusted_val, deviation))

# Final computation with list comprehension and zip (key step)
basic_elements = [x[1] for x in health_signature]
weight_vector = [0.8, 1.1, 0.9, 1.2, 0.7]  # Manual weights
weighted_sum = sum(a * b for a, b in zip(basic_elements, weight_vector))
penalty = sum(x[2] for x in health_signature if x[2] > 1.0)

# Destructuring and conditional assignment
_, primary_value, _ = health_signature[0]
backup_chain = [primary_value]
if len(active_sensors) < 4:
    backup_chain.append(dominant_band)
else:
    backup_chain.append(weighted_sum)

# Actual answer computation (non-obvious path)
def process_metrics(signature, readings_dict):
    total = 0.0
    for entry in signature:
        sensor_id, adj_val, dev = entry
        raw_val = readings_dict[sensor_id]
        contribution = adj_val * (1 + dev / 100)
        if 'S3' in sensor_id or 'S1' in sensor_id:
            contribution *= 0.95
        total += contribution
    total -= penalty * 1.5
    return round(total, 4)

# Critical execution point
final_diagnostic = process_metrics(health_signature, readings)

# Print result as required
print(f"Result: {final_diagnostic}")