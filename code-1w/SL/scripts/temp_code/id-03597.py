def analyze_subsystem_integrity(raw_signals, baseline):
    signal_power = sum(abs(x) for x in raw_signals)
    noise_floor = max(raw_signals) * 0.1
    return (signal_power - noise_floor) > baseline


def compute_entropy(data_stream):
    from collections import Counter
    counts = Counter(data_stream)
    total = len(data_stream)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Non-standard pseudo-entropy
    return round(entropy, 4)

# Simulated telemetry data
sensor_readings = [0.88, -0.45, 0.92, 0.11, -0.67, 0.34, -0.22, 0.76]
diagnostic_codes = {101: 'OK', 102: 'STANDBY', 105: 'CALIBRATING'}
system_uptime = 14285
maintenance_cycle = system_uptime % 720

# Irrelevant health indicators
battery_level = 87
temperature_k = 301
cpu_load_history = [0.21, 0.33, 0.41, 0.29, 0.52]

# Core state tracking
network_state_log = {
    'nodes_active': 7,
    'sync_epoch': 1699902845,
    'latency_spikes': [12, 8, 15],
    'checksum_validations': ['a8c3', 'd9e1', 'a8c3', 'f2b4']
}

# Data structure manipulation with distractors
unique_checksums = len(set(network_state_log['checksum_validations']))
mode_switch = 'high_throughput' if network_state_log['nodes_active'] > 5 else 'low_latency'

# Red herring computation
theoretical_bandwidth = 10 ** (network_state_log['nodes_active'] // 2)
efficiency_ratio = (unique_checksums * 10) / (network_state_log['nodes_active'] + 1)

# System health assessment using conditional expressions
recent_latency_avg = sum(network_state_log['latency_spikes']) / len(network_state_log['latency_spikes'])
system_health = {
    'stable': recent_latency_avg < 12,
    'redundancy': network_state_log['nodes_active'] >= 6,
    'consistency': unique_checksums >= 3
}

overall_stability_score = 1 if system_health['stable'] else 0
redundancy_flag = 1 if system_health['redundancy'] else 0
consistency_metric = 1 if system_health['consistency'] else 0

# Decoy function - never called
def trigger_recalibration(seq):
    return [x ^ 7 for x in seq if x % 3 == 0]

# Another dead function path
def validate_handshake(protocol_id):
    return protocol_id in [0x1A, 0x2C, 0x3F]

# Misleading intermediate calculation
projected_downtime = (system_uptime * 0.001) ** 2
scheduled_maintenance_window = projected_downtime > 0.5

# Conditional expression with nested logic
health_index = 3 if system_health['stable'] and system_health['redundancy'] else (2 if system_health['stable'] else 1)

# Bitwise obfuscation layer (distraction)
encoded_status = (health_index << 2) ^ 0x5A
status_check_result = (encoded_status & 0xFF) == 0x7B

# Actual relevant metric aggregation
base_metric = network_state_log['nodes_active'] * 100
latency_penalty = 30 if not system_health['stable'] else 0
consistency_bonus = 50 if system_health['consistency'] else 0

# Core transformation - looks similar to distractors but is critical
def aggregate_metrics(state, health_profile):
    base = state['nodes_active'] * 100
    penalty = 0
    if not health_profile['stable']:
        penalty += 30
    if not health_profile['redundancy']:
        penalty += 20
    bonus = 50 if health_profile['consistency'] else 0
    return base - penalty + bonus

# Secondary adjustment based on entropy-like measure
traffic_pattern = [1, 1, 0, 1, 0, 0, 1, 1, 1, 0]
entropy_measure = compute_entropy(traffic_pattern)

corrective_adjustment = int((0.5 - entropy_measure) * 100)

# Final diagnostic depends on both aggregate_metrics and corrective_adjustment
final_diagnostic = aggregate_metrics(network_state_log, system_health) + corrective_adjustment

# Output the result as required
print(f"Result: {final_diagnostic}")