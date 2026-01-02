from collections import defaultdict
import math

# Simulate network link matrix with redundant metadata
def generate_link_matrix(nodes=5):
    matrix = [[0] * nodes for _ in range(nodes)]
    metadata = defaultdict(lambda: 'unknown')
    for i in range(nodes):
        for j in range(nodes):
            if i != j:
                matrix[i][j] = (i + j) * 2 + 1  # symmetric cost assignment
                metadata[(i, j)] = f'link_{i}_to_{j}'
    return matrix, metadata

# Misleading helper: computes unused signal latency (red herring)
def compute_signal_latency(distance, jitter_factor=0.05):
    return round(distance / 299792 * (1 + jitter_factor), 6)  # speed of light in km/ms

# Real logic: calculate effective bandwidth utilization
def analyze_traffic_flow(flow_map):
    total_load = 0
    peak_hour_adjustment = 1.4
    base_flows = list(flow_map.values())
    
    # Irrelevant sorting step (does not affect final sum)
    base_flows.sort(reverse=True)
    
    for key, value in flow_map.items():
        if 'priority' in key:
            total_load += value * peak_hour_adjustment
        else:
            total_load += value
    
    # Extra computation that looks important but isn't used later
    avg_load = total_load / len(flow_map) if flow_map else 0
    normalized_load = math.floor(avg_load * 100) / 100
    
    return int(total_load)

# Core optimization function combining bitwise and arithmetic ops
def optimize_route_capacity(link_matrix, traffic_flow):
    n = len(link_matrix)
    capacity_sum = 0
    adjustment_mask = 0b1101  # arbitrary mask for interference
    
    # Nested loops over links and simulated flows
    for i in range(n):
        max_local_flow = 0
        for j in range(n):
            edge_weight = link_matrix[i][j]
            # Bitwise interference pattern
            masked_weight = edge_weight & adjustment_mask
            shifted_weight = masked_weight << 1
            
            # Dummy state tracking (not used in output)
            temp_state = {
                'node': i,
                'linked_to': j,
                'raw': edge_weight,
                'masked': shifted_weight
            }
            
            # Only diagonal contributes to actual result
            if i == j:
                capacity_sum += edge_weight * 2
            else:
                # Real contribution: XOR-based weighting on off-diagonal
                capacity_sum += (edge_weight ^ j) % 5
        
    # Combine with traffic analysis (real dependency)
    flow_utilization = analyze_traffic_flow(traffic_flow)
    final_score = capacity_sum * (flow_utilization % 10)
    
    # Dead code branch (never executed due to above logic)
    if False:
        backup_route = [x for x in range(n) if x & 1]
        final_score -= sum(backup_route)
    
    return final_score

# Setup environment
link_matrix, meta_info = generate_link_matrix(5)

# Inject dummy values into matrix (some are overwritten later)
for i in range(5):
    for j in range(5):
        if i == j:
            link_matrix[i][j] = i * 3 + 2

# Define traffic patterns with mixed priorities
traffic_flow = {
    'priority_main': 85,
    'priority_backup': 45,
    'standard_batch_1': 60,
    'standard_batch_2': 30,
    'priority_test': 20
}

# Simulate unused latency calculations (distractor chain)
distances = [120, 300, 150, 400]
latencies = []
for d in distances:
    latencies.append(compute_signal_latency(d))

# Key execution point
final_bandwidth = optimize_route_capacity(link_matrix, traffic_flow)

print(f"Result: {final_bandwidth}")