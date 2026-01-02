def evaluate_system_capacity(config):
    base = config['nodes']
    redundancy = config['replicas']
    efficiency = config['efficiency_factor']
    
    # Intermediate calculations with some irrelevant ones
    temp_load = base * 1.8                    # Irrelevant: not used later
    adjusted_nodes = base - (redundancy - 1)  # Relevant: reduces effective nodes
    phantom_threshold = 999                   # Dead variable: never used
    
    nominal_capacity = adjusted_nodes * efficiency
    
    # Simulate resource overlaps using set operations
    active_resources = set(range(0, base * 2, 2))           # Even indices
    backup_resources = set(range(1, base * 2 + 1, 2))         # Odd indices
    overlap = active_resources.intersection(backup_resources)
    conflict_count = len(overlap)                          # Always 0, but computed anyway
    
    # Apply combinatorics: number of ways to assign tasks
    from math import comb
    if adjusted_nodes >= 3:
        task_distributions = comb(adjusted_nodes, 3)       # Relevant for scaling
    else:
        task_distributions = 0
    
    # Scaling factor based on distribution complexity
    scaling = 1.0
    if task_distributions > 10:
        scaling = 1.25
    elif task_distributions > 5:
        scaling = 1.1
        
    # Distractor loop: computes unused metrics
    performance_metrics = []
    for i in range(3):
        metric = (i + 1) * base / (redundancy + 1)
        performance_metrics.append(metric)  # Collected but unused
    
    # Final capacity calculation
    final_capacity = nominal_capacity * scaling
    
    return final_capacity

# Configuration setup
optimal_config = {
    'nodes': 8,
    'replicas': 3,
    'efficiency_factor': 12.5
}

# Execute key statement
final_capacity = evaluate_system_capacity(optimal_config)
print(f"Result: {final_capacity}")