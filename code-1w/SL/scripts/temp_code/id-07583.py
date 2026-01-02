def analyze_redundancy(nodes):
    # Irrelevant helper: calculates node degrees (not used in final result)
    degree_count = {}
    for node in nodes:
        degree = len(node['connections'])
        degree_count[node['id']] = degree
    return degree_count

network_nodes = [
    {'id': 1, 'connections': [2, 3], 'status': 'active'},
    {'id': 2, 'connections': [1, 3, 4], 'status': 'active'},
    {'id': 3, 'connections': [1, 2, 4], 'status': 'standby'},
    {'id': 4, 'connections': [2, 3], 'status': 'active'}
]

flow_matrix = [
    [0, 15, 10, 0],
    [15, 0, 5, 8],
    [10, 5, 0, 12],
    [0, 8, 12, 0]
]

# Misleading pre-computations
avg_flow = sum(sum(row) for row in flow_matrix) / len(flow_matrix)
status_filter = [node['id'] for node in network_nodes if node['status'] == 'active']
redundant_links = [(i, j) for i in range(len(flow_matrix)) for j in range(i+1, len(flow_matrix)) if flow_matrix[i][j] > 10]

# Real computation begins
edge_sum = sum(
    flow_matrix[i][j] for i in range(len(flow_matrix))
    for j in range(len(flow_matrix))
    if i != j
)

utilization_rates = []
for i, node in enumerate(network_nodes):
    total_flow = sum(flow_matrix[i])
    normalized_rate = total_flow / (len(node['connections']) + 1)
    utilization_rates.append(round(normalized_rate, 2))

# Simulate capacity scaling based on topology
scaling_factor = len([n for n in network_nodes if n['status'] == 'active'])
capacity_pool = [edge_sum * 0.1, scaling_factor * 50]

# Secondary distraction: unused path analysis
potential_paths = [
    (src, tgt) for src in range(4) 
    for tgt in range(4) 
    if src != tgt and flow_matrix[src][tgt] == 0
]
path_count_estimate = len(potential_paths) * 0.5

# Core logic: efficiency depends on edge_sum, scaling_factor, and active connections
active_connections = sum(
    1 for node in network_nodes 
    for conn in node['connections'] 
    if node['status'] == 'active'
)

# List comprehension to compute weighted contributions
weights = [round((utilization_rates[i] / (sum(utilization_rates) or 1)) * capacity_pool[1], 2) for i in range(4)]
adjusted_capacity = int((edge_sum * 0.8) + (scaling_factor * 10))

# Final efficiency calculation
redundancy_score = len(redundant_links) * 5
baseline_efficiency = adjusted_capacity + redundancy_score

# Key statement
final_capacity = baseline_efficiency - int(path_count_estimate)

print(f"Result: {final_capacity}")