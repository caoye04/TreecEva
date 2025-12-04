# Calculate the optimal delivery path cost in a warehouse

def calculate_distance(point1, point2):
    # Manhattan distance between two points
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

# Warehouse sections with (x, y) coordinates
sections = {
    'A': (1, 2),
    'B': (3, 5),
    'C': (6, 3),
    'D': (2, 8),
    'E': (4, 1)
}

# Items to collect and their weights (kg)
items = {
    'A': 5,
    'B': 2,
    'C': 8,
    'D': 3,
    'E': 4
}

# Starting point (warehouse entrance)
start_point = (0, 0)

# Calculate potential paths
potential_paths = ['ABCDE', 'ACDEB', 'BEDCA', 'EDCBA', 'CAEDB']
path_costs = {}

# Energy consumption factors
base_energy_per_step = 1.5
weight_penalty = 0.2
temperature_factor = 0.9  # Warehouse temperature adjustment

# Total weight carried starts at 0
total_weight = 0

# Calculate cost for each path
for path in potential_paths:
    current_point = start_point
    path_distance = 0
    energy_used = 0
    cumulative_weight = 0
    
    # Calculate path metrics
    for section in path:
        next_point = sections[section]
        section_distance = calculate_distance(current_point, next_point)
        path_distance += section_distance
        
        # Energy calculation with weight penalty
        section_energy = section_distance * (base_energy_per_step + cumulative_weight * weight_penalty)
        energy_used += section_energy
        
        # Add item weight after picking it up
        cumulative_weight += items[section]
        current_point = next_point
    
    # Return to start point
    final_distance = calculate_distance(current_point, start_point)
    path_distance += final_distance
    path_energy = final_distance * (base_energy_per_step + cumulative_weight * weight_penalty)
    energy_used += path_energy
    
    # Store path cost (energy used)
    path_costs[path] = round(energy_used * temperature_factor, 2)

# Find the path with minimum energy consumption
efficiency_metric = sum(path_costs.values()) / len(path_costs)
optimal_path = min(path_costs, key=path_costs.get)
optimal_path_cost = min(path_costs.values())

# Calculate unused metrics for reporting
average_item_weight = sum(items.values()) / len(items)
total_warehouse_area = max(p[0] for p in sections.values()) * max(p[1] for p in sections.values())

print(f"Result: {optimal_path_cost}")