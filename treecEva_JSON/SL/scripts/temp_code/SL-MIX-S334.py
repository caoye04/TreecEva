from collections import deque

def load_truck_packages():
    truck_capacity = 1000
    package_weights = [73, 128, 56, 201, 99, 312, 88, 155, 67, 244]
    modular_constraints = [5, 7, 3, 11, 2, 13, 4, 9, 6, 8]
    
    # Apply modular arithmetic to adjust weights
    adjusted_weights = [(w % m) if m != 0 else w for w, m in zip(package_weights, modular_constraints)]
    
    # Greedy selection: prioritize packages with higher adjusted weights
    sorted_indices = sorted(range(len(adjusted_weights)), key=lambda i: adjusted_weights[i], reverse=True)
    
    # Load packages using deque for efficient pops from both ends
    packages_queue = deque(sorted_indices)
    remaining_capacity = truck_capacity
    
    while packages_queue and remaining_capacity > 0:
        idx = packages_queue.popleft()
        weight = package_weights[idx]
        
        # Only load if it fits
        if weight <= remaining_capacity:
            remaining_capacity -= weight
    
    return remaining_capacity

remaining_capacity = load_truck_packages()
print(f"Result: {remaining_capacity}")