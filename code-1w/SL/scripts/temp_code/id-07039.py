def analyze_traffic(flow_data, threshold):
    high_load = set()
    temp_sum = 0
    for flow in flow_data:
        temp_sum += flow['load']
        if flow['load'] > threshold:
            high_load.add(flow['node'])
    return high_load


def calculate_efficiency(nodes, active_set):
    efficiency = 0
    overhead = 0
    for node in nodes:
        if node['id'] in active_set:
            efficiency += node['throughput'] / (node['latency'] + 1)
        else:
            overhead += node['power_draw']
    adjusted = efficiency - overhead * 0.1
    return round(adjusted, 4)


def linear_search(arr, target):
    # Irrelevant helper function for distraction
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def optimize_allocation():
    # System parameters
    network_nodes = [
        {'id': 101, 'throughput': 85, 'latency': 2, 'power_draw': 12},
        {'id': 102, 'throughput': 90, 'latency': 3, 'power_draw': 15},
        {'id': 103, 'throughput': 75, 'latency': 1, 'power_draw': 10},
        {'id': 104, 'throughput': 95, 'latency': 4, 'power_draw': 18}
    ]

    traffic_flows = [
        {'node': 101, 'load': 88},
        {'node': 102, 'load': 95},
        {'node': 103, 'load': 70},
        {'node': 104, 'load': 102}
    ]

    base_threshold = 80
    spike_buffer = 10
    safety_margin = 0.9

    # Simulate some irrelevant bit manipulation
    masked_threshold = base_threshold ^ 15
    masked_threshold = masked_threshold & 127

    # Identify high-load nodes
    congested_nodes = analyze_traffic(traffic_flows, base_threshold)

    # Calculate raw efficiency score
    raw_efficiency = calculate_efficiency(network_nodes, congested_nodes)

    # Dummy search to add noise
    search_result = linear_search([50, 60, 70, 80], base_threshold)

    # Apply safety margin and convert to bandwidth units
    preliminary_bandwidth = raw_efficiency * 10
    final_bandwidth = int(preliminary_bandwidth * safety_margin)

    # Extra unused variables to increase cognitive load
    debug_log = f"Nodes: {len(congested_nodes)}, Search: {search_result}"
    temp_state = {'stage': 'optimized', 'code': 200}
    audit_flag = True if final_bandwidth > 300 else False

    return final_bandwidth

# Execute and print result
target_result = optimize_allocation()
print(f"Target result: {target_result}")