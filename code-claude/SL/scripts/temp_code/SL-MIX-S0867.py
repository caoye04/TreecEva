from collections import Counter, defaultdict

def analyze_packet_loss(packets):
    # Misleading function that analyzes packet data
    dropped = sum(1 for p in packets if p < 0)
    received = len(packets) - dropped
    if received == 0:
        return 100.0  # All packets lost
    return (dropped / len(packets)) * 100.0

def optimize_routing(routes, bandwidth):
    # Distraction function for network optimization
    priority_routes = {}
    for route, traffic in routes.items():
        if traffic > bandwidth * 0.8:
            priority_routes[route] = traffic * 1.2
        else:
            priority_routes[route] = traffic * 0.9
    return priority_routes

def calculate_network_health(devices, connections):
    # This is the key function that determines the answer
    active_count = sum(1 for d in devices if d['status'] == 'active')
    inactive_count = len(devices) - active_count
    
    # Calculate connection strength using bit operations
    connection_strength = 0
    for src, targets in connections.items():
        if src % 2 == 0:  # Even-numbered source devices
            connection_strength |= (1 << (src % 7))
        else:  # Odd-numbered source devices
            connection_strength ^= (len(targets) << 1)
    
    # Process device metrics (relevant)
    reliability_score = 0
    for device in devices:
        if device['status'] == 'active':
            # XOR device ID with its uptime to create a reliability factor
            device_factor = device['id'] ^ (device['uptime'] // 10)
            reliability_score += device_factor & 0x0F  # Take lower 4 bits
    
    # Calculate redundancy factor (distractor)
    redundancy = defaultdict(int)
    for src, targets in connections.items():
        for target in targets:
            redundancy[target] += 1
    
    # This is a distractor calculation
    avg_redundancy = sum(redundancy.values()) / max(1, len(redundancy))
    
    # Misleading latency calculation
    latency_metrics = [d.get('latency', 50) for d in devices if d['status'] == 'active']
    latency_distribution = Counter(latency_metrics)
    highest_latency = max(latency_metrics) if latency_metrics else 0
    
    # Calculate network stability index (distractor)
    stability_index = (active_count * 5) - (inactive_count * 3) + connection_strength
    
    # Final health calculation - the actual determinant of the answer
    # The key insight: only active_count, reliability_score and connection_strength matter
    health = ((active_count * 10) + reliability_score - (connection_strength % 13)) % 100
    
    # Apply a scaling factor based on slicing operations on the device IDs
    device_ids = [d['id'] for d in devices]
    if len(device_ids) >= 4:
        scaling = sum(device_ids[1:4:2]) / 10.0
        health = (health * scaling) % 100
    
    return round(health, 2)

# Setup test data
packets = [-5, 10, 15, -3, 20, 25, -8]  # Distractor data
packet_loss = analyze_packet_loss(packets)  # Unused result

# Network configuration (the actual data used)
active_devices = [
    {'id': 12, 'status': 'active', 'uptime': 45, 'latency': 20},
    {'id': 7, 'status': 'inactive', 'uptime': 0, 'latency': 0},
    {'id': 9, 'status': 'active', 'uptime': 120, 'latency': 15},
    {'id': 3, 'status': 'active', 'uptime': 60, 'latency': 25},
    {'id': 18, 'status': 'active', 'uptime': 30, 'latency': 30}
]

# Connection mapping between devices
connection_map = {
    12: [3, 9],
    9: [12, 3, 18],
    3: [9],
    18: [9]
}

# Distractor data and operations
bandwidth_allocation = {f"route_{i}": i*10 for i in range(1, 6)}
optimized_routes = optimize_routing(bandwidth_allocation, 30)  # Unused result

# Process some string data as distraction
network_logs = "ERROR:192.168.1.1;OK:10.0.0.5;WARNING:172.16.0.1"
log_entries = network_logs.split(';')
log_status = [entry.split(':')[0] for entry in log_entries]
error_count = log_status.count("ERROR")

# The key calculation
network_health = calculate_network_health(active_devices, connection_map)

# Some more distractor operations after the key calculation
health_category = "Good" if network_health > 70 else "Fair" if network_health > 40 else "Poor"
network_load = sum(len(targets) for targets in connection_map.values()) * 2.5

# Print the result
print(f"Network health score: {network_health}")
print(f"Health category: {health_category}")
print(f"Network load: {network_load}")
