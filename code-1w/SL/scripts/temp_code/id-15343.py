from collections import defaultdict, Counter
import math

# Simulated system telemetry data
timing_log = [
    {'event': 'startup', 'duration_ms': 120, 'cpu_load': 0.25},
    {'event': 'init_cache', 'duration_ms': 85, 'cpu_load': 0.33},
    {'event': 'load_config', 'duration_ms': 45, 'cpu_load': 0.18},
    {'event': 'bind_ports', 'duration_ms': 210, 'cpu_load': 0.67},
    {'event': 'start_workers', 'duration_ms': 95, 'cpu_load': 0.41}
]

system_state = {
    'status': 'active',
    'nodes': ['n1', 'n2', 'n3'],
    'active_sessions': 23,
    'bandwidth_usage': 0.78,
    'last_restart_age_sec': 3612
}

# Irrelevant helper (dead code path)
def legacy_checksum(data):
    acc = 0
    for i, d in enumerate(data):
        acc += (i + 1) * hash(str(d)) % 97
    return acc % 1000  # Never called

# Misleading intermediate computation (unused)
baseline_avg = sum(e['duration_ms'] for e in timing_log) / len(timing_log)
spike_threshold = baseline_avg * 1.8
detected_spikes = [e for e in timing_log if e['duration_ms'] > spike_threshold]

# Unused transformation
event_names = [e['event'].upper() for e in timing_log]
sorted_events = sorted(timing_log, key=lambda x: x['duration_ms'], reverse=True)

# Decoy statistical analysis
mean_load = sum(e['cpu_load'] for e in timing_log) / len(timing_log)
variance = sum((e['cpu_load'] - mean_load)**2 for e in timing_log) / len(timing_log)
std_dev = math.sqrt(variance)

# Real processing begins here
status_flag = 1 if system_state['status'] == 'active' else 0
node_count = len(system_state['nodes'])

# Build frequency map of duration ranges
bucket_counts = defaultdict(int)
for entry in timing_log:
    bucket = (entry['duration_ms'] // 50) * 50
    bucket_counts[bucket] += 1

# Extract dominant pattern
max_bucket = max(bucket_counts, key=lambda k: bucket_counts[k])

# Simulate diagnostic fingerprint
fingerprint_seed = node_count * 1000 + int(max_bucket)
fingerprint = (fingerprint_seed ^ 0xABCDEF) & 0xFFFF

# Hidden accumulator logic
session_factor = system_state['active_sessions'] % 7
accum = 0
for i in range(3):
    accum = (accum * 31 + session_factor + i) % 10000

# Secondary decoy: correlation attempt (unused)
correlation = 0.0
if len(timing_log) > 1:
    xy_sum = sum(e['duration_ms'] * e['cpu_load'] for e in timing_log)
    x_sum = sum(e['duration_ms'] for e in timing_log)
    y_sum = sum(e['cpu_load'] for e in timing_log)
    numerator = xy_sum - (x_sum * y_sum) / len(timing_log)
    x_sq = sum(e['duration_ms']**2 for e in timing_log)
    y_sq = sum(e['cpu_load']**2 for e in timing_log)
    denom_x = x_sq - (x_sum**2)/len(timing_log)
    denom_y = y_sq - (y_sum**2)/len(timing_log)
    if denom_x > 0 and denom_y > 0:
        correlation = numerator / math.sqrt(denom_x * denom_y)

# Actual metric aggregation function
def aggregate_metrics(log, state):
    # Heavily nested logic with distractions
    total_duration = sum(e['duration_ms'] for e in log)
    critical_count = sum(1 for e in log if e['cpu_load'] > 0.4)
    
    # Red herring: unused weighted score
    weighted_score = sum(
        e['duration_ms'] * (e['cpu_load'] ** 0.5)
        for e in log if e['cpu_load'] > 0.2
    )
    
    # Real signal
    base_metric = total_duration + (critical_count * 100)
    
    # Conditional modulation
    if state['bandwidth_usage'] > 0.75:
        penalty = 250
        if state['last_restart_age_sec'] > 3600:
            penalty += 100
        base_metric += penalty
    else:
        base_metric -= 50
    
    # Final interference: hashing with irrelevant counters
    event_counter = Counter(e['event'].split('_')[0] for e in log)
    prefix_bonus = sum(5 for v in event_counter.values() if v >= 2)
    
    final_value = base_metric + prefix_bonus + status_flag
    
    # This line contains the actual answer generation
    return final_value

# Key execution point
final_diagnostic = aggregate_metrics(timing_log, system_state)

print(f"Result: {final_diagnostic}")