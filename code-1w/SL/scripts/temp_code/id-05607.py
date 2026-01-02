from collections import defaultdict

# Simulate network node health and throughput metrics
def analyze_network_flow():
    node_metrics = [
        {'node': 'A1', 'status': 'active', 'latency_ms': 12, 'throughput_kbps': 850},
        {'node': 'B2', 'status': 'active', 'latency_ms': 18, 'throughput_kbps': 920},
        {'node': 'C3', 'status': 'degraded', 'latency_ms': 45, 'throughput_kbps': 300},
        {'node': 'D4', 'status': 'inactive', 'latency_ms': 0, 'throughput_kbps': 0},
    ]

    # Track status distribution
    status_count = defaultdict(int)
    total_latency = 0
    active_node_count = 0
    peak_throughput = 0
    latency_outliers = []

    for entry in node_metrics:
        status = entry['status']
        status_count[status] += 1
        
        if status == 'active' or status == 'degraded':
            total_latency += entry['latency_ms']
            if entry['latency_ms'] > 40:
                latency_outliers.append(entry['node'])
        
        if status == 'active':
            active_node_count += 1
            if entry['throughput_kbps'] > peak_throughput:
                peak_throughput = entry['throughput_kbps']

    # Compute average latency (only for active/degraded nodes)
    relevant_node_count = status_count['active'] + status_count['degraded']
    avg_latency = total_latency / relevant_node_count if relevant_node_count else 0

    # Simulate packet loss correlation with high latency
    packet_loss_estimate = 0.0
    if avg_latency > 30:
        packet_loss_estimate = round(avg_latency * 0.012, 3)
    elif avg_latency > 20:
        packet_loss_estimate = round(avg_latency * 0.008, 3)
    else:
        packet_loss_estimate = round(avg_latency * 0.005, 3)

    # Distractor: irrelevant computation on string patterns
    node_names = [nm['node'] for nm in node_metrics]
    char_frequency = defaultdict(int)
    for name in node_names:
        for char in name:
            char_frequency[char] += 1
    # End of distractor block

    # System state aggregation
    system_state = {
        'node_count': len(node_metrics),
        'active_count': status_count['active'],
        'degraded_count': status_count['degraded'],
        'avg_latency': avg_latency,
        'packet_loss': packet_loss_estimate,
        'max_throughput': peak_throughput
    }

    # Efficiency model based on operational factors
    base_efficiency = 0.95
    degradation_penalty = 0.15 * status_count['degraded']
    inactive_penalty = 0.10 * status_count['inactive']
    load_balance_ratio = active_node_count / len(node_metrics) if len(node_metrics) else 0

    # Final efficiency factor calculation
    efficiency_factor = base_efficiency - degradation_penalty - inactive_penalty
    efficiency_factor *= (0.8 + 0.2 * load_balance_ratio)  # Scale by balance
    efficiency_factor = max(efficiency_factor, 0.3)  # Floor to prevent collapse

    # Key assignment point
    flow_capacity = system_state.get('max_throughput', 0) * efficiency_factor

    # Additional red herring: unused derived metric
    projected_capacity_growth = flow_capacity * 1.07 if status_count['active'] >= 2 else 0

    # Output target result
    print(f"Result: {flow_capacity}")

    return flow_capacity

analyze_network_flow()