def process_node(node_data, threshold=0.5):
    # Process node attributes based on type and connectivity
    node_type = node_data.get('type', 'standard')
    connectivity = node_data.get('connections', 0)
    
    # Calculate potential based on node type
    potential_map = {'standard': 1.0, 'router': 2.5, 'gateway': 3.0, 'switch': 1.75}
    base_potential = potential_map.get(node_type, 0.8)
    
    # Apply connectivity factor
    if connectivity > 5:
        potential = base_potential * 1.2
    else:
        potential = base_potential * 0.9
    
    # Apply threshold filter
    return potential > threshold, potential

def analyze_network_segment(segment_id, nodes):
    # Analyze network segment performance
    segment_load = sum([n.get('traffic', 0) for n in nodes if n.get('segment') == segment_id])
    segment_capacity = 1000 * len([n for n in nodes if n.get('segment') == segment_id])
    
    # Calculate theoretical throughput
    theoretical_throughput = segment_capacity * 0.8
    
    # This calculation is not used in the final result
    segment_utilization = segment_load / segment_capacity if segment_capacity else 0
    
    return segment_id, theoretical_throughput

def calculate_network_efficiency(nodes):
    # Extract active nodes with high stability
    stable_nodes = [n for n in nodes if n.get('stability', 0) > 0.7]
    
    # Calculate weighted node values
    node_values = {}
    for i, node in enumerate(stable_nodes):
        # Complex weighting formula - only part of this is relevant
        base_value = node.get('capacity', 0) * node.get('reliability', 1.0)
        redundancy_factor = 1 + (0.1 * node.get('redundancy', 0))
        
        # Misleading calculation that isn't used
        optimal_load = node.get('capacity', 0) * 0.75
        load_difference = abs(node.get('load', 0) - optimal_load)
        
        # Calculate node efficiency - this is the key calculation
        efficiency = base_value * redundancy_factor
        if node.get('type') == 'gateway':
            efficiency *= 1.25
        
        node_values[node.get('id')] = efficiency
    
    # Calculate network segments - this is a distraction
    segments = set([n.get('segment') for n in nodes if 'segment' in n])
    segment_metrics = {}
    for segment in segments:
        segment_id, throughput = analyze_network_segment(segment, nodes)
        segment_metrics[segment_id] = throughput
    
    # Calculate topological density - another distraction
    total_connections = sum([n.get('connections', 0) for n in nodes])
    max_connections = len(nodes) * (len(nodes) - 1)
    density = total_connections / max_connections if max_connections > 0 else 0
    
    # Calculate the actual network efficiency
    if not node_values:
        return 0
    
    # The key calculation for network efficiency
    efficiency_sum = sum(node_values.values())
    active_node_count = len(node_values)
    
    # Apply diminishing returns formula
    base_efficiency = efficiency_sum / (active_node_count * 2.5)
    network_factor = 0.8 + (0.2 * (1 - 1/(active_node_count + 1)))
    
    return round(base_efficiency * network_factor, 3)

# Network node definitions
network_nodes = [
    {'id': 'A1', 'type': 'router', 'capacity': 100, 'reliability': 0.95, 'redundancy': 2, 'stability': 0.85, 'connections': 4, 'load': 65, 'traffic': 250, 'segment': 1},
    {'id': 'B2', 'type': 'switch', 'capacity': 80, 'reliability': 0.92, 'redundancy': 1, 'stability': 0.9, 'connections': 6, 'load': 45, 'traffic': 180, 'segment': 1},
    {'id': 'C3', 'type': 'gateway', 'capacity': 120, 'reliability': 0.98, 'redundancy': 3, 'stability': 0.75, 'connections': 8, 'load': 95, 'traffic': 310, 'segment': 2},
    {'id': 'D4', 'type': 'standard', 'capacity': 60, 'reliability': 0.88, 'redundancy': 0, 'stability': 0.6, 'connections': 2, 'load': 30, 'traffic': 120, 'segment': 2},
    {'id': 'E5', 'type': 'router', 'capacity': 90, 'reliability': 0.94, 'redundancy': 1, 'stability': 0.8, 'connections': 5, 'load': 70, 'traffic': 280, 'segment': 3}
]

# Apply filtering to nodes
filter_results = [process_node(node) for node in network_nodes]
filtered_nodes = [network_nodes[i] for i, result in enumerate(filter_results) if result[0]]

# Process the segments for optimization
segment_data = {}
for node in filtered_nodes:
    segment = node.get('segment', 0)
    if segment not in segment_data:
        segment_data[segment] = {'count': 0, 'total_capacity': 0}
    segment_data[segment]['count'] += 1
    segment_data[segment]['total_capacity'] += node.get('capacity', 0)

# Calculate theoretical bandwidth - not used in final result
theoretical_bandwidth = sum([segment_data[s]['total_capacity'] for s in segment_data])

# Calculate network efficiency
network_efficiency = calculate_network_efficiency(filtered_nodes)

# Calculate alternative metrics - not used in the final result
alternative_metric = sum([node.get('reliability', 0) for node in filtered_nodes]) / len(filtered_nodes) if filtered_nodes else 0

# Apply scaling factor - not used in the final result
scaled_metric = alternative_metric * 10

print(f"Result: {network_efficiency}")