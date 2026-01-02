from itertools import permutations

def analyze_congestion(flow_data, threshold):
    congested_nodes = []
    temp_loads = []
    for i, load in enumerate(flow_data):
        if load > threshold * 1.5:
            congested_nodes.append(i)
        temp_loads.append(load * 0.1)  # Irrelevant accumulation
    return congested_nodes

def calculate_efficiency_score(nodes, base_rate):
    score = 0
    decay = 1.0
    for _ in nodes:
        score += base_rate * decay
        decay *= 0.9
    return round(score, 4)

def optimize_routing(flow_matrix, node_capacity):
    n = len(flow_matrix)
    total_flow = sum(sum(row) for row in flow_matrix)
    capacity_utilization = [sum(flow_matrix[i]) / node_capacity[i] for i in range(n)]
    
    # Distractor: Compute but don't use
    max_util_node = capacity_utilization.index(max(capacity_utilization))
    efficiency_factor = calculate_efficiency_score(list(range(n)), 0.85)
    
    # Real logic begins
    candidate_paths = []
    for p in permutations(range(n)):
        if p[0] == 0 and p[-1] == n-1:
            candidate_paths.append(p)
    
    best_metric = float('inf')
    optimal_path = None
    for path in candidate_paths:
        delay_metric = 0
        for i in range(len(path) - 1):
            delay_metric += flow_matrix[path[i]][path[i+1]]
        if delay_metric < best_metric:
            best_metric = delay_metric
            optimal_path = path
    
    # Use only the length of optimal path for final calculation
    path_penalty = len(optimal_path) - n
    adjusted_flow = total_flow * (1 + path_penalty * 0.1)
    
    # Misleading intermediate: not actually used in core logic
    dummy_shift = 0
    for cap in node_capacity:
        dummy_shift += cap % 7
    
    # Final computation
    base_bandwidth = 1000
    utilization_penalty = sum(capacity_utilization) / n
    final_bandwidth = base_bandwidth * (1 - utilization_penalty) + efficiency_factor * 10
    
    # Print required output
    print(f"Result: {final_bandwidth}")
    return final_bandwidth

# Input setup
flow_data = [120, 200, 80, 250]
node_capacity = [300, 250, 200, 400]
flow_matrix = [
    [0, 50, 70, 0],
    [50, 0, 0, 100],
    [70, 0, 0, 80],
    [0, 100, 80, 0]
]

# Trigger function call
final_bandwidth = optimize_routing(flow_matrix, node_capacity)