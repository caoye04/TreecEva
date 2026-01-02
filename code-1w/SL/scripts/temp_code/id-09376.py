def calculate_utilization(nodes):
    # Irrelevant pre-processing: sorting by name (has no impact on result)
    sorted_names = sorted([n['name'] for n in nodes])
    temp_sum = sum(len(name) for name in sorted_names)

    # Semi-relevant transformation: map node status using lambda
    status_map = list(map(lambda x: 1 if x['active'] else 0, nodes))

    # Core logic: compute weighted capacity based on tier and load
    base_capacities = []
    for node in nodes:
        if node['tier'] == 'A':
            cap = node['base'] * 1.5
        elif node['tier'] == 'B':
            cap = node['base'] * 1.2
        else:
            cap = node['base'] * 1.0
        
        # Adjust by current load factor
        cap -= node['load']
        base_capacities.append(cap)
    
    # Secondary adjustment based on redundancy count (only some nodes contribute)
    redundancy_bonus = 0
    for node in nodes:
        if node['redundant'] and node['tier'] in ['A', 'B']:
            redundancy_bonus += 5

    # Distractor: unused computation involving string methods
    all_ids = ''.join([n['name'].upper().strip() for n in nodes])
    checksum = len(all_ids.replace('NODE', '')) * 2  # Not used

    # Final aggregation
    raw_total = sum(base_capacities)
    adjusted_total = raw_total + redundancy_bonus
    
    return int(adjusted_total)

# Define network configuration
network_nodes = [
    {'name': 'node-alpha', 'base': 40, 'tier': 'A', 'load': 10, 'active': True, 'redundant': True},
    {'name': 'node-beta',  'base': 30, 'tier': 'B', 'load': 8,  'active': False, 'redundant': True},
    {'name': 'node-gamma', 'base': 50, 'tier': 'C', 'load': 15, 'active': True, 'redundant': False},
    {'name': 'node-delta', 'base': 35, 'tier': 'A', 'load': 5,  'active': True, 'redundant': True}
]

# Execute main logic
initial_estimate = sum(n['base'] for n in network_nodes)  # distractor variable
auxiliary_data = {n['name']: len(n['name']) % 3 for n in network_nodes}  # dead code path

final_capacity = calculate_utilization(network_nodes)
print(f"Result: {final_capacity}")