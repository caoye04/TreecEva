def analyze_routing_efficiency(nodes, loads):
    total_bandwidth = 0
    peak_utilization = 0
    utilization_history = []

    for idx, (node, load) in enumerate(zip(nodes, loads)):
        base_capacity = len(node['name']) * 15
        redundancy_factor = node.get('redundancy', 1.0)
        security_overhead = node['security_level'] * 3.5 if 'security_level' in node else 0

        # Irrelevant computation - simulates logging overhead
        log_entry = f"Node {node['name']} at index {idx} processed."
        log_length = len(log_entry)

        # Real computation path
        active_interfaces = node['interfaces'] if 'interfaces' in node else 1
        adjusted_capacity = (base_capacity * active_interfaces * redundancy_factor)

        current_utilization = load / adjusted_capacity if adjusted_capacity > 0 else 0
        utilization_history.append(current_utilization)

        if current_utilization > peak_utilization:
            peak_utilization = current_utilization

        total_bandwidth += adjusted_capacity

    avg_utilization = sum(utilization_history) / len(utilization_history) if utilization_history else 0
    efficiency_score = total_bandwidth * (1 - peak_utilization)  # Higher bandwidth and lower peak = better

    return total_bandwidth, avg_utilization, efficiency_score


def calculate_utilization(network_nodes, traffic_load):
    debug_flags = [False, True, False]
    temp_results = {}

    for i, flag in enumerate(debug_flags):
        if flag:
            # Dead code branch - never executed
            temp_results[f'debug_{i}'] = "diagnostic_active"

    # Misleading variable - unused in final logic
    baseline_estimate = len(network_nodes) * 100

    # Core calculation
    _, avg_usage, score = analyze_routing_efficiency(network_nodes, traffic_load)
    scaling_factor = 0.85 if avg_usage < 0.6 else 0.65

    # Final result based on efficiency score and scaling
    final_capacity = int(score * scaling_factor)

    # Red herring: irrelevant string processing
    status_msg = "System nominal"
    status_code = ''.join([chr(ord(c) + 1) for c in status_msg])  # Obfuscated message, not used

    return final_capacity

# Input data
network_nodes = [
    {'name': 'router_A', 'interfaces': 4, 'redundancy': 1.2, 'security_level': 3},
    {'name': 'switch_B', 'interfaces': 8, 'redundancy': 1.5, 'security_level': 2},
    {'name': 'gateway_C', 'interfaces': 2, 'redundancy': 1.1, 'security_level': 4},
    {'name': 'bridge_D', 'interfaces': 6, 'security_level': 1}
]

traffic_load = [120, 300, 85, 200]

# Execution point
final_capacity = calculate_utilization(network_nodes, traffic_load)
print(f"Result: {final_capacity}")