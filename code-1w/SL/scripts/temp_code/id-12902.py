import math

# Simulated network node diagnostics with mixed computational paradigms
def analyze_node_health(node_data, threshold=0.75):
    # Irrelevant transformation (distractor)
    normalized_power = [math.log(p + 1) for p in node_data['power_levels']]
    
    # Relevant logic: count nodes above threshold
    signal_strengths = node_data['signals']
    stable_count = sum(1 for s in signal_strengths if s > threshold)
    
    # Misleading intermediate calculation (dead path)
    avg_latency = sum(node_data['latency']) / len(node_data['latency'])
    if avg_latency < 50:
        jitter_score = 0.9
    else:
        jitter_score = 0.3
    
    return stable_count

def compute_redundancy_index(config_map):
    # Complex but irrelevant bit manipulation (red herring)
    index = 0
    for key, value in config_map.items():
        index ^= hash(str(value)) & 0xFFFF
    return index % 100

def evaluate_failover_risk(nodes, backup_links):
    risk_score = 0
    for i, node in enumerate(nodes):
        load = node['load']
        active_links = node['links']
        # Logical operations with short-circuiting (partially relevant)
        if load > 0.8 and (i in backup_links or load > 0.95):
            risk_score += 1
    return risk_score

def system_status_tracker(node_cluster):
    # Key data structures
    health_metrics = {}
    diagnostic_log = []
    
    # Step 1: Extract core signals
    all_signals = []
    for zone, nodes in node_cluster.items():
        zone_signals = [n['signal'] for n in nodes]
        all_signals.extend(zone_signals)
    
    # Step 2: Prepare node data (only some fields are used)
    fused_data = {
        'signals': all_signals,
        'power_levels': [n['power'] for nodes in node_cluster.values() for n in nodes],
        'latency': [50 + i*3 for i in range(len(all_signals))]  # Fake latency data
    }
    
    # Step 3: Compute health (this is where real logic begins)
    healthy_nodes = analyze_node_health(fused_data)
    health_metrics['stable'] = healthy_nodes
    
    # Step 4: Redundant safety check (distractor)
    config_snapshot = {'version': '2.1.9', 'mode': 'active', 'nodes': len(all_signals)}
    redundancy = compute_redundancy_index(config_snapshot)
    health_metrics['redundancy'] = redundancy
    
    # Step 5: Risk evaluation with tuple unpacking (mixed relevance)
    primary_nodes = [(n['load'], n['links']) for nodes in node_cluster.values() for n in nodes]
    backup_indices = [i for i, n in enumerate(primary_nodes) if n[0] < 0.2]
    failover_risk = evaluate_failover_risk([
        {'load': load, 'links': links} for load, links in primary_nodes
    ], backup_indices)
    
    # Step 6: Diagnostic fusion via dictionary operations
    status_map = {
        0: 100, 1: 90, 2: 80, 3: 70, 4: 60, 5: 50,
        6: 40, 7: 30, 8: 20, 9: 10, 10: 0
    }
    base_score = status_map.get(healthy_nodes, 25)
    
    # Step 7: Apply risk adjustment using logical operations
    override_flag = failover_risk > 3 and not (redundancy > 80 or base_score == 100)
    adjustment_factor = 0.85 if override_flag else 1.0
    
    # Step 8: Final computation chain
    raw_diagnostic = base_score * adjustment_factor
    
    # Step 9: Decoy transformation (never used)
    smoothed = round(raw_diagnostic + math.sin(len(all_signals)), 2)
    diagnostic_log.append(smoothed)
    
    # Step 10: Actual final result
    final_diagnostic = int(round(raw_diagnostic))
    
    # Step 11: Dead code path with misleading print
    if final_diagnostic < 0:
        print("Critical failure cascade detected")
    
    # Step 12: Return true answer
    return final_diagnostic

# Simulated input data
network_topology = {
    'zone_a': [
        {'signal': 0.82, 'power': 45, 'load': 0.65, 'links': 3},
        {'signal': 0.67, 'power': 52, 'load': 0.71, 'links': 2},
        {'signal': 0.91, 'power': 38, 'load': 0.55, 'links': 4}
    ],
    'zone_b': [
        {'signal': 0.76, 'power': 48, 'load': 0.82, 'links': 3},
        {'signal': 0.54, 'power': 55, 'load': 0.49, 'links': 1},
        {'signal': 0.95, 'power': 41, 'load': 0.68, 'links': 5}
    ],
    'zone_c': [
        {'signal': 0.88, 'power': 50, 'load': 0.77, 'links': 2},
        {'signal': 0.43, 'power': 60, 'load': 0.35, 'links': 3}
    ]
}

# Execute main logic
final_diagnostic = system_status_tracker(network_topology)
print(f"Target result: {final_diagnostic}")