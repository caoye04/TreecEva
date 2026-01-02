from itertools import combinations

def analyze_redundancy(paths):
    # Analyzes redundant paths; returns number of overlapping segments
    overlaps = 0
    for pair in combinations(paths, 2):
        overlaps += len(set(pair[0]) & set(pair[1]))
    return overlaps

def calculate_theoretical_capacity(channels, modulation_level):
    # Irrelevant helper: calculates theoretical bandwidth (not used in final result)
    return channels * 100 * (2 ** modulation_level)

def route_failover(backups, threshold=3):
    # Distractor function: simulates failover logic
    recovered = 0
    for b in backups:
        if sum(b) > threshold:
            recovered += 1
    return recovered

def optimize_routing(flow_matrix, latency_map):
    base_capacity = 150
    penalty = 0
    total_flow = 0
    
    # Real computation begins
    for row in flow_matrix:
        for flow in row:
            total_flow += flow
    
    # Compute average latency from mapping
    latencies = []
    for key in latency_map:
        if key.startswith('node'):
            latencies.append(latency_map[key])
    avg_latency = sum(latencies) / len(latencies) if latencies else 0
    
    # Meaningful penalty based on latency
    if avg_latency > 40:
        penalty += 30
    elif avg_latency > 30:
        penalty += 15
    
    # Dummy operations with intermediate variables
    temp_score = base_capacity - penalty
    adjustment_factor = 1.0
    if total_flow > 500:
        adjustment_factor *= 0.9
    if total_flow < 200:
        adjustment_factor *= 1.1
    
    # Final bandwidth calculation
    final_bandwidth = int(temp_score * adjustment_factor)
    
    # Dead code branch (never executed due to fixed inputs)
    emergency_mode = False
    if len(flow_matrix) > 10 or avg_latency > 100:
        emergency_mode = True
        final_bandwidth = 10  # red herring
    
    return final_bandwidth

# Simulated network data
flow_matrix = [
    [50, 75, 100],
    [80, 60, 90],
    [45, 65, 40]
]

latency_map = {
    'node_01': 25,
    'node_02': 35,
    'node_03': 45,
    'aux_diag_01': 12,  # irrelevant diagnostic node
    'aux_diag_02': 18   # irrelevant diagnostic node
}

# Unused variables (distractors)
redundant_paths = [['A', 'B', 'C'], ['A', 'X', 'C'], ['D', 'B', 'C']]
modulation_level = 4
channels = 8
topology_checksum = 0x1A3F

# Key execution point
final_bandwidth = optimize_routing(flow_matrix, latency_map)

# Print result as required
print(f"Result: {final_bandwidth}")