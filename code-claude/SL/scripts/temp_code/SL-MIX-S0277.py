def calculate_latency(hops, bandwidth):
    # Higher bandwidth reduces latency, more hops increases it
    return (hops * 2.5) / (bandwidth ** 0.6)

def optimize_routing(paths, congestion_factors):
    # Routing optimization algorithm (not used in main calculation)
    optimized = {}
    for path, congestion in zip(paths, congestion_factors):
        if congestion > 0.8:
            optimized[path] = path * 0.7
        else:
            optimized[path] = path * 0.9
    return sum(optimized.values()) / len(optimized) if optimized else 0

# Network configuration parameters
node_count = 12
active_nodes = 7
backup_nodes = node_count - active_nodes

# Connection metrics
base_bandwidth = 45.0
bandwidth_fluctuation = 5.0
actual_bandwidth = base_bandwidth - bandwidth_fluctuation

# Network topology metrics
topology_types = {'mesh': 1.0, 'star': 0.6, 'ring': 0.8, 'bus': 0.5}
selected_topology = 'mesh'

# Path calculations (distractor)
paths = [3, 5, 2, 4, 6]
congestion_factors = [0.6, 0.9, 0.3, 0.7, 0.8]

# Error rates by protocol (distractor)
protocol_error_rates = {
    'TCP': 0.02,
    'UDP': 0.05,
    'HTTP': 0.01,
    'HTTPS': 0.005
}

# Calculate packet loss simulation (not used in final calculation)
packet_count = 1000
packet_loss = int(packet_count * protocol_error_rates['TCP'])
successful_packets = packet_count - packet_loss

# Network reliability factor
reliability_base = 0.95
reliability_adjustment = active_nodes / node_count * 0.1
reliability = reliability_base + reliability_adjustment if active_nodes > 5 else reliability_base - reliability_adjustment

# Connection strength calculation
raw_connection_strength = actual_bandwidth * reliability
connection_strength = raw_connection_strength * topology_types.get(selected_topology, 0.5)

# Network latency (distractor)
hop_count = node_count // 2 + 1
network_latency = calculate_latency(hop_count, actual_bandwidth)

# Optimization calculation (distractor)
optimized_value = optimize_routing(paths, congestion_factors)

# Security overhead calculation (distractor)
security_levels = {'low': 0.05, 'medium': 0.1, 'high': 0.2}
security_overhead = security_levels.get('high', 0.1) * connection_strength

def calculate_network_efficiency(active_nodes, connection_strength):
    # Base efficiency calculation
    base_efficiency = (active_nodes / node_count) * 100
    
    # Connection quality factor
    connection_quality = connection_strength / (base_bandwidth * topology_types.get(selected_topology, 0.5))
    
    # Apply diminishing returns for connection quality above 0.8
    quality_factor = connection_quality if connection_quality <= 0.8 else 0.8 + (connection_quality - 0.8) * 0.5
    
    # Calculate potential throughput (distractor)
    potential_throughput = base_bandwidth * active_nodes * quality_factor
    
    # The efficiency calculation
    raw_efficiency = base_efficiency * quality_factor
    
    # Apply topology adjustment
    topology_factor = 1.0 if selected_topology == 'mesh' else 0.8
    
    # Final efficiency calculation with topology adjustment
    return raw_efficiency * topology_factor

# Calculate the network efficiency
network_efficiency = calculate_network_efficiency(active_nodes, connection_strength)

# Apply overhead adjustments (distractor)
overhead_adjusted_efficiency = network_efficiency * (1 - security_levels.get('medium', 0.1))

# Print the result
print(f"Result: {network_efficiency}")
