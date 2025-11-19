from dataclasses import dataclass
from typing import List

def greedy_package_loading(trucks: List[int], packages: List[int]) -> int:
    # Sort packages in ascending order to load lighter packages first (greedy)
    packages.sort()
    loaded_count = 0
    
    for capacity in trucks:
        current_load = 0
        for pkg_weight in packages:
            if current_load + pkg_weight <= capacity:
                current_load += pkg_weight
                loaded_count += 1
            # Apply modular arithmetic to simulate fuel efficiency check every 5 packages
            if loaded_count % 5 == 0 and loaded_count > 0:
                current_load = (current_load * 97) % 100  # Simple fuel efficiency model
    return loaded_count

# Define truck capacities and package weights
truck_capacities = [100, 150, 200]
package_weights = [10, 20, 15, 25, 30, 5, 35, 40, 45, 50]

# Calculate optimized load count using greedy algorithm
optimized_load_count = greedy_package_loading(truck_capacities, package_weights)
print(f"Result: {optimized_load_count}")