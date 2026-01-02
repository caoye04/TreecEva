import itertools

# Simulated sensor network diagnostic system
network_graph = {
    'sensor_A': ['relay_1', 'relay_2'],
    'sensor_B': ['relay_2', 'relay_3'],
    'relay_1': ['hub_X'],
    'relay_2': ['hub_X', 'hub_Y'],
    'relay_3': ['hub_Y'],
    'hub_X': [],
    'hub_Y': []
}

diagnostics = {
    'voltage_A': 12.4, 'voltage_B': 11.8,
    'temp_X': 67.3, 'temp_Y': 72.1,
    'signal_A': 89, 'signal_B': 94
}

# Irrelevant baseline thresholds (distractor)
thresholds = {
    'pressure': 101.3, 'humidity': 45,
    'light': 300, 'co2': 400
}

# Misleading intermediate calculation (dead path)
def compute_stability_index(data):
    return sum(v ** 0.5 for v in data.values() if isinstance(v, (int, float))) * 0.3

stability_score = compute_stability_index(diagnostics)  # Red herring

# Unused utility function (decoy)
def validate_calibration(nodes):
    valid_set = set()
    for node in nodes:
        if node.startswith('sensor') or node.endswith('X'):
            valid_set.add(node)
    return valid_set

# Real logic begins here
visited = set()
entry_points = []

for node in network_graph:
    if node.startswith('sensor'):
        entry_points.append(node)

# Find root nodes (sources in the graph)
def find_root_nodes(graph):
    all_children = set(child for children in graph.values() for child in children)
    roots = [node for node in graph if node not in all_children]
    return sorted(roots)  # Only 'sensor_A', 'sensor_B' are roots

# Bit manipulation decoy (irrelevant)
mask = 0b101010
obfuscated_code = (len(entry_points) << 3) ^ mask & 0xFF

# Complex data transformation with slicing distraction
event_log = ['init', 'ping_A', 'ping_B', 'sync', 'ack_X', 'ack_Y', 'done']
recent_events = event_log[-5:-1]  # unused slice

# Set operations used meaningfully
def analyze_path(root_nodes, readings):
    hub_coverage = set()
    signal_nodes = set()

    # Build coverage map (real logic)
    for root in root_nodes:
        stack = [root]
        while stack:
            current = stack.pop()
            if current in network_graph:
                for child in network_graph[current]:
                    hub_coverage.add(child)
                    stack.append(child)
    
    # Extract relevant hubs
    primary_hubs = {h for h in hub_coverage if h.startswith('hub')}
    
    # Signal correlation (distraction but looks relevant)
    for k, v in readings.items():
        if 'signal' in k and v > 90:
            signal_nodes.add(k.split('_')[1])
    
    # Critical computation: weighted diagnostic
    voltage_sum = sum(readings[k] for k in readings if 'voltage' in k)
    temp_extremes = [readings[k] for k in readings if 'temp' in k]
    thermal_factor = max(temp_extremes) - min(temp_extremes)
    
    # Real answer derivation
    base_score = voltage_sum * 10
    adjustment = int(thermal_factor * 100)
    final_score = base_score - adjustment
    
    # Multiple assignments distraction
    interim, final_diagnostic = 0, 0
    interim = final_score + len(primary_hubs) * 5
    final_diagnostic = interim
    
    # Dead code branch (never executes)
    if len(signal_nodes) > 10:
        final_diagnostic += 100
    
    # Use of itertools (meets requirement)
    combinations = list(itertools.combinations(primary_hubs, 2))
    if len(combinations) > 0:
        final_diagnostic -= 10  # minor penalty
    
    return final_diagnostic

# Key execution point
root_list = find_root_nodes(network_graph)
final_diagnostic = analyze_path(root_list, diagnostics)

# Output result as required
print(f"Target result: {final_diagnostic}")