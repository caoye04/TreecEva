import math

# Simulated network node states over time
node_status = {
    'node_alpha': [1, 1, 0, 1, 1],
    'node_beta': [1, 0, 0, 1, 0],
    'node_gamma': [0, 1, 1, 1, 1],
    'node_delta': [1, 1, 1, 0, 1]
}

# System thresholds and calibration data (mostly irrelevant)
calibration_coefficients = [0.98, 1.02, 0.99, 1.01, 0.97]
dummy_weights = {'w1': 0.5, 'w2': 0.3, 'w3': 0.2}  # Unused in final calculation

# Historical uptime records (distractor)
historical_uptime = {
    'Q1': 99.2,
    'Q2': 98.7,
    'Q3': 99.5,
    'Q4': 96.4
}

# Irrelevant string processing for log sanitization (red herring)
def sanitize_log_entry(entry):
    return entry.strip().lower().replace('_', '-').replace(' ', '')

log_entries = ['ERROR_CRITICAL', 'warning_pending', 'INFO_OK']
sanitized_logs = [sanitize_log_entry(log) for log in log_entries]

# Real computation begins: construct state transition log
network_state_log = []
for node, states in node_status.items():
    active_transitions = 0
    for i in range(1, len(states)):
        if states[i-1] == 0 and states[i] == 1:
            active_transitions += 1
    network_state_log.append(active_transitions)

# Secondary metric: total downtime events
downtime_events = {}
for node, states in node_status.items():
    down_count = 0
    for i in range(len(states)):
        if states[i] == 0:
            down_count += 1
    downtime_events[node] = down_count

# Health score based on transitions (used)
basic_health_index = sum(network_state_log)

# Complex decoy structure: entropy calculation (unused)
from collections import Counter
def calculate_entropy(lst):
    counts = Counter(lst)
    total = len(lst)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

transition_entropy = calculate_entropy(network_state_log)  # Computed but unused

# System health as conditional expression (used in final result)
system_health = 75 if basic_health_index >= 3 else 60

# Phantom function: looks important but does nothing relevant
def compute_latency_jitter(timestamps):
    if len(timestamps) < 2:
        return 0.0
    jitters = [abs(timestamps[i] - timestamps[i-1]) for i in range(1, len(timestamps))]
    return sum(jitters) / len(jitters) if jitters else 0.0

# Unused timestamp simulation
timestamp_sequence = [100, 105, 112, 114, 120]
jitter_score = compute_latency_jitter(timestamp_sequence)  # Dead computation

# Anomaly detection with bit manipulation red herring
def detect_anomalies_bitwise(state_list):
    # This function is called but only uses simple logic, despite bitwise appearance
    packed = 0
    for s in state_list:
        packed = (packed << 1) | s
    # The following line computes something but is ignored
    parity_check = bin(packed).count('1') % 2
    return 5 if parity_check == 1 else 10  # Distracting return pattern

# Another dead path: unused analysis
consistency_flag = True
for node, states in node_status.items():
    if len(set(states)) == 1:
        consistency_flag = False

# Actual anomaly score computed simply
anomaly_score = 0
for log in network_state_log:
    if log > 1:
        anomaly_score += 2

# Decoy dictionary operation (looks like fusion but unused)
fused_diagnostics = {
    'entropy': round(transition_entropy, 3),
    'jitter': round(jitter_score, 3),
    'consistency': consistency_flag,
    'calibrated_health': system_health * 1.05
}

# Core aggregation function used in final answer
def aggregate_metrics(transitions, health):
    base = sum(transitions)
    adjustment = 5 if health >= 70 else -5
    return base * 10 + adjustment

# Critical statement
final_diagnostic = aggregate_metrics(network_state_log, system_health) + anomaly_score

print(f"Result: {final_diagnostic}")