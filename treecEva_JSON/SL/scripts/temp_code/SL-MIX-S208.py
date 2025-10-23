import math

# Package data: (weight, priority)
packages = [
    (12.5, 3),
    (7.2, 5),
    (15.8, 2),
    (9.1, 4),
    (6.4, 6)
]

# Truck capacities
truck_capacities = [30.0, 25.0, 20.0]

# Greedy assignment based on priority-to-weight ratio
packages.sort(key=lambda x: x[1]/x[0], reverse=True)

# Track assignments
truck_assignments = {i: [] for i in range(len(truck_capacities))}
truck_loads = {i: 0.0 for i in range(len(truck_capacities))}

# Assign packages greedily
for weight, priority in packages:
    best_truck = -1
    best_remaining = float('inf')
    
    for i in range(len(truck_capacities)):
        remaining = truck_capacities[i] - truck_loads[i]
        if remaining >= weight and remaining < best_remaining:
            best_truck = i
            best_remaining = remaining
    
    if best_truck != -1:
        truck_assignments[best_truck].append((weight, priority))
        truck_loads[best_truck] += weight

# Calculate optimal load using load balancing formula
load_factors = [truck_loads[i]/truck_capacities[i] for i in range(len(truck_capacities))]
optimal_load = sum(load_factors) / len(load_factors) * 100

# Adjust for precision
optimal_load = round(optimal_load, 2)

print(f"Result: {optimal_load}")