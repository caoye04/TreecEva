def calculate_overlap(nodes_a, nodes_b):
    return len(set(nodes_a) & set(nodes_b))


def calculate_density_score(node_list, region_map):
    # Irrelevant calculation - not used in final result
    total = 0
    for region in region_map.values():
        total += len(set(node_list) & set(region))
    return total / (len(node_list) + 1)


def calculate_remaining_capacity(active, reserved, factor):
    active_set = set(active)
    reserved_set = set(reserved)
    
    # Core logic step 1: Find overlapping nodes
    overlap = len(active_set & reserved_set)
    
    # Core logic step 2: Adjust active count by removing duplicates
    adjusted_active = len(active_set) - overlap
    
    # Core logic step 3: Reserved capacity adjustment
    adjusted_reserved = len(reserved_set) // 2
    
    # Core logic step 4: Apply scaling factor based on system load
    if adjusted_active > 10:
        factor *= 1.2
    elif adjusted_active < 5:
        factor *= 0.8
    
    # Core logic step 5: Compute base capacity
    base_capacity = (adjusted_active * 3) + (adjusted_reserved * 2)
    
    # Core logic step 6: Final scaling
    final = int(base_capacity * factor)
    
    return final

# Simulation data
node_ids = [f'N{i}' for i in range(100)]
region_config = {
    'east': node_ids[10:25],
    'west': node_ids[30:45],
    'north': node_ids[50:70]
}

# Actual inputs for computation
available_nodes = ['N1', 'N3', 'N4', 'N7', 'N9', 'N11', 'N13', 'N14', 'N17', 'N19', 'N20', 'N21']
reserved_nodes = ['N7', 'N9', 'N12', 'N14', 'N17', 'N19', 'N22', 'N25']
scaling_factor = 1.5

# Dead code - distractor (misleading usage)
baseline_utilization = sum(len(v) for v in region_config.values()) / len(node_ids)
density_metric = calculate_density_score(available_nodes, region_config)

# Key statement
final_capacity = calculate_remaining_capacity(available_nodes, reserved_nodes, scaling_factor)

print(f"Result: {final_capacity}")