def calculate_node_weight(attrs):
    base = attrs['cores'] * 1.5
    overhead = attrs['latency'] * 0.2
    return base - overhead


def calculate_network_capacity(nodes):
    total = 0
    for node_id, attrs in nodes.items():
        if attrs['status'] == 'active':
            weight = calculate_node_weight(attrs)
            total += weight * attrs['availability']
    return int(total)

# System node configuration
nodes = {
    'node_a': {'cores': 8, 'latency': 10, 'status': 'active', 'availability': 0.95},
    'node_b': {'cores': 12, 'latency': 5, 'status': 'active', 'availability': 0.98},
    'node_c': {'cores': 6, 'latency': 20, 'status': 'inactive', 'availability': 0.90},
    'node_d': {'cores': 16, 'latency': 8, 'status': 'active', 'availability': 0.93}
}

initial_count = len(nodes)
dummy_flag = False

# Main computation
total_capacity = calculate_network_capacity(nodes)

print(f"Result: {total_capacity}")