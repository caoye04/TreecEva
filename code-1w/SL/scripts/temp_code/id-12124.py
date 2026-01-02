from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [
    {'node': 'A', 'load': 78, 'temp': 65, 'errors': 2, 'uptime': 420},
    {'node': 'B', 'load': 85, 'temp': 73, 'errors': 1, 'uptime': 380},
    {'node': 'A', 'load': 60, 'temp': 59, 'errors': 0, 'uptime': 425},
    {'node': 'C', 'load': 92, 'temp': 81, 'errors': 5, 'uptime': 200},
    {'node': 'B', 'load': 77, 'temp': 69, 'errors': 0, 'uptime': 390},
    {'node': 'C', 'load': 88, 'temp': 77, 'errors': 3, 'uptime': 210},
    {'node': 'A', 'load': 83, 'temp': 68, 'errors': 1, 'uptime': 430}
]

# Irrelevant auxiliary mapping (distractor)
node_locations = {'A': 'Zone-1', 'B': 'Zone-3', 'C': 'Zone-2'}
location_priority = {'Zone-1': 2, 'Zone-2': 1, 'Zone-3': 3}

# System thresholds for health check (relevant)
system_thresholds = {
    'max_load': 80,
    'max_temp': 70,
    'max_errors_per_hour': 4,
    'min_uptime': 300
}

# Aggregation structures (mixed relevance)
node_aggregates = defaultdict(lambda: defaultdict(list))
error_logs = []
node_downtime = {}  # Unused distractor

# Process raw stream into node-based time series
for entry in telemetry_stream:
    node = entry['node']
    for k, v in entry.items():
        node_aggregates[node][k].append(v)

# Compute derived metrics (some relevant, some not)
derived_stats = {}
consistency_flags = []

for node, metrics in node_aggregates.items():
    load_avg = sum(metrics['load']) / len(metrics['load'])
    temp_peak = max(metrics['temp'])
    total_errors = sum(metrics['errors'])
    uptime_initial = metrics['uptime'][0]
    error_rate = total_errors / (len(metrics['uptime']) * 0.25)  # per hour

    # Health flags with nested logic
    load_flag = 'over' if load_avg > system_thresholds['max_load'] else 'normal'
    temp_flag = 'over' if temp_peak > system_thresholds['max_temp'] else 'normal'
    error_flag = 'over' if error_rate > system_thresholds['max_errors_per_hour'] else 'normal'

    # Diagnostic score (core computation path)
    base_score = 100
    if load_flag == 'over': base_score -= 25
    if temp_flag == 'over': base_score -= 20
    if error_flag == 'over': base_score -= 30
    if metrics['uptime'][0] < system_thresholds['min_uptime']: base_score -= 25

    # Distractor: Consistency analysis (unused)
    load_variance = max(metrics['load']) - min(metrics['load'])
    if load_variance > 20:
        consistency_flags.append(f'{node}_unstable')

    derived_stats[node] = {
        'score': base_score,
        'load_status': load_flag,
        'temp_status': temp_flag,
        'error_rate': round(error_rate, 2),
        'final_uptime': metrics['uptime'][-1]
    }

# Secondary transformation layer (relevant)
log_data = []
for record in telemetry_stream:
    # Conditional expression used
    status = 'critical' if record['load'] > 90 or record['errors'] > 4 else 'warning' if record['load'] > 80 or record['errors'] > 0 else 'normal'
    log_data.append({
        'id': f"{record['node']}-{len(log_data)}",
        'level': status,
        'metrics': record
    })

# Decoy function - never called (dead code path)
def analyze_downtime(nodes):
    results = {}
    for n in nodes:
        results[n] = math.sin(len(nodes) * 0.1)
    return results

# Another decoy: unused summary
aggregated_errors = Counter([entry['node'] for entry in telemetry_stream if entry['errors'] > 0])
peak_load_node = max(derived_stats.keys(), key=lambda x: derived_stats[x]['score'])  # Misleading: uses inverse logic

# Core processing function with multiple concepts
def process_metrics(logs, thresholds):
    node_impact = defaultdict(int)
    severity_counts = {'critical': 0, 'warning': 0, 'normal': 0}

    for log in logs:
        node = log['metrics']['node']
        load = log['metrics']['load']
        errors = log['metrics']['errors']
        level = log['level']

        severity_counts[level] += 1

        impact = 0
        if level == 'critical':
            impact += 50
        elif level == 'warning':
            impact += 20
        
        if load > thresholds['max_load']:
            impact += 10
        
        if errors > 0:
            impact += 5 * errors

        node_impact[node] += impact

    # Compute weighted diagnostic index
    total_severity = (
        severity_counts['critical'] * 10 + 
        severity_counts['warning'] * 3 + 
        severity_counts['normal'] * 0
    )
    
    # Final aggregation using min/max/average
    impacts = list(node_impact.values())
    if impacts:
        avg_impact = sum(impacts) / len(impacts)
        peak_impact = max(impacts)
        normalized = (avg_impact * 0.7) + (peak_impact * 0.3)
    else:
        normalized = 0

    # Final diagnostic calculation
    baseline = 200
    adjustment = math.log(total_severity + 1) * 15 if total_severity > 0 else 0
    penalty = min(normalized, 100)  # Capped impact penalty
    
    # Key statement
    final_diagnostic = int(baseline - adjustment - penalty)

    return final_diagnostic

# Execute main computation
final_diagnostic = process_metrics(log_data, system_thresholds)

# Print result as required
print(f"Target result: {final_diagnostic}")