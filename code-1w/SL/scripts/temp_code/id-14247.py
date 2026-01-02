from collections import defaultdict

# Simulate network link utilization across redundant paths
def calculate_network_capacity(links, redundancy):
    base_capacities = defaultdict(float)
    scaling_factor = 1.0 + (redundancy * 0.1)
    
    for link_id, speed in links.items():
        if speed > 100:
            base_capacities[link_id] = speed * scaling_factor
        else:
            base_capacities[link_id] = speed * 0.9
    
    total = sum(base_capacities.values())
    return int(total)

# Irrelevant utility function (minimal distraction)
def format_bytes(size):
    return f'{size} B'

# Network configuration
link_speeds = {
    'core_a': 1000,
    'core_b': 1000,
    'edge_x': 100,
    'edge_y': 50,
    'backup_z': 200
}

redundancy_factor = 3
total_capacity = calculate_network_capacity(link_speeds, redundancy_factor)

# Logging (non-interfering)
status = 'active'

Result: {total_capacity}