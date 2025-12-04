from collections import defaultdict, Counter

def process_network_data(raw_data):
    # Process input data to extract node information
    processed = []
    error_count = 0
    for entry in raw_data:
        if entry % 7 == 0:
            error_count += 1
            continue  # Skip entries divisible by 7 (simulating errors)
        processed.append((entry * 2) ^ 0xA5)  # Apply bitwise transformation
    
    # Calculate some network statistics (unused)
    avg_value = sum(processed) / len(processed) if processed else 0
    variance = sum((x - avg_value) ** 2 for x in processed) / len(processed) if processed else 0
    return processed, error_count

def map_connections(nodes):
    # Create a connection map between nodes
    connections = defaultdict(list)
    node_types = Counter()
    
    for i, node_id in enumerate(nodes):
        # Determine node type based on bit patterns
        node_type = 'primary' if (node_id & 0x3) == 0 else 'secondary'
        node_types[node_type] += 1
        
        # Connect to previous nodes based on certain rules
        for j in range(max(0, i-3), i):
            if (nodes[i] ^ nodes[j]) % 5 == 0:  # XOR-based connection rule
                connections[i].append(j)
                connections[j].append(i)
    
    # Calculate potential backup paths (unused)
    backup_paths = 0
    for node in connections:
        if len(connections[node]) > 2:
            backup_paths += len(connections[node]) - 2
    
    return dict(connections), node_types

def calculate_network_reliability(active_nodes, connection_map):
    # Calculate network reliability score
    if not active_nodes:
        return 0
    
    # Count connected components
    visited = set()
    component_sizes = []
    
    for node in active_nodes:
        if node not in visited:
            # Start BFS from this node
            component = set()
            queue = [node]
            while queue:
                current = queue.pop(0)
                if current not in component and current in active_nodes:
                    component.add(current)
                    visited.add(current)
                    # Add neighbors to queue
                    for neighbor in connection_map.get(current, []):
                        if neighbor not in component and neighbor in active_nodes:
                            queue.append(neighbor)
            
            component_sizes.append(len(component))
    
    # Calculate reliability metrics
    total_nodes = len(active_nodes)
    largest_component = max(component_sizes) if component_sizes else 0
    component_count = len(component_sizes)
    
    # These factors don't actually affect the final result
    redundancy_factor = sum(1 for size in component_sizes if size > 1) / max(1, component_count)
    isolation_penalty = sum(1 for size in component_sizes if size == 1) * 2
    
    # The actual reliability calculation
    reliability = (largest_component / total_nodes) * 100 * (1 - (component_count - 1) / total_nodes)
    
    return reliability

# Main network analysis
raw_network_data = [23, 14, 35, 42, 19, 28, 56, 31, 49, 63, 77, 21, 84, 91]
processed_data, error_logs = process_network_data(raw_network_data)

# Identify active nodes (nodes with even processed values)
active_candidates = [i for i, val in enumerate(processed_data) if val % 2 == 0]
backup_nodes = [i for i, val in enumerate(processed_data) if val % 3 == 0]

# Simulate network traffic (unused)
traffic_simulation = [(node, processed_data[node] % 100) for node in active_candidates]
simulated_failures = [node for node, traffic in traffic_simulation if traffic > 80]

# Determine final active nodes (even processed values, not in simulated failures)
active_nodes = [node for node in active_candidates if node not in simulated_failures]

# Generate connection map
connection_map, node_classification = map_connections(processed_data)

# Calculate network reliability
network_reliability = calculate_network_reliability(active_nodes, connection_map)

# Calculate alternative metrics (unused)
backup_reliability = calculate_network_reliability(backup_nodes, connection_map)
full_network_reliability = calculate_network_reliability(list(range(len(processed_data))), connection_map)

print(f"Result: {network_reliability}")