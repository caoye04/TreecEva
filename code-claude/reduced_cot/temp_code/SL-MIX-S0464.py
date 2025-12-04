import itertools

def calculate_optimal_capacity(containers):
    # Extract only the relevant container information
    valid_containers = [(volume, weight) for volume, weight, durability in containers if weight > 0]
    
    # Sort by volume efficiency (higher is better)
    valid_containers.sort(key=lambda x: x[0]/x[1] if x[1] > 0 else 0, reverse=True)
    
    # Calculate the optimal capacity based on weight distribution
    total_volume = sum(v for v, w in valid_containers)
    total_weight = sum(w for v, w in valid_containers)
    
    # Apply weight adjustment factor
    weight_factor = 0.75
    adjusted_weight = total_weight * weight_factor
    
    # These calculations don't affect the final result
    max_volume = max(v for v, w in valid_containers) if valid_containers else 0
    min_weight = min(w for v, w in valid_containers) if valid_containers else 0
    ratio_product = max_volume * min_weight
    
    # Calculate container combinations (unused in final result)
    combinations = list(itertools.combinations(valid_containers, 2))
    combination_count = len(combinations)
    
    # Calculate the balance factor
    if total_weight > 0:
        balance_factor = (total_volume / total_weight) * 1.25
    else:
        balance_factor = 0
    
    # Apply efficiency correction based on container count
    efficiency = 1.0
    if len(valid_containers) > 3:
        efficiency = 1.1
    elif len(valid_containers) > 1:
        efficiency = 0.95
    
    # Calculate optimal capacity
    optimal_capacity = int(total_volume * efficiency)
    
    return optimal_capacity

# Container data: (volume, weight, durability)
container_data = [
    (120, 30, 8),
    (90, 20, 6),
    (150, 40, 9),
    (80, 0, 7),   # Invalid due to zero weight
    (110, 25, 5)
]

# Calculate the optimal capacity
optimal_capacity = calculate_optimal_capacity(container_data)
print(f"Result: {optimal_capacity}")
