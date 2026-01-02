from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [
    {'node': 'A', 'load': 78, 'errors': 2, 'temp': 67},
    {'node': 'B', 'load': 85, 'errors': 1, 'temp': 73},
    {'node': 'C', 'load': 92, 'errors': 4, 'temp': 81},
    {'node': 'A', 'load': 80, 'errors': 0, 'temp': 68},
    {'node': 'B', 'load': 87, 'errors': 3, 'temp': 75},
    {'node': 'C', 'load': 88, 'errors': 5, 'temp': 83},
    {'node': 'D', 'load': 95, 'errors': 8, 'temp': 89}
]

# Irrelevant helper function (decoy)
def calculate_health_score(metrics):
    return sum([m['load'] * 0.3 + m['temp'] * 0.2 for m in metrics]) / len(metrics)

# Unused error counter (red herring)
error_tally = defaultdict(int)
for entry in telemetry_stream:
    error_tally[entry['node']] += entry['errors']

# Misleading intermediate transformation (dead path)
decoy_aggregation = {}
for entry in telemetry_stream:
    node = entry['node']
    if node not in decoy_aggregation:
        decoy_aggregation[node] = {'peak_load': 0, 'total_errors': 0}
    decoy_aggregation[node]['peak_load'] = max(decoy_aggregation[node]['peak_load'], entry['load'])
    decoy_aggregation[node]['total_errors'] += entry['errors']

# Real processing begins here
log_data = defaultdict(list)
for record in telemetry_stream:
    log_data[record['node']].append(record['load'])

# Secondary distractor: frequency analysis of error counts (unused)
error_counts = [r['errors'] for r in telemetry_stream]
error_frequency = Counter(error_counts)

# Another red herring: temperature trend analysis
temp_history = []
for record in sorted(telemetry_stream, key=lambda x: x['temp']):
    temp_history.append(record['temp'] * 0.8 + 20)  # fake normalization

# Actual signal extraction
stable_nodes = []
fluctuation_index = {}
for node, loads in log_data.items():
    avg_load = sum(loads) / len(loads)
    variance = sum((x - avg_load) ** 2 for x in loads) / len(loads)
    fluctuation_index[node] = round(math.sqrt(variance), 3)
    if variance < 25 and avg_load < 90:
        stable_nodes.append(node)

# Fake risk scoring (looks important but unused)
risk_profile = {}
for node in log_data:
    base_risk = fluctuation_index.get(node, 0) * 1.5
    if node == 'D':
        base_risk += 10
    risk_profile[node] = round(base_risk, 2)

# Core logic buried under distractions
system_threshold = 1.8
def process_metrics(data_dict, threshold):
    result_set = []
    for key, values in data_dict.items():
        mean_val = sum(values) / len(values)
        # Key operation: normalized stability score
        stability_score = (mean_val / (fluctuation_index[key] + 1))
        result_set.append(stability_score)
    
    # Critical computation hidden in middle of logic chain
    aggregate_stability = sum(result_set) / len(result_set)
    penalty_factor = 0
    if 'D' in data_dict and fluctuation_index.get('D', 0) > threshold:
        penalty_factor = 15
    
    # Secondary adjustment based on count
    size_modifier = len(data_dict) % 7

    # Final diagnostic calculation (main answer path)
    final_score = (aggregate_stability * 10) - penalty_factor + size_modifier

    # Dead branch: never executed due to fixed condition
    if False and len(stable_nodes) > 10:
        fallback = sum(fluctuation_index.values())
        return fallback
        
    return round(final_score, 4)

# Execution point of interest
final_diagnostic = process_metrics(log_data, system_threshold)

# Noise: unused statistical summary
diagnostic_stats = {
    'max_fluctuation': max(fluctuation_index.values()),
    'min_stable': min([v for k, v in risk_profile.items() if k in stable_nodes], default=0),
    'node_count': len(log_data)
}

# Target result output
print(f"Result: {final_diagnostic}")