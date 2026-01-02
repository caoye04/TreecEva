def analyze_node(traffic, threshold=100):
    return 'stable' if sum(traffic) < threshold else 'unstable'


def compute_health_score(metrics):
    base = metrics.get('latency', 0)
    jitter = metrics.get('jitter', 0)
    packet_loss = metrics.get('packet_loss', 0)
    score = 100 - base - (jitter * 2) - (packet_loss * 5)
    return max(score, 0)


def transform_data(raw_data):
    # Irrelevant transformation chain
    temp_a = [x ** 0.5 for x in raw_data if x > 10]
    temp_b = [y + 10 for y in temp_a if y < 20]
    processed = [z * 1.5 for z in temp_b]
    return processed if len(processed) > 3 else [0] * 5

# Simulated network monitoring system
network_state = {
    'nodes': 15,
    'active_connections': 87,
    'bandwidth_utilization': [85, 90, 76, 95, 67],
    'security_events': set(),
    'last_sync': '2023-10-05T14:30:00Z'
}

diagnostics_log = [
    {'node_id': 1, 'latency': 12, 'jitter': 3, 'packet_loss': 1, 'traffic': [95, 87, 102]},
    {'node_id': 2, 'latency': 8, 'jitter': 1, 'packet_loss': 0, 'traffic': [45, 67, 54]},
    {'node_id': 3, 'latency': 20, 'jitter': 5, 'packet_loss': 2, 'traffic': [110, 115, 98]},
    {'node_id': 4, 'latency': 15, 'jitter': 2, 'packet_loss': 1, 'traffic': [76, 88, 91]},
    {'node_id': 5, 'latency': 5, 'jitter': 0, 'packet_loss': 0, 'traffic': [30, 40, 35]}
]

# Dead code path - never called
def deprecated_analysis(data):
    cumulative = 0
    for item in data:
        if isinstance(item, dict) and 'value' in item:
            cumulative += item['value'] ** 2
    return cumulative // 3 if cumulative > 0 else 0

# Unused auxiliary variables - red herrings
baseline_profile = {'throughput': 950, 'error_rate': 0.01, 'uptime': 99.97}
config_override = {k: v * 1.1 for k, v in baseline_profile.items() if isinstance(v, float)}
shadow_buffer = [i * 0.01 for i in range(100)]

# Distractor computation - looks important but unused
redundant_aggregation = 0
for entry in diagnostics_log:
    redundant_aggregation += entry.get('latency') // 2
    redundant_aggregation -= entry.get('packet_loss')

# Conditional expression with real and fake logic branches
is_peak_hour = False
scaling_factor = 1.25 if is_peak_hour else 0.85

# Real processing begins here
health_scores = []
status_count = {'stable': 0, 'unstable': 0}

for log in diagnostics_log:
    score = compute_health_score(log)
    health_scores.append(score)
    
    node_status = analyze_node(log['traffic'])
    status_count[node_status] += 1

    # Embedded irrelevant bit manipulation
    mask = 0b1101
    masked_value = score & mask
    _ = masked_value << 2  # unused

# Secondary distractor: set operations that don't affect outcome
critical_nodes = set()
for i, s in enumerate(health_scores):
    if s < 70:
        critical_nodes.add(f'node_{i+1}')

all_nodes_set = {f'node_{i}' for i in range(1, 16)}
overlap_check = all_nodes_set.intersection(critical_nodes)
_ = len(overlap_check) * 10  # decoy usage

# Main aggregation logic
average_health = sum(health_scores) / len(health_scores)
stable_ratio = status_count['stable'] / len(diagnostics_log)

# Simulated diagnostic weightings (some are red herrings)
weights = {
    'health': 0.6,
    'stability': 0.3,
    'bandwidth': 0.1  # unused weight
}

# Real metric calculation
weighted_diagnostic = (average_health * weights['health'] + 
                        (stable_ratio * 100) * weights['stability'])

# Irrelevant bandwidth transformation
util_avg = sum(network_state['bandwidth_utilization']) / len(network_state['bandwidth_utilization'])
adjusted_util = util_avg * scaling_factor if util_avg > 80 else util_avg
_ = adjusted_util * 0.95  # unused adjustment

# Final data transformation with conditional expression
sanitized_scores = [s if s >= 50 else 50 for s in health_scores]
penalty_applied = len(health_scores) != len(sanitized_scores)

def aggregate_metrics(state, log):
    node_count = state['nodes']
    active_conn = state['active_connections']
    
    # Complex conditional expression combining multiple factors
    base_metric = (node_count * 10) + (active_conn * 2) - (util_avg * 1.5)
    
    # Multi-step reasoning: combine health, stability, and fake signal
    fake_signal = len(shadow_buffer) // 10  # 10, looks meaningful
    real_component = weighted_diagnostic * 0.7
    fake_component = fake_signal * 0.3  # misleading inclusion
    
    # Only real_component contributes - fake_component is neutralized
    adjusted_base = base_metric + real_component - fake_component + penalty_applied
    
    # Final nonlinear transformation
    final_score = int((adjusted_base ** 1.05) % 9997)
    
    # Key result stored here
    return final_score

# Execution point of interest
final_diagnostic = aggregate_metrics(network_state, diagnostics_log)
print(f"Result: {final_diagnostic}")