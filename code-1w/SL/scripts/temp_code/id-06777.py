def analyze_network_load(node_metrics, traffic_log):
    total_nodes = len(node_metrics)
    peak_utilization = max(node_metrics.values())
    avg_latency = sum([v['latency'] for v in traffic_log.values()]) / len(traffic_log)
    
    # Irrelevant aggregation
    dummy_sum = 0
    for k in traffic_log:
        if 'error' in traffic_log[k]:
            dummy_sum += traffic_log[k]['error']
    
    threshold = 0.75 * peak_utilization
    congested_nodes = [nid for nid, util in node_metrics.items() if util > threshold]
    
    return congested_nodes, avg_latency


def calculate_path_efficiency(route_list, link_weights):
    efficiency_scores = {}
    for route in route_list:
        score = 1.0
        for i in range(len(route) - 1):
            pair = tuple(sorted([route[i], route[i+1]]))
            score *= link_weights.get(pair, 0.8)
        efficiency_scores[tuple(route)] = round(score, 4)
    
    # Dead computation - not used later
    normalized = {k: v / (sum(efficiency_scores.values()) + 1e-8) for k, v in efficiency_scores.items()}
    
    return efficiency_scores


def optimize_routing(flow_matrix, node_capacity):
    routes = list(flow_matrix.keys())
    adjustments = 0
    
    base_flow = sum(flow_matrix[r] for r in routes)
    capacity_ratio = sum(node_capacity.values()) / (len(node_capacity) + 1e-8)
    
    temp_grid = [[i*j for j in range(3)] for i in range(3)]  # Unused matrix computation
    
    scaling_factor = 0.9 if capacity_ratio < 50 else 1.1
    
    # Simulate iterative tuning
    for _ in range(2):
        new_flows = {}
        for route in routes:
            nodes_in_route = [int(n.split('_')[1]) for n in route.split('-')]
            min_cap = min(node_capacity[f'node_{n}'] for n in nodes_in_route)
            new_flows[route] = flow_matrix[route] * (min_cap / 100) * scaling_factor
        flow_matrix = new_flows
        adjustments += 1
    
    final_estimate = sum(flow_matrix.values()) * scaling_factor
    
    # Extra distraction
    outlier_check = [f for f in flow_matrix.values() if f > 2 * final_estimate / len(flow_matrix)]
    
    return int(round(final_estimate))

# Main execution
if __name__ == '__main__':
    node_metrics = {
        'node_1': 68,
        'node_2': 82,
        'node_3': 45,
        'node_4': 91,
        'node_5': 73
    }

    traffic_log = {
        'link_A': {'latency': 12, 'retries': 1},
        'link_B': {'latency': 18, 'retries': 0},
        'link_C': {'latency': 15, 'retries': 2},
        'link_D': {'latency': 20, 'error': 3}
    }

    link_weights = {
        ('A', 'B'): 0.85,
        ('B', 'C'): 0.75,
        ('C', 'D'): 0.9,
        ('A', 'D'): 0.65
    }

    routes = [
        'node_1-node_2-node_4',
        'node_1-node_3-node_4',
        'node_5-node_2-node_4'
    ]

    flow_matrix = {
        'node_1-node_2-node_4': 120,
        'node_1-node_3-node_4': 80,
        'node_5-node_2-node_4': 100
    }

    node_capacity = {
        'node_1': 100,
        'node_2': 85,
        'node_3': 90,
        'node_4': 95,
        'node_5': 80
    }

    # Step 1: Analyze network load (produces unused data)
    congested, avg_lat = analyze_network_load(node_metrics, traffic_log)
    
    # Step 2: Calculate path efficiency (semi-relevant, but only structure matters)
    efficiencies = calculate_path_efficiency(routes, link_weights)
    
    # Key statement
    final_bandwidth = optimize_routing(flow_matrix, node_capacity)
    
    # Use slicing and dictionary operations as required
    recent_routes = list(efficiencies.keys())[1:]
    active_segments = {k: v for k, v in node_capacity.items() if v > 85}
    
    print(f"Result: {final_bandwidth}")