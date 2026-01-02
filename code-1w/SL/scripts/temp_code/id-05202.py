from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [
    {'node': 'A', 'load': 0.7, 'errors': 2, 'timestamp': 100},
    {'node': 'B', 'load': 0.9, 'errors': 5, 'timestamp': 101},
    {'node': 'A', 'load': 0.3, 'errors': 0, 'timestamp': 102},
    {'node': 'C', 'load': 0.95, 'errors': 8, 'timestamp': 103},
    {'node': 'B', 'load': 0.6, 'errors': 1, 'timestamp': 104}
]

# Irrelevant auxiliary mapping (distractor)
node_sectors = {'A': 'alpha', 'B': 'beta', 'C': 'gamma', 'D': 'delta'}
sector_priority = {'alpha': 3, 'beta': 2, 'gamma': 1}

# Misleading performance baseline (red herring)
baseline_error_rate = 3.5
adjustment_factor = 1.2
theoretical_capacity = sum([500 * (1 + 0.1 * i) for i in range(4)])  # Unused calculation

# Data aggregation with distractors
raw_logs = defaultdict(list)
error_counts = Counter()

for entry in telemetry_stream:
    raw_logs[entry['node']].append(entry['load'])
    error_counts[entry['node']] += entry['errors']

# Fake transformation chain (dead path)
transformed = list(map(lambda x: x * 1.5 if x < 0.5 else x * 0.9, [0.1, 0.8, 0.3]))
filtered_data = [x for x in transformed if x > 0.5]  # Computation not used later

# Decoy function that looks important but isn't called
def calculate_resilience_score(nodes):
    return sum([len(node) * 10 for node in nodes])

# Another decoy using bitwise (misdirection)
def assess_fault_tolerance(x, y):
    return (x ^ y) & 0xFF

# Real processing begins here
system_state = {
    'active_nodes': set(raw_logs.keys()),
    'peak_load': max([max(raw_logs[node]) for node in raw_logs]),
    'stability_ratio': len([l for l in raw_logs['A'] if l < 0.5]) / len(raw_logs['A']) if 'A' in raw_logs else 0
}

log_entries = []
for entry in telemetry_stream:
    # Compute diagnostic signature (some are distractions)
    sig = entry['load'] * 100
    flag = 1 if entry['errors'] > baseline_error_rate else 0
    checksum = int(sig) ^ entry['errors']  # Bitwise red herring
    priority = sector_priority.get(node_sectors[entry['node']], 0)  # Uses distractor map

    log_entries.append({
        'id': f"{entry['node']}-{entry['timestamp']}",
        'metric': sig,
        'flagged': bool(flag),
        'priority': priority,
        'checksum': checksum
    })

# Core logic disguised among noise
def analyze_stress_pattern(entries):
    high_stress = [e for e in entries if e['metric'] > 70]
    stress_sum = sum([e['metric'] for e in high_stress])
    count_A = sum([1 for e in high_stress if e['id'].startswith('A')])
    return stress_sum - 10 * count_A  # Key computation step 1

# Secondary analysis with conditional logic
def evaluate_recovery_indicators(entries):
    sorted_entries = sorted(entries, key=lambda x: x['metric'], reverse=True)
    top_three = sorted_entries[:3]
    recovery_score = 0
    for item in top_three:
        if not item['flagged']:
            recovery_score += item['metric'] / 25
        else:
            recovery_score -= 5
    return math.floor(recovery_score)  # Key computation step 2

# Main processing function combining multiple concepts
def process_metrics(logs, state):
    # Step 1: Aggregate priority-weighted anomalies
    anomalies = [log for log in logs if log['flagged']]
    weighted_anomalies = sum([a['metric'] * (a['priority'] + 1) for a in anomalies])

    # Step 2: Compute temporal instability index
    timestamps = [t['timestamp'] for t in telemetry_stream]
    instability_index = max(timestamps) - min(timestamps)  # 103 - 100 = 3

    # Step 3: Combine with logical conditions
    critical_load = state['peak_load'] > 0.85
    sufficient_stability = state['stability_ratio'] > 0.4

    # Step 4: Complex conditional expression
    base_score = analyze_stress_pattern(logs)
    recovery_bonus = evaluate_recovery_indicators(logs)

    # Step 5: Final composition with modular arithmetic
    temp_result = (base_score + recovery_bonus) % 1000
    if critical_load and not sufficient_stability:
        temp_result *= 2
    elif not critical_load:
        temp_result += 50

    # Step 6: Apply anomaly weighting only if conditions met
    if len(anomalies) > 1:
        temp_result += int(weighted_anomalies // 10)

    # Step 7: Final adjustment using bit manipulation (actually relevant)
    final_value = temp_result ^ instability_index  # XOR with 3

    # Step 8: Correction factor based on node diversity
    node_count = len(state['active_nodes'])
    final_value = final_value + (node_count * 7)

    return final_value

# Execute main logic
diagnostic_trace = [entry for entry in log_entries if entry['priority'] > 0]
system_health_map = {node: sum(raw_logs[node]) for node in raw_logs}  # Unused

# Critical execution point
final_diagnostic = process_metrics(log_entries, system_state)

# Output result
print(f"Result: {final_diagnostic}")