import functools

def priority_calculator(weight, distance):
    return (distance // 10) * (100 - weight)

@functools.lru_cache(maxsize=None)
def recursive_optimizer(remaining_capacity, idx, packages):
    if idx >= len(packages) or remaining_capacity <= 0:
        return 0
    
    # Unpack current package
    weight, distance, priority_flag = packages[idx]
    current_priority = priority_calculator(weight, distance) if priority_flag else 0
    
    # Greedy choice: take package if it fits
    if weight <= remaining_capacity:
        take_package = current_priority + recursive_optimizer(remaining_capacity - weight, idx + 1, packages)
        skip_package = recursive_optimizer(remaining_capacity, idx + 1, packages)
        return max(take_package, skip_package)
    else:
        return recursive_optimizer(remaining_capacity, idx + 1, packages)

# Package data: (weight, distance, priority_flag)
shipment_manifest = [
    (15, 250, True),
    (30, 120, False),
    (10, 300, True),
    (22, 180, True),
    (18, 90, False),
    (25, 220, True),
    (12, 160, True)
]

truck_capacity = 60
loaded_packages_map = {}

total_priority_score = 0
for i in range(len(shipment_manifest)):
    package_weight, _, _ = shipment_manifest[i]
    # Ternary operator to decide if we attempt optimization
    attempt_optimization = True if package_weight <= truck_capacity else False
    
    if attempt_optimization:
        # Logical operations to determine if package set should be processed
        not_overweight = package_weight <= truck_capacity
        has_priority = shipment_manifest[i][2]
        
        if not_overweight and (has_priority or i % 2 == 0):  # Even index fallback
            optimized_score = recursive_optimizer(truck_capacity, i, tuple(shipment_manifest))
            total_priority_score += optimized_score if optimized_score > 0 else 0
            break  # Only process first valid optimization

print(f"Result: {total_priority_score}")