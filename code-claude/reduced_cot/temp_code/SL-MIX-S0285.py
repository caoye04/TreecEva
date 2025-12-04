def process_node_activity(node_values, modifier=1.5):
    """Process node activity with various transformations."""
    activity_levels = []
    noise_factor = 3.7  # Misleading - not actually used
    for val in node_values:
        # Complex but irrelevant calculation
        potential = (val * modifier) ** 2 / 4 if val > 0 else 0
        activity_levels.append(val + 0.5)  # The actual calculation ignores potential
    
    # Misleading calculations that don't affect the result
    max_potential = sum([v ** 2 for v in node_values if v > 5]) / 2
    activity_index = len([v for v in activity_levels if v > 2])
    
    return activity_levels

def apply_network_filters(nodes, filters=[2, 4, 6]):
    """Apply network filters to nodes - mostly distraction."""
    filtered_nodes = {}
    for i, node in enumerate(nodes):
        # Complex but ultimately unused calculations
        priority = (i % 3) * node + sum(filters)
        weight = node * 1.5 if node > 0 else node * 0.8
        
        # Only this assignment is relevant
        filtered_nodes[i] = node > 0
        
        # More distraction calculations
        if priority > 15:
            weight *= 0.75
        
    return filtered_nodes

def calculate_active_nodes(graph, threshold):
    """Calculate number of active nodes in the network."""
    # Misleading variables and calculations
    total_edges = sum(len(connections) for connections in graph.values())
    edge_density = total_edges / len(graph) if graph else 0
    
    # Extract node values - only this part is truly relevant
    node_values = list(graph.keys())
    
    # More distraction with complex calculations
    activity_scores = process_node_activity(node_values)
    network_resilience = sum([1 for score in activity_scores if score > 3])
    
    # Filter nodes - the key operation
    active_status = apply_network_filters(node_values)
    
    # Misleading recursive function that isn't used
    def calculate_cascade_effect(node, depth=0):
        if depth > 3 or node not in graph:
            return 0
        return 1 + sum(calculate_cascade_effect(n, depth+1) for n in graph.get(node, []))
    
    # The actual calculation happens here, ignoring most of the above
    active_count = sum(1 for status in active_status.values() if status)
    
    # More distraction calculations
    potential_growth = [calculate_cascade_effect(node) for node in node_values[:2]]
    stability_index = edge_density * network_resilience
    
    return active_count

# Network graph representation - nodes with positive values are potentially active
network_graph = {
    5: [2, 3],
    -2: [4, 5],
    0: [1],
    3: [5, -2],
    -1: [0, 3],
    2: [-1, 0]
}

# Some misleading calculations
network_size = len(network_graph)
connection_density = sum(len(v) for v in network_graph.values()) / network_size
health_score = sum(k for k in network_graph.keys() if k > 0)

# The threshold affects nothing in the actual calculation
threshold = 2.5 if health_score > 10 else 1.8

# This is the key calculation
final_count = calculate_active_nodes(network_graph, threshold)

# More distraction
adjusted_count = final_count * (connection_density if connection_density > 1 else 1)
scaled_result = [n * adjusted_count for n in [0.5, 1.0, 1.5]]

print(f"Result: {final_count}")