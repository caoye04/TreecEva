def load_trucks():
    # Available packages: (weight, priority)
    all_packages = [(12, 24), (7, 14), (5, 15), (9, 18), (11, 22), (8, 16), (6, 12), (10, 20)]
    
    # Required packages (using set operations)
    required_weights = {5, 7, 9, 11}
    available_weights = {pkg[0] for pkg in all_packages}
    eligible_weights = available_weights & required_weights
    
    # Filter packages using set and create list
    eligible_packages = [pkg for pkg in all_packages if pkg[0] in eligible_weights]
    
    # Sort by priority-to-weight ratio using lambda
    eligible_packages.sort(key=lambda pkg: pkg[1]/pkg[0], reverse=True)
    
    # Truck capacity
    truck_capacity = 20
    
    # Greedy loading with nested loops
    loaded_packages = []
    remaining_capacity = truck_capacity
    
    for i in range(len(eligible_packages)):
        pkg_weight, pkg_priority = eligible_packages[i]
        if pkg_weight <= remaining_capacity:
            # Check if adding this package improves total priority
            include_package = True
            
            # Nested loop to check interactions with already loaded packages
            for j in range(len(loaded_packages)):
                loaded_weight, loaded_priority = loaded_packages[j]
                # Ternary operator to decide whether to keep both packages
                capacity_check = (pkg_weight + loaded_weight) <= truck_capacity
                priority_improvement = (pkg_priority + loaded_priority) > sum(p[1] for p in loaded_packages)
                include_package = include_package and (capacity_check or priority_improvement)
            
            # Conditional branch with ternary operator
            action = 'load' if include_package else 'skip'
            if action == 'load':
                loaded_packages.append(eligible_packages[i])
                remaining_capacity -= pkg_weight
    
    # Calculate total priority
    total_priority = sum(pkg[1] for pkg in loaded_packages)
    return total_priority

# Execute and print result
result = load_trucks()
print(f"Result: {result}")