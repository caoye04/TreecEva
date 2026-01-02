def analyze_node_health(node_data):
    # Irrelevant transformation
    temp_score = sum([v ** 0.5 for v in node_data.values() if v > 5])
    adjusted = {k: v * 1.1 for k, v in node_data.items()}
    # Actual relevant logic
    healthy_count = len([v for v in adjusted.values() if v < 10])
    return healthy_count > 3

# Misleading diagnostic function (never called)
def legacy_diagnostic(nodes):
    return sum(hash(n) % 10 for n in nodes) // len(nodes)

# Unused helper
def normalize_vector(vec):
    mag = sum(x**2 for x in vec) ** 0.5
    return [x / mag for x in vec]

# Decoy data
benchmark_results = {
    'test_run_1': [8, 7, 9, 6],
    'test_run_2': [5, 5, 4, 3]
}

network_nodes = [
    {'id': 'N1', 'load': 6, 'temp': 8},
    {'id': 'N2', 'load': 9, 'temp': 12},
    {'id': 'N3', 'load': 5, 'temp': 7},
    {'id': 'N4', 'load': 4, 'temp': 6},
    {'id': 'N5', 'load': 10, 'temp': 14}
]

# System log with irrelevant timestamps and events
system_log = [
    (1001, 'heartbeat'), (1002, 'update'), (1003, 'error'),
    (1004, 'heartbeat'), (1005, 'sync'), (1006, 'heartbeat')
]

# Dead code path
if False:
    fallback_config = {k: v * 2 for k, v in network_nodes[0].items()}
    redundant_calc = sum(fallback_config.values())

# Red herring list comprehension
_ = [node['load'] * node['temp'] for node in network_nodes if node['load'] > 7]

# Distractor variables
baseline_threshold = 7.5
connection_matrix = [[1, 0, 1], [0, 1, 1], [1, 1, 0]]

# Core processing
active_heartbeats = len([event for ts, event in system_log if event == 'heartbeat'])
status_flags = []
for idx, node in enumerate(network_nodes):
    # Simulate health check using actual logic
    health_data = {k: v for k, v in node.items() if k != 'id'}
    is_stable = analyze_node_health(health_data)
    status_flags.append((f'Node_{idx}', is_stable, active_heartbeats >= 3))

# Misdirection: unused zip operation
zipped_debug = list(zip([n['id'] for n in network_nodes], [n['load'] for n in network_nodes]))

# Set operations as per language-specific requirement
unresponsive_ids = {'N2', 'N5'}
stable_ids = {f'Node_{i}' for i, (_, stable, _) in enumerate(status_flags) if stable}
detected_outliers = unresponsive_ids.intersection(stable_ids)

# Dictionary aggregation with enumerate (required features)
correlation_map = {}
for i, (name, stable, hb_ok) in enumerate(status_flags):
    correlation_map[name] = (i + 1) * (2 if stable else 1) * (1.5 if hb_ok else 1)

# Final computation — only this matters
aggregated_health = sum(correlation_map.values())
heartbeat_influence = active_heartbeats * 1.5

# Key statement
final_diagnostic = int(aggregated_health - heartbeat_influence + len(detected_outliers) * 5)

print(f"Result: {final_diagnostic}")