from collections import defaultdict

def calculate_min_containers(package_weights, container_capacities):
    # Sort packages in descending order for greedy selection
    package_weights.sort(reverse=True)
    container_capacities.sort(reverse=True)
    
    min_containers = float('inf')
    current_allocation = []
    
    def backtrack(package_idx):
        nonlocal min_containers
        
        # Early termination if current allocation exceeds known minimum
        if len(current_allocation) >= min_containers:
            return
        
        # Base case: all packages allocated
        if package_idx == len(package_weights):
            min_containers = min(min_containers, len(current_allocation))
            return
        
        package_weight = package_weights[package_idx]
        
        # Try placing package in existing containers
        for i, capacity in enumerate(current_allocation):
            if capacity >= package_weight:
                current_allocation[i] -= package_weight
                backtrack(package_idx + 1)
                current_allocation[i] += package_weight
        
        # Try placing package in a new container
        for container_capacity in container_capacities:
            if container_capacity >= package_weight:
                current_allocation.append(container_capacity - package_weight)
                backtrack(package_idx + 1)
                current_allocation.pop()
                break  # Greedy: use first suitable container size
        
        return
    
    # Start backtracking from first package
    backtrack(0)
    return min_containers

# Problem setup
packages = [7, 5, 3, 2, 2]
containers = [10, 5, 3]

# Calculate result
min_containers = calculate_min_containers(packages, containers)
print(f"Result: {min_containers}")