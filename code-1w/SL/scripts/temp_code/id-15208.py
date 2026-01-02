def analyze_system_load(resources, limit):
    active_nodes = [r for r in resources if r['load'] > limit]
    inactive_nodes = [r for r in resources if r['load'] <= limit]
    
    # Irrelevant transformation (distractor)
    temp_snapshot = [node['id'] + '_tmp' for node in inactive_nodes]
    temp_snapshot.reverse()

    total_capacity = sum(node['capacity'] for node in resources)
    utilized_capacity = sum(node['capacity'] for node in active_nodes)
    
    # Misleading intermediate calculation (not used in final result)
    avg_load = sum(node['load'] for node in resources) / len(resources) if resources else 0
    peak_load_node = max(resources, key=lambda x: x['load']) if resources else None
    
    # Red herring: calculating unused capacity but not using it directly
    unused_capacity = total_capacity - utilized_capacity
    capacity_ratio = utilized_capacity / total_capacity if total_capacity > 0 else 0
    
    # Key distraction: complex filtering that isn't part of answer
    over_threshold_groups = {}
    for node in active_nodes:
        group = node['region']
        if group not in over_threshold_groups:
            over_threshold_groups[group] = 0
        over_threshold_groups[group] += node['capacity']

    # Actual logic step: find nodes with balanced load and add their capacity
    balanced_nodes = [n for n in resources if n['load'] == limit * 1.5]
    bonus_capacity = sum(n['capacity'] * 0.5 for n in balanced_nodes)

    # Final computation (depends only on specific chain)
    base_result = utilized_capacity + bonus_capacity
    adjustment = len(active_nodes) * 10
    final_capacity = int(base_result + adjustment)

    return final_capacity

# System configuration data
data_pool = [
    {'id': 'A', 'load': 75, 'capacity': 200, 'region': 'NORTH'},
    {'id': 'B', 'load': 30, 'capacity': 150, 'region': 'SOUTH'},
    {'id': 'C', 'load': 90, 'capacity': 300, 'region': 'NORTH'},
    {'id': 'D', 'load': 45, 'capacity': 100, 'region': 'EAST'},
    {'id': 'E', 'load': 60, 'capacity': 250, 'region': 'SOUTH'}
]

threshold = 60
resource_map = data_pool.copy()

# Modify one entry to create exact condition for balanced_nodes
resource_map[1]['load'] = 90  # Now B has load 90, which is 60*1.5

final_capacity = analyze_system_load(resource_map, threshold)
print(f"Target result: {final_capacity}")