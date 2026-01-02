def analyze_system_load(loads):
    cumulative = 0
    peak_moment = -1
    for i, load in enumerate(loads):
        if load > 85:
            peak_moment = i
        cumulative += load * (i + 1)
    return cumulative, peak_moment


def encode_timestamp(ts_str):
    parts = ts_str.split(':')
    return int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])


def decode_timestamp(ts_int):
    h = ts_int // 3600
    m = (ts_int % 3600) // 60
    s = ts_int % 60
    return f'{h:02}:{m:02}:{s:02}'

# Irrelevant helper - distractor
def calculate_compression_ratio(raw, compressed):
    if compressed == 0:
        return float('inf')
    return raw / compressed

# Unused function - red herring
def validate_checksum(data_bytes):
    checksum = 0
    for b in data_bytes:
        checksum = (checksum ^ b) * 13
    return checksum % 256

# Misleading transformation chain
transform_chain = [lambda x: x ** 0.5, lambda x: x * 2.5, lambda x: x + 10]
temp_adjustment = 0
for func in transform_chain:
    temp_adjustment = func(temp_adjustment + 1)

# Decoy data structure
maintenance_log = {
    'last_cleaned': '2023-11-05',
    'filters': ['A7', 'B3'],
    'status_code': 200,
    'downtime_minutes': [12, 8, 15],
    'version': 'v2.1.9'
}

# Real input data
log_entries = [
    {'timestamp': '08:12:34', 'cpu': 78, 'memory': 65, 'disk_queue': 3},
    {'timestamp': '08:13:34', 'cpu': 91, 'memory': 72, 'disk_queue': 6},
    {'timestamp': '08:14:34', 'cpu': 83, 'memory': 68, 'disk_queue': 4},
    {'timestamp': '08:15:34', 'cpu': 94, 'memory': 75, 'disk_queue': 8},
    {'timestamp': '08:16:34', 'cpu': 87, 'memory': 70, 'disk_queue': 5}
]

system_thresholds = {
    'critical_cpu': 90,
    'high_memory': 70,
    'queue_warning': 5
}

# Distractor list comprehension with no side effect
_ = [encode_timestamp(entry['timestamp']) for entry in log_entries if entry['cpu'] > 80]

# Fake aggregation - looks important but unused
baseline_avg = sum([entry['cpu'] for entry in log_entries]) / len(log_entries)
adjusted_scores = []
for idx, entry in enumerate(log_entries):
    score = 0
    if entry['cpu'] > system_thresholds['critical_cpu']:
        score += 3
    if entry['memory'] > system_thresholds['high_memory']:
        score += 2
    if entry['disk_queue'] >= system_thresholds['queue_warning']:
        score += 2
    adjusted_scores.append((idx, score))

# Another red herring: zipping unrelated sequences
timestamps_sec = [encode_timestamp(e['timestamp']) for e in log_entries]
cpu_readings = [e['cpu'] for e in log_entries]
mismatch_pairs = list(zip(timestamps_sec, cpu_readings[::-1]))  # deliberately reversed

# Core logic buried among noise
abnormal_periods = 0
priority_alerts = 0
for i, entry in enumerate(log_entries):
    timestamp_val = encode_timestamp(entry['timestamp'])
    if (entry['cpu'] > system_thresholds['critical_cpu'] and 
        entry['memory'] > system_thresholds['high_memory'] and 
        entry['disk_queue'] >= system_thresholds['queue_warning']):
        abnormal_periods += 1
    if entry['cpu'] > 90 and entry['disk_queue'] > 7:
        priority_alerts += 1

# Secondary processing with real dependency
load_sequence = [e['cpu'] for e in log_entries]
cumulative_load, peak_index = analyze_system_load(load_sequence)

# Final computation - depends on multiple prior results
stability_factor = len(log_entries) - abnormal_periods
alert_penalty = priority_alerts * 15

# Key line: this is where the answer is determined
final_diagnostic = (cumulative_load // 10) - alert_penalty + (stability_factor * 5)

print(f"Result: {final_diagnostic}")