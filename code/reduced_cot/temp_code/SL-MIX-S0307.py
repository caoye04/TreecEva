def calculate_optimal_priority():
    # Package data: (weight, priority)
    shipment_manifest = [
        (2, 3), (3, 4), (4, 5), (5, 6),
        (1, 2), (6, 8), (2, 3), (3, 4),
        (7, 9), (1, 1), (4, 4), (2, 2)
    ]
    
    # Remove duplicate packages using set operations
    unique_packages = list(set(shipment_manifest))
    
    # Sort packages by priority-to-weight ratio (greedy approach)
    unique_packages.sort(key=lambda x: x[1]/x[0], reverse=True)
    
    # Initialize truck parameters
    truck_capacity = 15
    loaded_weight = 0
    total_priority = 0
    
    # Greedily load packages
    for weight, priority in unique_packages:
        if loaded_weight + weight <= truck_capacity:
            loaded_weight += weight
            total_priority += priority
    
    # Apply functional transformation to verify constraints
    weight_check = list(map(lambda x: x[0], filter(lambda p: p[0] <= 5, unique_packages)))
    
    # Conditional adjustment based on special cargo rules
    if len(weight_check) > 3:
        total_priority += sum(weight_check[:3])
    
    return total_priority

final_score = calculate_optimal_priority()
print(f"Result: {final_score}")