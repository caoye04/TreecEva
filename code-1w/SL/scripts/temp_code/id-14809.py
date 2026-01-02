from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [
    {'node': 'A', 'load': 78, 'temp': 65, 'errors': 2, 'timestamp': 1001},
    {'node': 'B', 'load': 85, 'temp': 70, 'errors': 1, 'timestamp': 1002},
    {'node': 'A', 'load': 90, 'temp': 68, 'errors': 0, 'timestamp': 1003},
    {'node': 'C', 'load': 40, 'temp': 50, 'errors': 0, 'timestamp': 1004},
    {'node': 'B', 'load': 95, 'temp': 75, 'errors': 3, 'timestamp': 1005},
    {'node': 'C', 'load': 30, 'temp': 45, 'errors': 1, 'timestamp': 1006},
    {'node': 'A', 'load': 82, 'temp': 66, 'errors': 0, 'timestamp': 1007}
]

# Irrelevant auxiliary function (decoy)
def analyze_bandwidth(data):
    total = 0
    for entry in data:
        if 'bandwidth' in entry:
            total += entry['bandwidth']
    return total

# Misleading preprocessing step (dead path)
preprocessed_flags = []
for item in telemetry_stream:
    flag = (item['load'] > 80) << 1 | (item['temp'] > 60)
    preprocessed_flags.append(flag)

# Unused statistical counters (distractor variables)
load_variance_tracker = defaultdict(float)
error_burst_count = 0
for i in range(1, len(telemetry_stream)):
    prev, curr = telemetry_stream[i-1], telemetry_stream[i]
    if curr['errors'] > prev['errors']:
        error_burst_count += 1
    load_variance_tracker[curr['node']] += (curr['load'] - 70) ** 2

# Core aggregation logic
def aggregate_node_metrics(stream):
    node_stats = defaultdict(lambda: {'total_load': 0, 'high_temp_count': 0, 'critical_events': 0})
    node_sequence = []
    
    for record in stream:
        node_id = record['node']
        node_stats[node_id]['total_load'] += record['load']
        if record['temp'] > 60:
            node_stats[node_id]['high_temp_count'] += 1
        if record['load'] > 85 and record['errors'] > 0:
            node_stats[node_id]['critical_events'] += 1
        node_sequence.append(node_id)
    
    # Compute transition entropy (unused but plausible)
    transitions = Counter(zip(node_sequence, node_sequence[1:]))
    total_transitions = sum(transitions.values())
    entropy = 0.0
    for count in transitions.values():
        p = count / total_transitions
        entropy -= p * math.log2(p) if p > 0 else 0
    
    return node_stats

# Secondary transformation with red herring output
def compute_efficiency_score(metrics_dict):
    score = 0
    for node, data in metrics_dict.items():
        raw_score = data['total_load']
        if data['high_temp_count'] > 0:
            raw_score *= 0.9
        if data['critical_events'] > 0:
            raw_score *= 0.8
        score += raw_score
    efficiency_ratio = score / (len(metrics_dict) or 1)
    return efficiency_ratio  # Not used in final answer

# Data restructuring for no purpose (distractor)
restructured_map = {}
for entry in telemetry_stream:
    ts = entry['timestamp']
    restructured_map[ts] = {k: v for k, v in entry.items() if k != 'timestamp'}

# Log compression simulation (irrelevant)
compressed_size = 0
for key in restructured_map:
    compressed_size ^= key  # Bitwise decoy
    for val in restructured_map[key].values():
        if isinstance(val, int):
            compressed_size += val % 7

# Actual signal extraction path
def extract_anomaly_pattern(stream):
    pattern_code = 0
    last_critical_node = ''
    critical_times = []
    
    for r in stream:
        if r['load'] > 85 and r['temp'] > 60:
            pattern_code += r['load'] * 3
            last_critical_node = r['node']
            critical_times.append(r['timestamp'])
    
    # Inject fake dependency
    if last_critical_node:
        pattern_code += ord(last_critical_node) - ord('A')
    
    return pattern_code, critical_times

# Main processing function
def process_metrics(log_data, threshold):
    aggregated = aggregate_node_metrics(log_data)
    efficiency = compute_efficiency_score(aggregated)  # Computed but unused
    
    # Real anomaly detection
    anomaly_code, timestamps = extract_anomaly_pattern(log_data)
    
    # Decoy calculation chain
    temporal_delta = 0
    if len(timestamps) > 1:
        temporal_delta = sum(
            timestamps[i+1] - timestamps[i] 
            for i in range(len(timestamps)-1)
        )
    
    # Core logic: weighted diagnostic code
    base_diagnostic = 0
    for node, stats in aggregated.items():
        contribution = stats['total_load']
        if stats['high_temp_count'] >= 2:
            contribution *= 1.2
        if node == 'B':
            contribution += 10  # Special adjustment
        base_diagnostic += int(contribution)
    
    # Final interference: modular adjustment based on anomaly
    if anomaly_code > 0:
        base_diagnostic = (base_diagnostic * 7) % 1000
        base_diagnostic += anomaly_code % 100
    
    # Actual final computation
    adjustment_factor = (threshold + 5) // 10
    final_value = base_diagnostic + adjustment_factor * 17
    
    return final_value

# Irrelevant global filter
system_nodes = set(entry['node'] for entry in telemetry_stream)
system_threshold = 92

# Dead computation branch
if 'D' not in system_nodes:
    shadow_metric = 0
    for t in telemetry_stream:
        shadow_metric += t['load'] ^ t['errors']

# Key execution point
final_diagnostic = process_metrics(telemetry_stream, system_threshold)
print(f"Target result: {final_diagnostic}")