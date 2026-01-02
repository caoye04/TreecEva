from collections import defaultdict, Counter

# Simulated system telemetry data from distributed nodes
telemetry_streams = {
    'node_7': [127, 134, 129, 131, 134, 126],
    'node_2': [95, 92, 94, 93, 96, 95, 91],
    'node_9': [145, 152, 148, 150, 152, 149, 154],
    'node_4': [88, 85, 87, 86, 89, 84, 86]
}

# Irrelevant auxiliary mapping – red herring for signal processing
auxiliary_filters = {
    'alpha': lambda x: (x * 1.05) - 2,
    'beta': lambda x: (x + 1) // 1.1,
    'gamma': lambda x: x ** 0.5 * 3
}

# System health thresholds (real constraint)
system_thresholds = {
    'critical': 140,
    'warning': 120,
    'normal': 90
}

# Misleading statistical summaries – unused in final logic
decoy_aggregates = {}
for node, readings in telemetry_streams.items():
    avg = sum(readings) / len(readings)
    peak = max(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    # These are calculated but never used
    decoy_aggregates[node] = {
        'mean': round(avg, 2),
        'max_deviation': peak - avg,
        'variance': round(variance, 3)
    }

# Real-time anomaly detection using sliding window (unused path)
def detect_spikes(stream, window_size=3, sensitivity=1.1):
    spikes = []
    for i in range(len(stream) - window_size + 1):
        window = stream[i:i+window_size]
        if max(window) > sensitivity * sum(window) / window_size:
            spikes.append(i)
    return spikes  # Computed but not used

# Hidden diagnostic code path – looks important but irrelevant
node_spike_reports = {}
for node, data in telemetry_streams.items():
    report = detect_spikes(data, window_size=2)
    node_spike_reports[node] = len(report) > 0

# Core data transformation pipeline
log_data = []
for node_id, values in telemetry_streams.items():
    prefix = node_id.split('_')[1]
    category = 'A' if int(prefix) % 2 == 0 else 'B'
    # Only nodes above warning level contribute to log
    filtered_values = [v for v in values if v > system_thresholds['warning']]
    for val in filtered_values:
        log_data.append({'source': node_id, 'value': val, 'class': category})

# Decoy bit manipulation function – appears low-level and critical
compute_checksum = lambda data: sum(
    (val << 2) ^ (val >> 1) for val in data
) % 256

checksums = {}
for node, vals in telemetry_streams.items():
    checksums[node] = compute_checksum(vals)  # Calculated but ignored

# Central processing logic with distractor conditions
anomaly_counter = Counter()
class_metrics = defaultdict(lambda: {'count': 0, 'total': 0, 'alerts': 0})

for entry in log_data:
    val = entry['value']
    cls = entry['class']
    
    # Real logic: count anomalies above critical threshold
    if val > system_thresholds['critical']:
        anomaly_counter[entry['source']] += 1
    
    # Accumulate class-level metrics
    class_metrics[cls]['count'] += 1
    class_metrics[cls]['total'] += val
    
    # Alert logic only triggers on specific pattern
    if val > system_thresholds['critical'] and '9' in entry['source']:
        class_metrics[cls]['alerts'] += 1

# Secondary metric: weighted risk index (distractor)
risk_index = 0
for cls, metrics in class_metrics.items():
    if metrics['count'] > 0:
        avg_val = metrics['total'] / metrics['count']
        risk_index += avg_val * (metrics['alerts'] + 1)

# Unused recursive helper – mimics complex analysis
def calculate_depth_score(value, depth=0):
    if value <= system_thresholds['normal'] or depth >= 3:
        return depth
    return calculate_depth_score(value // 2, depth + 1)

depth_scores = {k: calculate_depth_score(max(v)) for k, v in telemetry_streams.items()}  # Dead code

# Final processing step – only this matters
def process_metrics(log_entries, thresholds):
    high_risk_nodes = set()
    node_contributions = defaultdict(int)
    
    # Relevant aggregation
    for entry in log_entries:
        src = entry['source']
        val = entry['value']
        if val > thresholds['critical']:
            node_contributions[src] += 1
    
    # Only nodes with multiple critical events are flagged
    for count in node_contributions.values():
        if count >= 2:
            high_risk_nodes.add(src)
    
    # Diagnostic score: number of class B entries with high value
    diagnostic_score = sum(
        1 for e in log_entries 
        if e['value'] > thresholds['critical'] and e['class'] == 'B'
    )
    
    # Final result derived from specific condition
    base = len(anomaly_counter) * 100
    bonus = sum(class_metrics[c]['alerts'] for c in class_metrics) * 50
    penalty = len([c for c in class_metrics if class_metrics[c]['count'] == 0]) * 10
    return base + bonus - penalty

final_diagnostic = process_metrics(log_data, system_thresholds)
print(f"Target result: {final_diagnostic}")