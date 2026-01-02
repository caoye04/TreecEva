import math

# Simulated network and system diagnostic tool with heavy distractions
def analyze_packet_flow(bandwidth, latency, jitter):
    if bandwidth <= 0:
        return 0
    performance_index = (bandwidth / (latency + 1)) * (100 - jitter)
    adjustment_factor = 1.5 if jitter > 15 else 0.8
    return int(performance_index * adjustment_factor)

# Irrelevant helper function — dead code path
def legacy_checksum(data_str):
    checksum = 0
    for c in data_str:
        checksum ^= ord(c)
    return checksum

def evaluate_system_stability(cpu_load, memory_pressure, disk_io):
    stress_metric = cpu_load * 1.2 + memory_pressure * 0.8 + disk_io * 0.5
    stability_score = 100 - min(stress_metric, 95)
    return stability_score

# Unused but plausible-looking function
def deprecated_normalization(x, y):
    if y == 0:
        return 0
    return (x - y) / y

# Core data structures
network_state_log = {
    'nodes': 12,
    'active_sessions': 347,
    'packet_loss_rate': 2.3,
    'retransmission_count': 18,
    'flow_analysis': analyze_packet_flow(95, 14, 12)
}

system_health = [
    {'metric': 'cpu', 'value': 68, 'weight': 0.35},
    {'metric': 'memory', 'value': 74, 'weight': 0.40},
    {'metric': 'disk', 'value': 52, 'weight': 0.25}
]

# Distractor variables — look relevant but aren't used in final result
temporal_factor = 0.91
phase_shift = math.sin(math.pi / 6)  # unused
baseline_reference = sum([h['value'] for h in system_health])  # misleading intermediate

# Simulate a security audit with red herring logic
security_flags = [True, False, True, True]
audit_weighting = [0.2, 0.1, 0.4, 0.3]
security_audit_score = 0
for i in range(len(security_flags)):
    if security_flags[i]:
        security_audit_score += audit_weighting[i] * 100

# Decoy accumulation — looks important but unused
shadow_accumulator = 0
for key in network_state_log:
    if isinstance(network_state_log[key], int):
        shadow_accumulator += network_state_log[key] * 0.1

# Conditional expression used appropriately
health_sum = sum(h['value'] * h['weight'] for h in system_health)
adjusted_health = health_sum if health_sum < 80 else 80 - (health_sum - 80) * 0.2

# Complex dictionary transformation — actually contributes
transformed_log = {
    'efficiency': network_state_log['flow_analysis'] * 0.75,
    'penalty': network_state_log['packet_loss_rate'] * 5,
    'bonus': 10 if network_state_log['retransmission_count'] < 20 else 0
}

# Real computation chain
base_diagnostic = transformed_log['efficiency'] - transformed_log['penalty'] + transformed_log['bonus']

# Summation over filtered set
recent_events = {1: 'ok', 2: 'ok', 3: 'error', 4: 'pending', 5: 'ok'}
event_severity_map = {'ok': 0, 'error': 5, 'pending': 2}
event_risk_total = sum(event_severity_map[status] for status in recent_events.values() if status in event_severity_map)

# Actual aggregation function used in answer
def aggregate_metrics(log, health):
    flow = log['efficiency']
    penalty = log['penalty']
    bonus = log['bonus']
    health_component = evaluate_system_stability(health[0]['value'], health[1]['value'], health[2]['value'])
    return int(flow - penalty + bonus + health_component)

# Key execution point
final_diagnostic = aggregate_metrics(network_state_log, system_health) + security_audit_score

# Print result as required
print(f"Result: {final_diagnostic}")