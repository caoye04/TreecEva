import itertools

def calculate_redundancy_factor(active_paths, total_capacity):
    redundant_links = active_paths * 3  # misleading computation
    efficiency_ratio = total_capacity / (active_paths + 1)
    return efficiency_ratio * 0.8  # dead coefficient

def compute_bandwidth_utilization(throughput_matrix, max_throughput):
    temp_sum = sum(sum(row) for row in throughput_matrix)
    utilization = temp_sum / (len(throughput_matrix) * max_throughput)
    unused_calc = temp_sum * 2 - max_throughput  # irrelevant variable
    return min(utilization, 1.0)

def analyze_network_latency(node_pairs, base_latency):
    latency_values = []
    for pair in node_pairs:
        if len(pair) == 2:
            latency = base_latency + abs(pair[0] - pair[1]) * 0.5
            latency_values.append(latency)
        else:
            latency_values.append(base_latency * 3)  # dead code path
    
    if not latency_values:
        return base_latency * 2  # unused return path
    
    return sum(latency_values) / len(latency_values)

def compute_network_efficiency(primary_nodes, secondary_routers, bandwidth_config):
    # Relevant computations
    active_paths = len(primary_nodes) * len(secondary_routers)
    total_capacity = sum(bandwidth_config.values())
    
    # Distractor computations
    redundant_factor = calculate_redundancy_factor(active_paths, total_capacity)
    max_bandwidth = max(bandwidth_config.values()) if bandwidth_config else 0
    
    # Irrelevant variables and misleading calculations
    throughput_matrix = [[bandwidth_config.get(node, 0) for node in primary_nodes]]
    utilization_score = compute_bandwidth_utilization(throughput_matrix, max_bandwidth)
    
    # Dead variable that doesn't affect final result
    network_overhead = redundant_factor * 2 - utilization_score
    
    # Generate node pairs for latency analysis
    node_pairs = list(itertools.combinations(primary_nodes, 2))
    average_latency = analyze_network_latency(node_pairs, 10)
    
    # Core efficiency calculation (actual logic)
    efficiency_score = (total_capacity * utilization_score) / (average_latency + 1)
    
    # Misleading intermediate result
    temp_score = efficiency_score * redundant_factor
    
    # Final calculation with adjustments
    final_score = efficiency_score / (len(secondary_routers) + 1)
    
    return int(final_score)

# Network configuration
primary_nodes = [101, 103, 107, 109]
secondary_routers = ['router_a', 'router_b']
bandwidth_map = {101: 1000, 103: 1500, 107: 800, 109: 1200}

# Execute the network efficiency computation
final_network_score = compute_network_efficiency(primary_nodes, secondary_routers, bandwidth_map)

# Print the target result
print(f"Result: {final_network_score}")