from collections import defaultdict, Counter

# Simulate sensor data stream with anomalies
sensor_ids = ['S1', 'S2', 'S3', 'S1', 'S2', 'S4', 'S3', 'S1']
timestamps = [100, 105, 110, 115, 120, 125, 130, 135]
readings = [23.1, 45.6, 12.8, 23.3, 45.5, 67.0, 13.0, 23.0]
statuses = [1, 1, 0, 1, 1, 1, 0, 1]  # 1: active, 0: error

# Track occurrences and aggregate data
id_count = Counter(sensor_ids)
status_map = defaultdict(list)
for i, sid in enumerate(sensor_ids):
    status_map[sid].append(statuses[i])

# Compute redundancy score (irrelevant distractor)
redundancy_score = sum(len(v) for v in status_map.values() if len(v) > 1) * 2

# Analyze timestamp intervals (semi-relevant)
intervals = [timestamps[i] - timestamps[i-1] for i in range(1, len(timestamps))]
interval_stats = {
    'avg': sum(intervals) / len(intervals),
    'max_gap': max(intervals),
    'stability': intervals.count(5)
}

# Filter valid readings (active sensors only)
valid_readings = [readings[i] for i in range(len(readings)) if statuses[i] == 1]
valid_ids = [sensor_ids[i] for i in range(len(sensor_ids)) if statuses[i] == 1]

# Compute base statistical modes per sensor (distractor computation)
reading_by_id = defaultdict(list)
for i, sid in enumerate(valid_ids):
    reading_by_id[sid].append(valid_readings[i])

modes = {}
for sid, vals in reading_by_id.items():
    rounded_vals = [round(v, 1) for v in vals]
    freq = Counter(rounded_vals)
    modes[sid] = freq.most_common(1)[0][0]

# Sum of modes mod 256 (used later)
sum_modes = int(sum(modes.values()) * 10)  # Scale to integer impact

# Character analysis from sensor IDs (distractor)
char_freq = Counter(''.join(sensor_ids))
unique_chars = set(char_freq.keys())
ad_hoc_weight = len(unique_chars) * char_freq.get('S', 0)

# Core checksum calculation begins
base_value = 0
for i, (sid, val) in enumerate(zip(valid_ids, valid_readings)):
    contribution = (i + 1) * (ord(sid[-1]) ^ int(val))
    base_value += contribution

base_value = (base_value * 31) % 65536

# Running XOR over scaled valid readings
running_xor = 0
scaling_factor = 10
for val in valid_readings:
    scaled = int(val * scaling_factor)
    running_xor ^= scaled

# Secondary loop for id patterns (partially redundant)
id_xor = 0
for j, sid in enumerate(sensor_ids):
    temp = 0
    for c in sid:
        temp ^= ord(c) * (j + 1)
    if statuses[j] == 1:
        id_xor ^= temp % 256

# Final checksum depends only on base_value, running_xor, and sum_modes
final_checksum = base_value ^ running_xor ^ (sum_modes % 256)

# Irrelevant diagnostic print (dead code path)
if False:
    print(f'Diagnostics: {redundancy_score}, {ad_hoc_weight}, {interval_stats}')

print(f'Result: {final_checksum}')