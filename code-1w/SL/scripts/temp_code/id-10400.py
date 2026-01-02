from collections import defaultdict, Counter
import math

# Simulated system telemetry data with multiple irrelevant fields
telemetry_stream = [
    {'node': 'A', 'temp': 45, 'load': 0.6, 'errors': 2, 'uptime': 1200, 'priority': 'high'},
    {'node': 'B', 'temp': 50, 'load': 0.8, 'errors': 1, 'uptime': 900, 'priority': 'medium'},
    {'node': 'A', 'temp': 47, 'load': 0.7, 'errors': 0, 'uptime': 1250, 'priority': 'high'},
    {'node': 'C', 'temp': 60, 'load': 0.5, 'errors': 5, 'uptime': 800, 'priority': 'low'},
    {'node': 'B', 'temp': 55, 'load': 0.9, 'errors': 3, 'uptime': 950, 'priority': 'medium'},
    {'node': 'C', 'temp': 62, 'load': 0.4, 'errors': 7, 'uptime': 820, 'priority': 'low'}
]

# Irrelevant baseline metrics (distractor)
baseline_performance = {
    'avg_response_time': 120,
    'peak_throughput': 850,
    'retry_count': 3,
    'cache_hit_ratio': 0.88
}

# System thresholds for diagnostics (relevant)
system_thresholds = {
    'temp_warning': 50,
    'error_burst': 4,
    'load_spike': 0.75
}

# Auxiliary function that appears important but is never called (dead code path)
def calculate_health_score(nodes):
    return sum([100 - n['temp'] + (10 if n['priority'] == 'high' else 0) for n in nodes])

# Decoy transformation using lambda (irrelevant)
transform_payload = lambda x: {k: v * 2 if isinstance(v, int) and k != 'uptime' else v for k, v in x.items()}

# Aggregation of logs by node (partially relevant)
log_by_node = defaultdict(list)
for entry in telemetry_stream:
    log_by_node[entry['node']].append(entry)

# Spurious counter for error types (misleading intermediate)
error_distribution = Counter()
for log in telemetry_stream:
    if log['errors'] > 0:
        error_distribution[f"node_{log['node']}"] += log['errors']

# Fake normalization routine (dead path)
normalized_telemetry = []
for item in telemetry_stream:
    normalized = item.copy()
    normalized['load'] = round(normalized['load'] ** 0.5, 3)
    normalized_telemetry.append(normalized)

# Real processing begins here — aggregation of critical events
critical_events = []
for node, records in log_by_node.items():
    event_count = 0
    for r in records:
        # Check for temperature warning
        temp_alert = r['temp'] > system_thresholds['temp_warning']
        # Check for error burst
        error_alert = r['errors'] >= system_thresholds['error_burst']
        # Check for load spike
        load_alert = r['load'] >= system_thresholds['load_spike']
        # All three must be true to count as critical (complex condition)
        if temp_alert and error_alert and load_alert:
            event_count += 1
    critical_events.append(event_count)

# Secondary metric: cumulative risk score (distractor calculation)
risk_accumulator = 0
for entry in telemetry_stream:
    risk_factor = 0
    if entry['temp'] > 55:
        risk_factor += 3
    if entry['errors'] >= 5:
        risk_factor += 4
    if entry['load'] > 0.85:
        risk_factor += 2
    risk_accumulator += risk_factor  # Used nowhere

# String-based diagnostic tagger (seemingly complex but irrelevant)
diag_tags = []
for entry in telemetry_stream:
    tags = []
    if entry['temp'] > 50:
        tags.append('T')
    if entry['load'] > 0.7:
        tags.append('L')
    if entry['errors'] > 0:
        tags.append('E')
    diag_tags.append('-'.join(tags) if tags else 'OK')

# Real logic: compute diagnostic from critical event counts
# Only entries with at least one critical event contribute
active_risk_nodes = [e for e in critical_events if e > 0]

# Summation of active risks (key operation)
raw_diagnostic = sum(active_risk_nodes)

# Final transformation using logarithmic scaling (relevant)
if raw_diagnostic > 0:
    final_diagnostic = math.log(raw_diagnostic) * 100
else:
    final_diagnostic = 50

# Spurious formatting routine (decoy)
format_results = lambda data: [f"{k}:{v}" for k, v in sorted(data.items())]

# Another unused accumulator (red herring)
total_uptime = sum(e['uptime'] for e in telemetry_stream)

# Key execution point
final_diagnostic = process_metrics(log_data, system_thresholds)

# Simulate missing function with inline replacement to maintain correctness
# Re-define process_metrics to reflect actual logic
def process_metrics(log_data, thresholds):
    local_counter = defaultdict(int)
    for record in log_data:
        node = record['node']
        if (record['temp'] > thresholds['temp_warning'] and 
            record['errors'] >= thresholds['error_burst'] and 
            record['load'] >= thresholds['load_spike']):
            local_counter[node] += 1
    total_critical = sum(local_counter.values())
    return math.log(total_critical) * 100 if total_critical > 0 else 50

# Recompute final_diagnostic correctly
final_diagnostic = process_metrics(telemetry_stream, system_thresholds)

print(f"Result: {final_diagnostic}")