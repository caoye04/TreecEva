import itertools

def optimize_truck_loading(available_packages, truck_capacity):
    # available_packages is a list of tuples: (weight, priority)
    # Sort by priority descending (greedy approach)
    sorted_packages = sorted(available_packages, key=lambda x: x[1], reverse=True)
    
    selected_packages_weight = 0
    current_load = 0
    
    # Process packages using greedy selection
    for weight, priority in sorted_packages:
        # Short-circuit evaluation to check if adding package exceeds capacity
        if current_load + weight <= truck_capacity and priority > 0:
            current_load += weight
            selected_packages_weight += weight * priority
    
    # Apply set operations to filter high-priority packages
    high_priority_weights = {pkg[0] for pkg in available_packages if pkg[1] >= 8}
    low_priority_set = frozenset(pkg[0] for pkg in available_packages if pkg[1] < 5)
    
    # Use set difference to identify exclusive high-priority packages
    exclusive_high_priority = high_priority_weights - low_priority_set
    
    # Adjust selection using divide and conquer approach on remaining capacity
    remaining_capacity = truck_capacity - current_load
    if remaining_capacity > 0 and exclusive_high_priority:
        # Find best fit using combinations
        best_addition_weight = 0
        for r in range(1, min(3, len(exclusive_high_priority)) + 1):
            for combo in itertools.combinations(exclusive_high_priority, r):
                combo_weight = sum(combo)
                if combo_weight <= remaining_capacity:
                    best_addition_weight = max(best_addition_weight, combo_weight)
        
        selected_packages_weight += best_addition_weight * 2  # Bonus factor
    
    return selected_packages_weight

# Package data: (weight, priority)
packages = [(10, 9), (15, 7), (8, 10), (12, 4), (5, 8), (20, 6), (7, 9)]
truck_max_capacity = 35

selected_packages_weight = optimize_truck_loading(packages, truck_max_capacity)
print(f"Result: {selected_packages_weight}")