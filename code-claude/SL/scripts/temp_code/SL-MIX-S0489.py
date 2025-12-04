import itertools

def calculate_signal_quality(distance, interference):
    # Lower distance and interference means better quality
    base_quality = 100 - (distance * 5)
    noise_factor = interference * 2.5
    # Signal quality can't be negative
    return max(0, base_quality - noise_factor)

def calculate_network_strength(nodes, connections):
    if not nodes or len(nodes) < 2:
        return 0
    
    # Sort nodes by their ID for consistent processing
    sorted_nodes = sorted(nodes)
    
    # Calculate primary network metrics
    connection_density = len(connections) / (len(nodes) * (len(nodes) - 1) / 2)
    
    # Calculate average signal quality across all active connections
    total_quality = 0
    active_count = 0
    
    # Track which nodes are connected for redundancy calculation
    connected_nodes = set()
    for connection in connections:
        node1, node2, distance, interference = connection
        if node1 in nodes and node2 in nodes:
            quality = calculate_signal_quality(distance, interference)
            total_quality += quality
            active_count += 1
            connected_nodes.add(node1)
            connected_nodes.add(node2)
    
    # Calculate average signal quality (avoid division by zero)
    avg_quality = total_quality / active_count if active_count > 0 else 0
    
    # Calculate network redundancy (not used in final calculation)
    redundancy = len(connected_nodes) / len(nodes) if nodes else 0
    
    # Calculate potential backup routes (not directly used)
    potential_backups = len(list(itertools.combinations(nodes, 2))) - len(connections)
    
    # Network stability factor (used as a multiplier)
    stability_factor = 0.8 + (0.2 * connection_density)
    
    # Calculate final network strength
    network_strength = int(avg_quality * stability_factor)
    
    return network_strength

# Define network nodes and connections
nodes = [1, 2, 3, 4, 5]

# Format: (node1, node2, distance, interference)
all_connections = [
    (1, 2, 5, 2),   # Short distance, low interference
    (1, 3, 8, 4),   # Medium distance, medium interference
    (2, 3, 6, 1),   # Medium distance, low interference
    (2, 4, 10, 3),  # Long distance, medium interference
    (3, 5, 7, 5),   # Medium distance, high interference
    (4, 5, 4, 2)    # Short distance, low interference
]

# Filter connections based on some criteria (intervention - not critical to solution)
filtered_connections = [conn for conn in all_connections if conn[2] < 15]

# Calculate alternative path metrics (intervention - not used in final answer)
alternative_paths = {}
for n1, n2, _, _ in filtered_connections:
    key = tuple(sorted([n1, n2]))
    alternative_paths[key] = alternative_paths.get(key, 0) + 1

# Identify backup nodes (intervention - not used in final calculation)
backup_nodes = [node for node in nodes if node % 2 == 0]

# Calculate network strength with active connections
active_connections = [conn for conn in filtered_connections if conn[3] < 6]
network_strength = calculate_network_strength(nodes, active_connections)

# Recalculate with theoretical improvements (intervention - not used in final answer)
improved_connections = [(n1, n2, d*0.8, i*0.7) for n1, n2, d, i in active_connections]
theoretical_strength = calculate_network_strength(nodes, improved_connections)

# Output the result
print(f"Network strength: {network_strength}")