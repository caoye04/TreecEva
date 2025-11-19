import itertools

def transmission_efficiency(nodes, depth=0):
    if depth > 3:
        return 0
    if nodes <= 1:
        return nodes
    
    # Calculate base efficiency using bitwise operations
    base = (nodes & (nodes - 1)) ^ (nodes >> 1)
    
    # Recursive calculation with modified node count
    recursive_part = transmission_efficiency(nodes // 2, depth + 1)
    
    # Combine using combinatorial logic
    combinations = list(itertools.combinations(range(min(nodes, 4)), 2))
    combo_count = len(combinations)
    
    # Efficiency adjustment based on comparisons
    adjusted = base + combo_count if base < combo_count else base - combo_count
    
    return adjusted + recursive_part

# Initial network nodes
network_nodes = 12
final_efficiency = transmission_efficiency(network_nodes)
print(f'Result: {final_efficiency}')