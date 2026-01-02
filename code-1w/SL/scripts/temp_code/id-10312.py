from collections import defaultdict, Counter
from itertools import zip_longest

# Simulated telemetry data from a distributed sensor network
timestamps = [1623456780, 1623456785, 1623456790, 1623456795, 1623456800]
sensor_ids = ['S1', 'S2', 'S3', 'S1', 'S2']
readings = [23.1, 45.6, 12.8, 24.0, 44.9]
statuses = ['OK', 'WARNING', 'OK', 'OK', 'CRITICAL']

# Irrelevant auxiliary mapping (distractor)
status_severity = {'OK': 1, 'WARNING': 2, 'ERROR': 3, 'CRITICAL': 4}

# Dead code path - never invoked (red herring)
def legacy_calibrate(x):
    return (x * 1.02) + 5.7

# Unused transformation function (decoy)
def normalize_readings(data):
    mean_val = sum(data) / len(data)
    return [(x - mean_val) / mean_val for x in data]

# Misleading intermediate aggregation (distraction)
raw_stats = defaultdict(list)
for sid, val in zip(sensor_ids, readings):
    raw_stats[sid].append(val)

# Another irrelevant counter (misdirection)
event_counter = Counter(statuses)

# Simulated system state with multiple components (mixed relevance)
system_state = {
    'node_health': {'A': 0.95, 'B': 0.67, 'C': 0.89},
    'last_sync': 1623456780,
    'version': '2.3.1-debug',
    'maintenance_window': False
}

# Log data structure with mixed types and noise
log_data = [
    {'ts': 1623456780, 'src': 'S1', 'val': 23.1, 'type': 'temp', 'meta': {'q': 0.8}},
    {'ts': 1623456785, 'src': 'S2', 'val': 45.6, 'type': 'temp', 'meta': {'q': 0.9}},
    {'ts': 1623456790, 'src': 'S3', 'val': 12.8, 'type': 'temp', 'meta': {'q': 0.7}},
    {'ts': 1623456795, 'src': 'S1', 'val': 24.0, 'type': 'temp', 'meta': {'q': 0.85}},
    {'ts': 1623456800, 'src': 'S2', 'val': 44.9, 'type': 'temp', 'meta': {'q': 0.6}}
]

# Auxiliary computation on node health (partially relevant)
health_factor = 1.0
if all(h > 0.6 for h in system_state['node_health'].values()):
    health_factor *= 1.1
else:
    health_factor *= 0.9

# Spurious data alignment (distractor)
aligned_pairs = list(zip_longest(timestamps, statuses, fillvalue='N/A'))

# Core processing function with nested logic
def analyze_trend(values, threshold=20.0):
    if len(values) < 2:
        return 0
    trend_score = 0
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            trend_score += 1
        elif values[i] < values[i-1]:
            trend_score -= 1
    return trend_score if abs(trend_score) >= threshold else trend_score * 2

# Secondary metric (red herring)
def compute_stability(readings_list, window=2):
    if len(readings_list) < window:
        return 0.0
    diffs = [abs(readings_list[i] - readings_list[i-1]) for i in range(1, len(readings_list))]
    return round(sum(diffs) / len(diffs), 3)

# Main processing pipeline
sensor_trends = {}
for sid in set(sensor_ids):
    sid_readings = [r for s, r in zip(sensor_ids, readings) if s == sid]
    sensor_trends[sid] = analyze_trend(sid_readings)

# Misleading stability report (irrelevant to final result)
stability_index = compute_stability(readings)

# Real-time deviation check (used later)
current_deviation = abs(readings[-1] - readings[0])

# Key processing function
def process_metrics(log_entries, state):
    # Extract valid recent values above quality threshold
    qualified = [entry['val'] for entry in log_entries if entry['meta']['q'] > 0.75]
    
    # Compute base metric
    base_metric = sum(qualified) / len(qualified) if qualified else 0
    
    # Apply health adjustment
    health_multiplier = 1.0
    unhealthy_nodes = [k for k, v in state['node_health'].items() if v < 0.7]
    if unhealthy_nodes:
        health_multiplier = 0.85
    
    # Incorporate trend from S1 (only S1 matters in logic)
    s1_vals = [e['val'] for e in log_entries if e['src'] == 'S1']
    upward_trend = all(s1_vals[i] < s1_vals[i+1] for i in range(len(s1_vals)-1))
    
    # Critical decision branch
    if upward_trend and current_deviation > 0.5:
        adjustment = 1.2
    else:
        adjustment = 0.85
    
    # Final diagnostic score
    diagnostic_score = base_metric * health_multiplier * adjustment
    
    # Dead assignment - looks important but unused (distractor)
    confidence_interval = (diagnostic_score * 0.95, diagnostic_score * 1.05)
    
    return int(round(diagnostic_score))

# Execution point of interest
final_diagnostic = process_metrics(log_data, system_state)

# Print result as required
print(f"Result: {final_diagnostic}")