import itertools

def analyze_packet_loss(packets):
    # Red herring function that calculates complex statistics
    dropped = sum(1 for p in packets if p < 0)
    total = len(packets)
    loss_rate = dropped / total if total > 0 else 0
    jitter = sum(abs(packets[i] - packets[i-1]) for i in range(1, len(packets)))
    return (loss_rate * 100, jitter)

def optimize_route(nodes, traffic_weight):
    # Another distraction function
    if traffic_weight > 100:
        return nodes[::-1]
    elif traffic_weight < 0:
        return [n * 2 for n in nodes]
    return nodes[::2] + nodes[1::2]

def calculate_network_stability(packet_data):
    # Core function that determines the answer
    latency_values = [p['latency'] for p in packet_data if 'latency' in p]
    error_counts = [p.get('errors', 0) for p in packet_data]
    
    # Misleading intermediate calculation
    potential_score = sum(latency_values) / (max(error_counts) + 1)
    
    # Extracting key bits from packet flags (critical calculation)
    flags = [p.get('flags', 0) for p in packet_data]
    bit_count = 0
    for flag in flags:
        # Count bits in each flag value
        while flag:
            bit_count += flag & 1
            flag >>= 1
    
    # More distraction calculations
    hop_counts = [p.get('hops', 1) for p in packet_data]
    avg_hops = sum(hop_counts) / len(hop_counts) if hop_counts else 0
    
    # Another misleading path
    if sum(error_counts) > 100:
        return potential_score / 2
    
    # The actual stability formula
    stability = 0
    for i, (latency, errors) in enumerate(zip(latency_values, error_counts)):
        if i % 3 == 0:  # Only process every third packet
            stability += (latency - errors * 2)
    
    # Final calculation with bit influence
    return stability - bit_count * 5

# Setup test data
router_logs = [
    {'id': 101, 'status': 'active', 'load': 78.3},
    {'id': 102, 'status': 'maintenance', 'load': 0},
    {'id': 103, 'status': 'active', 'load': 92.1}
]

# Generate packet data with distracting elements
packet_data = [
    {'seq': 1, 'latency': 30, 'errors': 0, 'flags': 5, 'hops': 3},
    {'seq': 2, 'latency': 45, 'errors': 2, 'flags': 7, 'hops': 4},
    {'seq': 3, 'latency': 25, 'errors': 1, 'flags': 3, 'hops': 2},
    {'seq': 4, 'latency': 60, 'errors': 3, 'flags': 9, 'hops': 5},
    {'seq': 5, 'latency': 20, 'errors': 0, 'flags': 1, 'hops': 2},
    {'seq': 6, 'latency': 50, 'errors': 2, 'flags': 6, 'hops': 3}
]

# Distracting operations
packet_loss, jitter = analyze_packet_loss([-1, 5, 8, -2, 10, -3, 7])
optimal_path = optimize_route([1, 2, 3, 4, 5], packet_loss)

# Another distraction - complex iteration
route_combinations = list(itertools.combinations([r['id'] for r in router_logs if r['status'] == 'active'], 2))
backup_routes = {}
for i, combo in enumerate(route_combinations):
    backup_routes[combo] = i * 10

# The key calculation
network_stability = calculate_network_stability(packet_data)

# Misleading final calculations that aren't used
total_stability = network_stability + sum(backup_routes.values())
adjusted_stability = total_stability / len(packet_data) if packet_data else 0

print(f"Result: {network_stability}")
