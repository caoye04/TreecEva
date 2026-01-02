import math

# Simulated network node health monitoring system with diagnostic metrics
node_registry = {'alpha': 1, 'beta': 2, 'gamma': 3, 'delta': 4}
initial_power_levels = [98, 76, 85, 91]
baseline_threshold = 80

# Irrelevant lookup table for deprecated systems
legacy_codes = {101: 'ERR_LEGACY', 102: 'TIMEOUT', 103: 'HANDSHAKE_FAIL'}
decoys = [x ** 2 for x in range(10)]  # Unused computation

# Node status classification (only some used)
def classify_node_status(power):
    if power > 90:
        return 'OPTIMAL'
    elif power > baseline_threshold:
        return 'STABLE'
    else:
        return 'CRITICAL'

def encrypt_id(node_id):
    # Unused cryptographic red herring
    return sum([ord(c) * (i + 1) for i, c in enumerate(node_id)]) % 1000

def generate_sequence(n):
    # Dead-end function: Fibonacci-like but unused
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

# Real processing begins here
power_map = {list(node_registry.keys())[i]: initial_power_levels[i] for i in range(4)}
status_catalog = {node: classify_node_status(power) for node, power in power_map.items()}

# Simulate time-series log with irrelevant fields
network_state_log = []
for t in range(5):
    entry = {}
    for node in node_registry.keys():
        # Simulate fluctuating signal (damped oscillation)
        base = power_map[node]
        variation = int(5 * math.sin(t / 2))
        new_power = base + variation
        entry[f'{node}_power'] = new_power
        entry[f'{node}_status'] = classify_node_status(new_power)
        # Add noise
        entry[f'{node}_latency_ms'] = 20 + (t % 3) * 5  # Irrelevant
        entry[f'{node}_retry_count'] = 0 if t % 3 != 2 else 1  # Distractor
    entry['timestamp'] = t * 1000
    entry['checksum'] = sum(v for k, v in entry.items() if 'power' in k) ^ 0xAB  # Partially misleading
    network_state_log.append(entry)

# Diagnostic engine (core logic)
critical_flags = 0
oscillation_score = 0
for entry in network_state_log:
    stable_count = 0
    for node in node_registry:
        p = entry[f'{node}_power']
        s = entry[f'{node}_status']
        if s == 'CRITICAL':
            critical_flags += 1
        if abs(p - power_map[node]) > 8:
            oscillation_score += 1
        if s == 'OPTIMAL':
            stable_count += 1
    entry['system_wide_stability'] = stable_count >= 2  # Not directly used

# Secondary metric: consistency across nodes
consistency_metric = 0
for i in range(1, len(network_state_log)):
    prev = network_state_log[i-1]
    curr = network_state_log[i]
    matching_states = 0
    for node in node_registry:
        if prev[f'{node}_status'] == curr[f'{node}_status']:
            matching_states += 1
    if matching_states >= 3:
        consistency_metric += 1

# Decoy aggregation (unused path)
avg_latency = 0
for entry in network_state_log:
    latencies = [entry[f'{node}_latency_ms'] for node in node_registry]
    avg_latency += sum(latencies) / len(latencies)
avg_latency /= len(network_state_log)

# Actual diagnostics calculation
def aggregate_metrics(log, extra=None):
    total_power = 0
    min_power = float('inf')
    critical_events = 0
    recovery_count = 0

    for entry in log:
        power_values = [entry[f'{node}_power'] for node in node_registry]
        total_power += sum(power_values)
        min_power = min(min_power, min(power_values))

        # Count transitions from CRITICAL to STABLE/OPTIMAL
        if len(log) > 1 and log.index(entry) > 0:
            prev = log[log.index(entry) - 1]
            for node in node_registry:
                prev_status = prev[f'{node}_status']
                curr_status = entry[f'{node}_status']
                if prev_status == 'CRITICAL' and curr_status in ['STABLE', 'OPTIMAL']:
                    recovery_count += 1

        # Count current critical nodes
        for node in node_registry:
            if entry[f'{node}_status'] == 'CRITICAL':
                critical_events += 1

    avg_power = total_power / (len(log) * len(node_registry))
    severity_penalty = critical_events * 10
    stability_index = int(avg_power - severity_penalty + recovery_count * 3)

    return {
        'total_power': total_power,
        'min_recorded_power': min_power,
        'critical_incidents': critical_events,
        'recoveries': recovery_count,
        'stability_index': stability_index,
        'consistency_ratio': consistency_metric / (len(log) - 1) if len(log) > 1 else 0
    }

diagnostics = aggregate_metrics(network_state_log)

# Final computation point
final_diagnostic = aggregate_metrics(network_state_log, diagnostics)['stability_index']
print(f"Result: {final_diagnostic}")