import itertools
from collections import Counter, defaultdict

def analyze_packet_priority(packet_info):
    # Analyze packet priorities (not relevant to final calculation)
    priority_levels = {'HIGH': 3, 'MEDIUM': 2, 'LOW': 1}
    counts = Counter([p['priority'] for p in packet_info])
    priority_score = sum([priority_levels[p] * c for p, c in counts.items()])
    return priority_score * 0.01

def optimize_routing(node_map, bandwidth):
    # Optimize routing paths (distraction function)
    paths = []
    for i, j in itertools.combinations(node_map.keys(), 2):
        # Calculate theoretical optimal path
        path_score = (node_map[i] ^ node_map[j]) & 0xFF
        if path_score > bandwidth // 10:
            paths.append((i, j, path_score))
    return sum(p[2] for p in paths) if paths else 0

def calculate_network_load(traffic_matrix, active_nodes):
    # This is the core calculation that determines the answer
    total_load = 0
    node_weight = {}
    
    # Calculate node weights based on active connections
    for i, row in enumerate(traffic_matrix):
        connections = sum(1 for val in row if val > 0)
        node_weight[i] = connections * 2
    
    # Process traffic through active nodes only
    for node in active_nodes:
        # Get the traffic for this node from the matrix
        node_traffic = sum(traffic_matrix[node])
        
        # Apply bitwise operations to model network protocols
        protocol_overhead = (node_traffic & 0x3F) | 0x10
        
        # Calculate the actual load contribution from this node
        load_factor = node_weight.get(node, 0) * protocol_overhead
        total_load += load_factor
    
    # Apply network efficiency factor
    efficiency = max(60, 100 - (len(active_nodes) * 5))
    return total_load * (efficiency / 100)

# Network simulation parameters
node_ids = [10, 22, 35, 41, 56, 63, 78, 89]
node_map = {i: 1 << (i % 6) for i in node_ids}

# Network traffic simulation (bytes per second)
traffic_matrix = [
    [0, 420, 0, 150, 0, 0, 310, 0],
    [420, 0, 280, 0, 0, 190, 0, 0],
    [0, 280, 0, 0, 370, 0, 0, 210],
    [150, 0, 0, 0, 250, 0, 0, 0],
    [0, 0, 370, 250, 0, 320, 0, 0],
    [0, 190, 0, 0, 320, 0, 180, 0],
    [310, 0, 0, 0, 0, 180, 0, 290],
    [0, 0, 210, 0, 0, 0, 290, 0]
]

# Distraction: packet information (not used in final calculation)
packet_info = [
    {'id': 1, 'size': 64, 'priority': 'HIGH'},
    {'id': 2, 'size': 128, 'priority': 'MEDIUM'},
    {'id': 3, 'size': 256, 'priority': 'LOW'},
    {'id': 4, 'size': 512, 'priority': 'HIGH'},
    {'id': 5, 'size': 1024, 'priority': 'MEDIUM'}
]

# Distraction: calculate priority score
priority_multiplier = analyze_packet_priority(packet_info)

# Distraction: simulate network conditions
network_conditions = {'latency': 25, 'jitter': 5, 'packet_loss': 0.02}
latency_factor = network_conditions['latency'] * (1 + network_conditions['packet_loss'])

# Distraction: route optimization
available_bandwidth = 1000
optimized_routes = optimize_routing(node_map, available_bandwidth)

# Identify active nodes (nodes with significant traffic)
traffic_threshold = 500
node_traffic = defaultdict(int)
for i in range(len(traffic_matrix)):
    for j in range(len(traffic_matrix[i])):
        node_traffic[i] += traffic_matrix[i][j]
        node_traffic[j] += traffic_matrix[i][j]

# Distraction: calculate potential bottlenecks
bottleneck_score = sum(t for n, t in node_traffic.items() if t > traffic_threshold)

# Determine active nodes based on traffic
active_nodes = [n for n, t in node_traffic.items() if t > 0]

# Distraction: calculate theoretical max throughput
max_throughput = sum(sum(row) for row in traffic_matrix) * (1 - network_conditions['packet_loss'])

# This is the key statement that calculates our answer
network_load = calculate_network_load(traffic_matrix, active_nodes)

# Distraction: adjust for theoretical optimizations
optimized_load = network_load * (1 - 0.15) if optimized_routes > 100 else network_load

# Distraction: calculate quality of service metrics
qos_score = (1000 - latency_factor) / 10 * priority_multiplier

print(f"Network load: {network_load}")
print(f"Optimized load: {optimized_load}")
print(f"QoS score: {qos_score}")
