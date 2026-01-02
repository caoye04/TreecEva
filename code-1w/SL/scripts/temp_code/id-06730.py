import math

# Irrelevant utility function (dead code path)
def normalize_vector(v):
    norm = sum(x ** 2 for x in v) ** 0.5
    return [x / norm for x in v]

# Misleading data transformation
temp_readings = [23.4, 25.1, 22.8, 24.6, 26.3, 23.9]
adjusted_readings = [round(t * 1.02, 2) for t in temp_readings]
correction_factor = sum(adjusted_readings) / len(adjusted_readings) - 24.0

# Simulated sensor log with metadata
sensor_log = {
    'device_id': 'SEN-TRX9',
    'firmware': 'v2.1.7',
    'readings': [
        {'ts': 1001, 'val': 85, 'flag': False},
        {'ts': 1002, 'val': 92, 'flag': True},
        {'ts': 1003, 'val': 78, 'flag': False},
        {'ts': 1004, 'val': 96, 'flag': True},
        {'ts': 1005, 'val': 88, 'flag': False}
    ]
}

# Decoy statistical analysis
mean_val = sum(r['val'] for r in sensor_log['readings']) / len(sensor_log['readings'])
variance = sum((r['val'] - mean_val) ** 2 for r in sensor_log['readings']) / len(sensor_log['readings'])
std_dev = math.sqrt(variance)

# Irrelevant string processing
device_code = sensor_log['device_id']
code_parts = device_code.split('-')
prefix = code_parts[0]
suffix = code_parts[1]

# Character frequency map (distractor)
char_freq = {}
for c in ''.join(code_parts):
    char_freq[c] = char_freq.get(c, 0) + 1

# Unused lambda transformation
transform = lambda x: x ** 2 - x * 3 + 2
transformed_vals = [transform(r['val']) for r in sensor_log['readings']]

# Real computation begins — data log for performance evaluation
data_log = [
    {'event': 'init', 'duration': 120, 'success': True},
    {'event': 'encode', 'duration': 450, 'success': True},
    {'event': 'transfer', 'duration': 320, 'success': False},
    {'event': 'decode', 'duration': 180, 'success': True},
    {'event': 'verify', 'duration': 90, 'success': True}
]

# Baseline thresholds (in milliseconds)
baseline = {
    'encode': 500,
    'decode': 200,
    'verify': 100
}

# Auxiliary dictionary operations (partially relevant)
status_map = {True: 'pass', False: 'fail'}
event_status = {item['event']: status_map[item['success']] for item in data_log}

duration_map = {item['event']: item['duration'] for item in data_log}

# Complex conditional scoring with nested logic
contribution = 0.0
penalty = 0.0

for entry in data_log:
    event = entry['event']
    duration = entry['duration']
    success = entry['success']
    
    # Only certain events are scored against baseline
    if event in baseline:
        if success:
            if duration <= baseline[event]:
                contribution += 25.0
            else:
                contribution += 15.0
                penalty += 5.0 * (duration - baseline[event]) / baseline[event]
        else:
            penalty += 15.0
    
    # Hidden bonus condition: consecutive successes
    idx = data_log.index(entry)
    if success and idx > 0:
        prev = data_log[idx - 1]
        if prev['success']:
            contribution += 2.0  # bonus for continuity

# Red herring calculation using string methods
log_str = "Event log: " + ", ".join(event_status.keys())
word_count = len(log_str.split())
has_duplicate = len(set(log_str)) < len(log_str)

# Secondary irrelevant metric
efficiency_ratio = (sum(duration_map.values()) / 1000.0) / len(data_log)

# Core evaluation logic — actual answer depends on this
weighted_average = (contribution - penalty) * 0.95

# Final adjustment based on character count from earlier distractor
adjustment = sum(char_freq.values()) % 7

# Critical statement — determines final result
final_score = int(weighted_average - adjustment)

# Print result as required
print(f"Result: {final_score}")