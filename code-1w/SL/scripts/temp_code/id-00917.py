from collections import defaultdict, Counter
import math

# Simulated system performance metrics (some are red herrings)
telemetry_data = [
    {'cpu': 75, 'mem': 80, 'disk_r': 40, 'disk_w': 60, 'net_in': 30, 'net_out': 35},
    {'cpu': 80, 'mem': 82, 'disk_r': 45, 'disk_w': 65, 'net_in': 33, 'net_out': 37},
    {'cpu': 90, 'mem': 85, 'disk_r': 50, 'disk_w': 70, 'net_in': 36, 'net_out': 40},
    {'cpu': 60, 'mem': 70, 'disk_r': 55, 'disk_w': 75, 'net_in': 39, 'net_out': 45}
]

# Irrelevant historical logs (distractor data)
historical_logs = [
    {'timestamp': '2023-01-01', 'event': 'startup', 'code': 200},
    {'timestamp': '2023-01-02', 'event': 'reboot', 'code': 500}
]

# Extract recent metrics (only CPU and memory are actually used)
recent_metrics = [m for m in telemetry_data if m['cpu'] > 70]

# Dead code path: unused function (misleading)
def analyze_network_efficiency(data):
    total = 0
    for entry in data:
        total += (entry['net_in'] + entry['net_out']) / 2
    return total / len(data) if data else 0

# Unused transformation (red herring)
normalized_telemetry = [
    {k: v / 100 for k, v in row.items()} for row in telemetry_data
]

# Aggregate metrics per component (but only CPU and MEM matter)
aggregated = defaultdict(float)
for entry in recent_metrics:
    for k, v in entry.items():
        aggregated[k] += v / len(recent_metrics)

# Decoy calculation: network health (never used)
network_health = (aggregated['net_in'] + aggregated['net_out']) / 2

# Only these two metrics are actually used in final computation
metrics = {
    'cpu_load': aggregated['cpu'],
    'memory_usage': aggregated['mem']
}

# Weight configuration (weights for unused dimensions are distractions)
weights = {
    'cpu_load': 0.45,
    'memory_usage': 0.35,
    'disk_risk': 0.1,  # unused
    'network_stability': 0.1  # unused
}

# Fake risk scoring (dead code)
def calculate_disk_risk(disk_read, disk_write):
    return math.log(disk_read * disk_write + 1) / 10

# Real evaluation logic buried among noise
def evaluate_performance(perf_metrics, weight_map):
    score = 0.0
    # Only cpu_load and memory_usage contribute
    score += perf_metrics['cpu_load'] * weight_map['cpu_load']
    score += perf_metrics['memory_usage'] * weight_map['memory_usage']
    
    # Red herring: attempt to use other weights but no data provided
    if 'disk_risk' in weight_map and 'disk_r' in aggregated:
        score += weight_map['disk_risk'] * 50  # never executed
    
    # Additional distraction: sorting irrelevant keys
    irrelevant_keys = sorted([k for k in weight_map.keys() if 'disk' in k or 'network' in k])
    penalty = 0.5 * len(irrelevant_keys)  # calculated but not used
    
    # Final adjustment based on logical condition (hidden key step)
    if perf_metrics['cpu_load'] > 80 and perf_metrics['memory_usage'] > 80:
        score *= 1.1  # performance bonus
    else:
        score *= 0.95  # slight penalty
    
    return score

# Execution point of interest
final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Target result: {final_score}")