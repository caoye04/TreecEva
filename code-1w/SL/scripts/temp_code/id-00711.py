import math

# Simulated network telemetry data
telemetry_logs = [
    {'node': 'A1', 'latency': 45, 'packet_loss': 0.02, 'throughput': 870},
    {'node': 'B2', 'latency': 120, 'packet_loss': 0.08, 'throughput': 320},
    {'node': 'C3', 'latency': 67, 'packet_loss': 0.01, 'throughput': 910},
    {'node': 'D4', 'latency': 200, 'packet_loss': 0.15, 'throughput': 180},
    {'node': 'E5', 'latency': 52, 'packet_loss': 0.03, 'throughput': 790}
]

# Irrelevant auxiliary data (distractor)
legacy_system_flags = [True, False, True, True]
cached_checksums = {i: hash(str(i)) % 1000 for i in range(10)}
temporary_buffer = ''.join([chr(97 + (i % 26)) for i in range(50)])

# Data transformation pipeline
normalized_nodes = []
for entry in telemetry_logs:
    normalized = {
        'id': entry['node'],
        'response_score': 100 * math.exp(-entry['latency'] / 100),
        'integrity_weight': 1 - entry['packet_loss'],
        'efficiency_factor': entry['throughput'] / 1000,
        'overall_node_rank': 0  # placeholder
    }
    # Compute composite node metric
    raw_composite = (
        normalized['response_score'] * 0.4 +
        normalized['integrity_weight'] * 30 +
        normalized['efficiency_factor'] * 50
    )
    normalized['overall_node_rank'] = round(raw_composite, 2)
    normalized_nodes.append(normalized)

# Secondary irrelevant processing (red herring)
duplicate_tracker = {}
for char in temporary_buffer:
    duplicate_tracker[char] = duplicate_tracker.get(char, 0) + 1
redundant_frequency_list = sorted(duplicate_tracker.values(), reverse=True)[:10]

# Extract health indicators
system_health = []
def compute_stability_index(loss, latency):
    if loss > 0.1:
        return max(1.0 - loss * 10, 0.0)
    return 1.0 / (1.0 + latency / 200)

for log in telemetry_logs:
    stability = compute_stability_index(log['packet_loss'], log['latency'])
    performance_ratio = log['throughput'] / (log['latency'] + 1)
    health_score = stability * 0.7 + (performance_ratio / 10) * 0.3
    system_health.append({'node': log['node'], 'score': round(health_score, 3)})

# Network state classification (partially dead logic path)
network_states = []
for node in normalized_nodes:
    rank = node['overall_node_rank']
    if rank > 80:
        state = 'OPTIMAL'
    elif rank > 50:
        state = 'STABLE'
    elif rank > 30:
        state = 'DEGRADED'
    else:
        state = 'CRITICAL'
    
    # Unused computed field (decoy)
    node['diagnostic_flag'] = sum([ord(c) for c in node['id']]) % 7
    
    network_states.append({'node': node['id'], 'state': state})

# Unused function - red herring
def forecast_failure_risk(history):
    trend_line = [h['latency'] for h in history[-3:]]
    growth_rate = (trend_line[2] - trend_line[0]) / 2
    risk_metric = 0.1 * growth_rate + 0.05 * history[-1]['packet_loss']
    return min(max(risk_metric, 0), 1)

# Misleading intermediate aggregation (irrelevant)
avg_latency = sum([log['latency'] for log in telemetry_logs]) / len(telemetry_logs)
weighted_loss = sum([log['packet_loss'] * (log['throughput'] / 100) for log in telemetry_logs])
phantom_metric = avg_latency * weighted_loss / 10

# Core diagnostic logic - relevant path
def aggregate_metrics(states, health_probes):
    severity_map = {'OPTIMAL': 0, 'STABLE': 1, 'DEGRADED': 3, 'CRITICAL': 7}
    total_risk = 0
    total_health = 0.0
    
    for state_info in states:
        total_risk += severity_map[state_info['state']]
    
    for probe in health_probes:
        total_health += probe['score']
    
    # Final computation
    base_diagnostic = total_risk * 100
    adjustment_factor = int(round(total_health))
    final_score = base_diagnostic - adjustment_factor * 5
    
    # This is the actual answer variable
    return final_score

# Execution point of interest
final_diagnostic = aggregate_metrics(network_states, system_health)

# Print result as required
print(f"Target result: {final_diagnostic}")