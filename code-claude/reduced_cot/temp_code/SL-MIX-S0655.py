from collections import defaultdict, Counter

def simulate_traffic(nodes, paths, threshold=0.75):
    # Simulate network traffic (not relevant to final answer)
    traffic = defaultdict(int)
    for start, end in paths:
        traffic[start] += 1
        traffic[end] += 1
    
    congestion = sum(1 for node, count in traffic.items() if count > threshold * len(nodes))
    return congestion * 10

def optimize_routing(connections, active):
    # Misleading optimization function
    routes = {}
    for src, dest in connections:
        if src in active and dest in active:
            weight = (ord(src) + ord(dest)) % 10
            routes[(src, dest)] = weight
    
    return sum(routes.values())

def calculate_redundancy(nodes):
    # Calculate system redundancy factor
    node_chars = [ord(n) - ord('A') for n in nodes]
    redundancy = 1
    for val in node_chars:
        if val % 2 == 0:
            redundancy *= (val + 1)
        else:
            redundancy += val
    return redundancy

def calculate_network_metric(nodes, connections, reliability):
    # This is the key function that determines the answer
    active_connections = [(src, dst) for src, dst in connections if src in nodes and dst in nodes]
    
    # Distraction: calculate node popularity
    node_usage = Counter()
    for src, dst in active_connections:
        node_usage[src] += 1
        node_usage[dst] += 1
    
    # Calculate network density (relevant)
    max_possible_connections = len(nodes) * (len(nodes) - 1) / 2
    actual_connections = len(active_connections)
    density = actual_connections / max_possible_connections if max_possible_connections > 0 else 0
    
    # Distraction: calculate centrality
    centrality = {node: 0 for node in nodes}
    for node in nodes:
        connections_count = sum(1 for src, dst in active_connections if src == node or dst == node)
        centrality[node] = connections_count / (len(nodes) - 1) if len(nodes) > 1 else 0
    
    # Distraction: potential bottlenecks
    bottlenecks = [node for node, count in node_usage.items() if count > len(nodes) / 2]
    bottleneck_factor = len(bottlenecks) * 5
    
    # Calculate core metric components
    connectivity = len(active_connections) / len(nodes) if nodes else 0
    reliability_factor = sum(reliability.values()) / len(reliability) if reliability else 0
    
    # Distraction: calculate theoretical bandwidth
    bandwidth = sum([ord(n) - ord('A') + 1 for n in nodes]) * 2
    
    # Final calculation of network strength
    base_metric = (density * 50) + (connectivity * 30) + (reliability_factor * 20)
    
    # Apply small adjustment based on node count (misleading but still used)
    adjustment = len(nodes) % 5
    
    return round(base_metric + adjustment, 2)

# Network configuration
all_nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
all_connections = [
    ('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E'),
    ('D', 'F'), ('E', 'F'), ('E', 'G'), ('F', 'H'), ('G', 'H')
]

# Active nodes in the current network
active_nodes = ['A', 'B', 'C', 'D', 'E', 'F']

# Connection reliability ratings (0-1)
reliability = {'A': 0.95, 'B': 0.88, 'C': 0.92, 'D': 0.78, 'E': 0.85, 'F': 0.90}

# Distraction: Calculate traffic simulation
traffic_load = simulate_traffic(active_nodes, all_connections)

# Distraction: Optimize routing
routing_efficiency = optimize_routing(all_connections, active_nodes)

# Distraction: Calculate redundancy
redundancy_factor = calculate_redundancy(active_nodes)

# Calculate network strength - this is the key statement
network_strength = calculate_network_metric(active_nodes, all_connections, reliability)

# Distraction: Final network score
potential_score = (network_strength * routing_efficiency) / (traffic_load or 1)

# Distraction: Network health status
health_status = "OPTIMAL" if network_strength > 75 else "GOOD" if network_strength > 60 else "FAIR"

print(f"Network Configuration Analysis:")
print(f"- Active Nodes: {len(active_nodes)} of {len(all_nodes)}")
print(f"- Traffic Load: {traffic_load}")
print(f"- Routing Efficiency: {routing_efficiency}")
print(f"- Redundancy Factor: {redundancy_factor}")
print(f"- Network Strength: {network_strength}")
print(f"- Health Status: {health_status}")