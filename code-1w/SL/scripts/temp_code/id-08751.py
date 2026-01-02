from collections import defaultdict, Counter

# Simulated system telemetry data
telemetry_stream = [
    {'node': 'A', 'load': 0.7, 'errors': 2, 'temp': 65},
    {'node': 'B', 'load': 0.9, 'errors': 1, 'temp': 70},
    {'node': 'A', 'load': 0.3, 'errors': 0, 'temp': 58},
    {'node': 'C', 'load': 0.95, 'errors': 5, 'temp': 80},
    {'node': 'B', 'load': 0.85, 'errors': 3, 'temp': 72},
    {'node': 'C', 'load': 0.6, 'errors': 1, 'temp': 60}
]

# Irrelevant baseline configuration (distractor)
default_config = {
    'timeout': 30,
    'retries': 3,
    'backoff': 1.5,
    'debug_mode': False
}

# System health thresholds (used in logic)
system_thresholds = {
    'critical_load': 0.9,
    'high_error_rate': 4,
    'overheat_temp': 75
}

# Aggregation helper (used)
def group_by_node(data):
    grouped = defaultdict(list)
    for entry in data:
        grouped[entry['node']].append(entry)
    return grouped

# Misleading auxiliary function (dead code path)
def calculate_efficiency_score(nodes):
    # This function is defined but never called
    efficiency = {}
    for node, records in nodes.items():
        avg_load = sum(r['load'] for r in records) / len(records)
        efficiency[node] = round(1 - avg_load, 2)
    return efficiency

# Red herring transformation (unused)
transformed = [ {k: v*100 if isinstance(v, float) else v for k,v in item.items()} for item in telemetry_stream ]

# Real processing begins here
log_data = group_by_node(telemetry_stream)

# Decoy statistical summary (looks important, not used later)
error_summary = Counter()
for record in telemetry_stream:
    if record['errors'] > 0:
        error_summary[record['node']] += record['errors']

# Auxiliary lambda for dynamic threshold check (used)
is_anomalous = lambda x, thresh: (
    x['load'] > thresh['critical_load'] or 
    x['errors'] > thresh['high_error_rate'] or 
    x['temp'] > thresh['overheat_temp']
)

# Another distraction: simulated historical average (not referenced later)
historical_avg = {
    'A': {'load': 0.5, 'temp': 60},
    'B': {'load': 0.7, 'temp': 65},
    'C': {'load': 0.65, 'temp': 68}
}

# Core diagnostic processor (used)
def process_metrics(data, thresholds):
    diagnostics = {}
    anomaly_count = defaultdict(int)
    total_entries = 0

    # Nested loops with meaningful and distracting operations
    for node, records in data.items():
        critical_events = 0
        temp_alerts = 0  # looks relevant but only partially used

        for record in records:
            total_entries += 1

            # Real condition affecting output
            if is_anomalous(record, thresholds):
                anomaly_count[node] += 1
                critical_events += 1

            # Partially used — temp_alerts incremented but not always counted
            if record['temp'] > thresholds['overheat_temp']:
                temp_alerts += 1  # Distractor within logic

        # Key calculation: number of anomalous events per node
        diagnostics[node] = {
            'anomalies': critical_events,
            'status': 'CRITICAL' if critical_events >= 2 else 'WARNING' if critical_events == 1 else 'OK'
        }

    # Secondary distractor: sorting that isn't used
    sorted_nodes = sorted(diagnostics.keys(), key=lambda x: diagnostics[x]['anomalies'], reverse=True)

    # Critical intermediate result (misleading name)
    weighted_risk_score = 0
    for node in diagnostics:
        weighted_risk_score += diagnostics[node]['anomalies'] * 100
        if diagnostics[node]['status'] == 'CRITICAL':
            weighted_risk_score += 50  # bonus for critical status

    # Final computation — this is where answer comes from
    flattened_logs = [item for sublist in data.values() for item in sublist]
    total_anomalies = sum(1 for log in flattened_logs if is_anomalous(log, thresholds))

    # The actual final result
    final_component_a = sum(diagnostics[n]['anomalies'] for n in diagnostics)
    final_component_b = len([n for n in diagnostics if diagnostics[n]['status'] == 'CRITICAL'])
    final_diagnostic = final_component_a * 10 + final_component_b * 5

    return final_diagnostic

# Execution point of interest
final_diagnostic = process_metrics(log_data, system_thresholds)
print(f"Result: {final_diagnostic}")