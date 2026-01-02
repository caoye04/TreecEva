import math

# Simulated network node diagnostics with mixed data types and red herrings
def analyze_node_load(base_signal, interference_level):
    if base_signal <= 0:
        return 0.0
    signal_quality = math.log(base_signal + 1) / (interference_level + 1)
    normalized_load = min(signal_quality * 1.5, 100.0)
    return round(normalized_load, 2)

# Irrelevant helper: processes unused sensor type
def evaluate_thermal_flux(temp_seq):
    avg_temp = sum(temp_seq) / len(temp_seq)
    return avg_temp > 75.5

# Core system state tracker (only partially relevant)
network_state_log = {
    'node_a': {'signal': 42, 'ping_jitter': 18, 'active': True},
    'node_b': {'signal': 0, 'ping_jitter': 94, 'active': False},
    'node_c': {'signal': 15, 'ping_jitter': 51, 'active': True},
    'node_d': {'signal': 88, 'ping_jitter': 5, 'active': True}
}

# Misleading health matrix (partially unused)
system_health = {
    'bandwidth_util': 87.4,
    'latency_spike_count': 3,
    'redundancy_active': True,
    'last_failover_age': 12,
    'security_nonce': 5683  # decoy value
}

# Dead code path: never called but looks important
def trigger_system_audit():
    audit_id = hash('system_check_9') % 10000
    return audit_id

# Unused transformation: creates false dependency
temp_sensors = [68.2, 71.0, 79.8, 65.4]
thermal_alert = evaluate_thermal_flux(temp_sensors)

# Decoy calculation with plausible intermediate
baseline_offset = 0
for node_id, attrs in network_state_log.items():
    if attrs['ping_jitter'] > 50:
        baseline_offset += 3.5
    else:
        baseline_offset += 1.2

# Actual relevant computation chain starts here
active_node_count = 0
load_sum = 0.0
for node_id, attrs in network_state_log.items():
    if attrs['active']:
        active_node_count += 1
        load_sum += analyze_node_load(attrs['signal'], attrs['ping_jitter'])

average_load = load_sum / active_node_count if active_node_count else 0

# Secondary metric from system_health (only one field used)
if system_health['redundancy_active'] and system_health['latency_spike_count'] < 5:
    stability_bonus = 12.5
else:
    stability_bonus = -8.3

# Hidden correction factor based on dictionary keys
key_weight_total = 0
for key in network_state_log.keys():
    key_weight_total += ord(key[-1])  # 'a', 'b', 'c', 'd' -> 97, 98, 99, 100

corrective_factor = (key_weight_total // 10) - 29  # (97+98+99+100)=394 -> 394//10=39 -> 39-29=10

# Aggregate using only specific components (misleading prior calculations)
def aggregate_metrics(log_data, health_status):
    node_contributions = []
    for node_id, data in log_data.items():
        if data['active']:
            score = data['signal'] * 0.33
            jitter_penalty = data['ping_jitter'] * 0.1
            node_contributions.append(score - jitter_penalty)
    raw_metric = sum(node_contributions)
    return int(raw_metric)  # truncates to integer

# Key execution point
final_diagnostic = aggregate_metrics(network_state_log, system_health) + corrective_factor

# Irrelevant post-processing (dead end)
if final_diagnostic > 50:
    final_diagnostic = math.sqrt(final_diagnostic) * 1.1

# Output result as required
print(f"Target result: {final_diagnostic}")