from collections import Counter, defaultdict

def process_node_activity(activity_log):
    # Process node activity patterns
    node_counter = Counter(activity_log)
    
    # Analyze frequency patterns
    pattern_strength = defaultdict(int)
    for node, count in node_counter.items():
        if count > 5:
            pattern_strength[node] = count * 2
        else:
            pattern_strength[node] = count
    
    # This is a distraction - not used in final calculation
    anomaly_score = sum(v for k, v in pattern_strength.items() if k % 3 == 0)
    return pattern_strength

def map_connection_topology(nodes, mapping_function):
    # Create a complex network topology map
    topology = {}
    redundant_paths = set()
    
    for i, node in enumerate(nodes):
        # Calculate node importance (distraction)
        importance = (node * 2) % 10
        
        # Map connections using the mapping function
        connections = mapping_function(node)
        
        # Store valid connections only
        valid_connections = [c for c in connections if c in nodes]
        topology[node] = valid_connections
        
        # Add to redundant paths for analysis (unused)
        if len(valid_connections) > 2:
            redundant_paths.add(node)
    
    return topology

def optimize_paths(topology):
    # Optimization algorithm (mostly distraction)
    optimized = {}
    critical_nodes = set()
    
    for node, connections in topology.items():
        if len(connections) == 0:
            optimized[node] = 0
        elif len(connections) == 1:
            optimized[node] = 2
            critical_nodes.add(node)
        else:
            # This calculation is mostly irrelevant
            optimized[node] = min(5, len(connections) * 1.5)
    
    # This return value isn't used in the final calculation
    return optimized, critical_nodes

def calculate_network_value(nodes, connection_strength):
    if not nodes:
        return 0
    
    # Define network parameters
    base_value = 15
    scaling_factor = 0.75
    node_multiplier = lambda x: x if x % 2 == 0 else x + 1
    
    # Map node connections - this creates the network topology
    connection_map = map_connection_topology(
        nodes, 
        lambda n: [n-2, n+2, n//2] if n > 4 else [n+1]
    )
    
    # Calculate primary network metrics
    connectivity = sum(len(connections) for connections in connection_map.values())
    
    # Calculate node value contribution
    node_values = {node: node_multiplier(node) for node in nodes}
    total_node_value = sum(node_values.values())
    
    # Process activity patterns (distraction)
    activity_patterns = process_node_activity(nodes + [8, 8, 8, 12, 12])
    
    # Optimize network paths (mostly distraction)
    path_metrics, _ = optimize_paths(connection_map)
    
    # Calculate stability coefficient (relevant)
    stability = min(len(nodes), 10) / 10
    
    # Calculate network density (relevant)
    max_possible_connections = len(nodes) * (len(nodes) - 1) / 2
    actual_connections = connectivity / 2  # Each connection is counted twice in connectivity
    density = 0
    if max_possible_connections > 0:
        density = actual_connections / max_possible_connections
    
    # Calculate final network score
    raw_score = base_value * stability * (total_node_value / len(nodes))
    adjusted_score = raw_score * scaling_factor * (1 + density)
    
    # Apply connection strength modifier
    final_score = adjusted_score * connection_strength
    
    # Apply bitwise operations for network signature (distraction)
    network_signature = 0
    for node in nodes:
        network_signature |= (1 << (node % 8))
    
    return int(final_score)

# Initialize network parameters
active_nodes = [2, 4, 6, 8, 10]
backup_nodes = [3, 5, 7, 9]
connection_strength = 1.25
redundancy_level = 3

# Calculate alternative network configurations (distraction)
alternative_score = 0
for i in range(3):
    test_nodes = active_nodes[i:] + backup_nodes[:i]
    alternative_score += sum(test_nodes) // len(test_nodes)

# Calculate unused metrics (distraction)
network_overhead = sum(n for n in active_nodes if n % 2 == 0) * redundancy_level
latency_estimate = sum(active_nodes) / len(active_nodes) * 0.3

# This is the key calculation we're asked about
network_score = calculate_network_value(active_nodes, connection_strength)

# More distractions after the key calculation
reliability_score = network_score % 10 * redundancy_level
scalability_index = sum(1 for n in active_nodes if n > 5) * connection_strength

print(f"Result: {network_score}")