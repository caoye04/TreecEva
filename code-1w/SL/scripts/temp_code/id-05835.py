def calculate_system_capacity(nodes, redundancy_pool):
    base_power = sum([n[1] * 1.5 for n in nodes])
    stability_score = len(nodes) * 0.8 + len(redundancy_pool) * 0.2
    
    # Irrelevant computation: historical load simulation (dead-end)
    historical_loads = [base_power * 0.9, base_power * 1.1, base_power * 0.8]
    avg_historical = sum(historical_loads) / len(historical_loads)
    fluctuation = avg_historical * 0.05  # unused beyond this

    # Semi-relevant filtering: only active nodes contribute
    active_nodes = set([n[0] for n in nodes if n[2] == 'ACTIVE'])
    dormant_nodes = set([n[0] for n in nodes if n[2] == 'DORMANT'])
    available spares = redundancy_pool.intersection(active_nodes)  # misleading name, not used

    # Core logic: capacity depends on active node power and overlap with backup
    overlap_count = len(redundancy_pool.intersection(active_nodes))
    redundancy_boost = overlap_count * 1.75

    # Distractor: complex but unused state tracker
    system_state = {}
    for node_id in active_nodes:
        system_state[node_id] = {
            'status': 'OPTIMAL',
            'load': base_power / (len(active_nodes) + 1),
            'fallback': node_id in redundancy_pool
        }
    
    # Another red herring: environmental factor calculation
    env_factor = 1.0
    temperature = 22.5
    if temperature > 20:
        env_factor *= 0.98
    humidity = 45
    if 30 < humidity < 60:
        env_factor *= 1.01
    # env_factor never applied

    # Key computation
    final_capacity = int(base_power + redundancy_boost)
    return final_capacity

# System configuration data
node_configurations = [
    ('N1', 40, 'ACTIVE'),
    ('N2', 30, 'DORMANT'),
    ('N3', 50, 'ACTIVE'),
    ('N4', 20, 'ACTIVE'),
    ('N5', 35, 'DORMANT')
]

# Backup node identifiers
backup_identifiers = set(['N1', 'N3', 'N7', 'N9'])

# Intermediate variables for distraction
consistency_check = len(node_configurations) >= len(backup_identifiers)
system_mode = 'STANDBY' if not consistency_check else 'ACTIVE'
mode_weight = 1.0 if system_mode == 'ACTIVE' else 0.5  # unused

# Performance tier classification (distractor)
tier_A = tuple(n[0] for n in node_configurations if n[1] >= 40)
tier_B = tuple(n[0] for n in node_configurations if 20 <= n[1] < 40)

optimal_nodes = [n for n in node_configurations if n[0] in tier_A or n[2] == 'ACTIVE']

# Critical execution point
final_capacity = calculate_system_capacity(optimal_nodes, backup_identifiers)
print(f"Result: {final_capacity}")