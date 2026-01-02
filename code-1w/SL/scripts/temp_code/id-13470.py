from itertools import combinations

def analyze_fragment_overlap(fragments):
    # Irrelevant helper: computes pairwise string overlaps (not used in final result)
    overlap_score = 0
    for a, b in combinations(fragments, 2):
        for i in range(1, min(len(a), len(b)) + 1):
            if a.endswith(b[:i]):
                overlap_score += i
    return overlap_score

def validate_allocation(allocation, constraints):
    # Semi-relevant: checks if allocation fits constraints (used once in logic)
    return all(allocation[i] <= constraints[i] for i in range(len(constraints)))

def calculate_remaining_capacity(storage_map, allocation_list):
    total_storage = sum(storage_map.values())
    reserved = 0
    temp_buffer = []
    
    # Simulate allocation process with filtering
    for item in allocation_list:
        name = item['name']
        size = item['size']
        priority = item.get('priority', 1)
        
        # Misleading filter: high priority items get buffered (but buffer unused)
        if priority > 2:
            temp_buffer.append(size * 1.5)  # inflated for 'priority handling'
        elif priority == 2:
            reserved += size * 0.9  # partial reservation
        else:
            reserved += size
    
    # Dead code path: only triggers on non-existent 'critical' flag
    emergency_reserve = 0
    for item in allocation_list:
        if item.get('critical', False):
            emergency_reserve += item['size'] * 2  # never executed
    
    # Actual capacity logic
    available_keys = [k for k in storage_map.keys() if 'backup' not in k]
    primary_capacity = sum(storage_map[k] for k in available_keys)
    
    # Red herring sort: sorts allocations by name length (unused later)
    sorted_names = sorted([item['name'] for item in allocation_list], key=len)
    name_entropy = sum(len(n) for n in sorted_names) % 7  # irrelevant metric
    
    # Final computation
    base_used = sum(item['size'] for item in allocation_list)
    efficiency_ratio = 0.85 if base_used > 200 else 0.7
    effective_used = base_used * efficiency_ratio
    
    final_capacity = int(primary_capacity - effective_used)
    
    # Print required output
    print(f"Result: {final_capacity}")
    return final_capacity

# Setup data
storage_map = {
    'node_a': 120,
    'node_b': 180,
    'backup_node_x': 90,
    'node_c': 150
}

allocation_list = [
    {'name': 'config', 'size': 45, 'priority': 1},
    {'name': 'logs', 'size': 80, 'priority': 2},
    {'name': 'cache', 'size': 60, 'priority': 1},
    {'name': 'temp_data', 'size': 35, 'priority': 3},  # goes to temp_buffer (unused)
    {'name': 'metadata', 'size': 25, 'priority': 1}
]

# Call function
fragments = [item['name'] for item in allocation_list]
analyze_fragment_overlap(fragments)  # called but result ignored
final_capacity = calculate_remaining_capacity(storage_map, allocation_list)