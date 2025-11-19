from functools import reduce

def optimize_truck_loading(capacity, packages):
    # State machine states: 'INIT', 'LOADING', 'FULL', 'DONE'
    state = 'INIT'
    loaded_weight = 0
    loaded_value = 0
    
    # Sort packages by value-to-weight ratio in descending order (greedy approach)
    sorted_packages = sorted(packages, key=lambda x: x[1]/x[0] if x[0] != 0 else float('inf'), reverse=True)
    
    for weight, value in sorted_packages:
        if state == 'INIT':
            state = 'LOADING'
        
        if state == 'LOADING':
            if loaded_weight + weight <= capacity:
                loaded_weight += weight
                loaded_value += value
            else:
                # Check if we can fit a fraction of the package (simplified to skip for this problem)
                state = 'FULL' if loaded_weight >= capacity * 0.95 else state
        
        if state == 'FULL':
            break  # Early return when truck is considered full
    
    return loaded_value

# Packages represented as (weight, value) tuples
available_packages = [
    (10, 60),
    (20, 100),
    (30, 120),
    (5, 30),
    (15, 75),
    (25, 110)
]

truck_capacity = 50
loaded_value = optimize_truck_loading(truck_capacity, available_packages)
print(f"Result: {loaded_value}")