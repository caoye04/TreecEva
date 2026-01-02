from collections import defaultdict

def calculate_remaining_capacity(node_list, max_load):
    load_map = defaultdict(int)
    temp_sum = 0
    
    for node in node_list:
        zone = node['zone']
        load = node['load']
        load_map[zone] += load
        temp_sum += load
    
    overused_zones = set()
    total_capacity = len(node_list) * max_load
    used_capacity = sum(load_map.values())
    
    for zone, load in load_map.items():
        if load > max_load:
            overused_zones.add(zone)
    
    # Some irrelevant tracking
    debug_info = {'zones_count': len(load_map), 'overused': len(overused_zones)}
    
    final_capacity = total_capacity - used_capacity
    
    return final_capacity

# System node distribution across zones
test_nodes = [
    {'zone': 'A', 'load': 8},
    {'zone': 'B', 'load': 12},
    {'zone': 'A', 'load': 7},
    {'zone': 'C', 'load': 15},
    {'zone': 'B', 'load': 3},
    {'zone': 'D', 'load': 10}
]
max_system_load = 20

final_capacity = calculate_remaining_capacity(test_nodes, max_system_load)
print(f"Result: {final_capacity}")