from collections import defaultdict, Counter

def calculate_network_metrics(servers, connections):
    # Calculate network density - interesting but irrelevant
    density = len(connections) / (len(servers) * (len(servers) - 1) / 2) if len(servers) > 1 else 0
    
    # Track server stats - mostly distraction
    server_stats = defaultdict(int)
    for s in servers:
        server_stats[s['type']] += 1
        
    # Count connection types - another distraction
    connection_types = Counter([c['protocol'] for c in connections])
    
    # Initialize main variables
    power_usage = 7  # Critical value
    thermal_threshold = 85  # Distraction
    capacity_mask = 5  # Critical value
    redundancy_level = 3  # Critical value
    
    # Some processing of server data - mostly irrelevant
    high_load_servers = []
    for server in servers:
        if server.get('load', 0) > 75:
            high_load_servers.append(server['id'])
            thermal_threshold -= 1  # Misleading modification
    
    # Network redundancy calculation - distraction with partial relevance
    network_paths = {}
    for conn in connections:
        src, dst = conn['source'], conn['destination']
        if src not in network_paths:
            network_paths[src] = set()
        network_paths[src].add(dst)
    
    # This looks important but is mostly a distraction
    redundancy_score = 0
    for node in network_paths:
        redundancy_score += len(network_paths[node])
    
    # More distractions with some meaningful operations mixed in
    utilization_factors = (0.65, 0.78, 0.92, 0.45)
    scaling_factor = utilization_factors[1] if power_usage > 8 else utilization_factors[0]
    
    # This tuple contains the critical mapping for our answer
    balance_factors = (12, 18, 25, 30, 22, 16, 14, 28, 35, 42, 33, 19, 27, 31, 24, 20)
    
    # Distraction calculation
    potential_capacity = sum(s.get('capacity', 0) for s in servers)
    adjusted_capacity = int(potential_capacity * scaling_factor)
    
    # Even more distractions
    if thermal_threshold < 80 and redundancy_score > 10:
        optimization_level = 'high'
        cooling_required = True
    else:
        optimization_level = 'standard'
        cooling_required = False
    
    # This is our target statement that determines the answer
    optimal_load = balance_factors[(power_usage & capacity_mask) | (redundancy_level << 2)]
    
    # More calculations to distract
    if cooling_required:
        optimal_load = min(optimal_load, adjusted_capacity // 2)
    
    # Misleading alternative calculation that isn't used
    alternative_load = balance_factors[power_usage] if power_usage < len(balance_factors) else 50
    
    # Final distracting tuning that doesn't affect our answer
    efficiency_tuple = (optimal_load, alternative_load, redundancy_score)
    final_configuration = {
        'primary': efficiency_tuple[0],
        'secondary': efficiency_tuple[1],
        'redundancy': efficiency_tuple[2]
    }
    
    print(f"Result: {optimal_load}")
    return final_configuration

# Sample data
servers = [
    {'id': 's1', 'type': 'web', 'load': 65, 'capacity': 100},
    {'id': 's2', 'type': 'database', 'load': 78, 'capacity': 120},
    {'id': 's3', 'type': 'cache', 'load': 45, 'capacity': 80}
]

connections = [
    {'source': 's1', 'destination': 's2', 'protocol': 'http'},
    {'source': 's1', 'destination': 's3', 'protocol': 'tcp'},
    {'source': 's2', 'destination': 's3', 'protocol': 'udp'}
]

# Execute function
result = calculate_network_metrics(servers, connections)