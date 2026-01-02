def calculate_utilization(nodes):
    # Simulate network node capacity analysis with interference
    base_load = 127
    overhead = 0
    temp_buffer = []

    for node in nodes:
        if 'status' not in node or node['status'] != 'active':
            continue

        # Irrelevant signal processing simulation (distractor)
        signal_strength = node.get('signal', 0)
        interference_level = node.get('interference', 0)
        effective_signal = signal_strength - interference_level  # Not used later

        # Real computation path
        capacity = node['capacity']
        usage = node['usage']
        utilization = capacity * (1 - usage / 100)

        # Dead code path (misleading)
        if utilization < 50:
            overhead += 5
            temp_buffer.append(utilization * 0.1)  # Never accessed

        node['available'] = utilization

    # Use dictionary operation to aggregate
    active_caps = {nid: node['available'] for nid, node in enumerate(nodes) if node.get('status') == 'active'}

    # List comprehension with filtering and scaling (core logic)
    scaled_avail = [val * 1.1 for val in active_caps.values() if val > 40]

    # Secondary distraction: simulate latency adjustment (unused)
    latency_correction = 0
    for cap in scaled_avail:
        if cap > 100:
            latency_correction += 0.05

    # Final computation
    final_capacity = sum(scaled_avail) // len(scaled_avail) if scaled_avail else 0

    # Print result as required
    print(f"Target result: {final_capacity}")
    return final_capacity

# Setup realistic input data
network_nodes = [
    {'status': 'active', 'capacity': 200, 'usage': 30, 'signal': 85, 'interference': 20},
    {'status': 'inactive', 'capacity': 150, 'usage': 75, 'signal': 40, 'interference': 35},
    {'status': 'active', 'capacity': 180, 'usage': 45, 'signal': 90, 'interference': 10},
    {'status': 'active', 'capacity': 100, 'usage': 80, 'signal': 70, 'interference': 15},
    {'status': 'active', 'capacity': 220, 'usage': 20, 'signal': 95, 'interference': 5}
]

# Execute function
final_capacity = calculate_utilization(network_nodes)