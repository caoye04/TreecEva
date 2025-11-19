import heapq
from collections import defaultdict

def load_packages_greedy(truck_capacity, packages):
    # Sort packages by priority density (priority/weight) in descending order
    packages.sort(key=lambda pkg: pkg[1]/pkg[0], reverse=True)
    
    total_weight = 0
    total_priority = 0
    loaded_packages = []
    
    for weight, priority, pkg_id in packages:
        if total_weight + weight <= truck_capacity:
            total_weight += weight
            total_priority += priority
            loaded_packages.append(pkg_id)
    
    return total_priority, loaded_packages

def optimize_with_backtracking(truck_capacity, packages, index=0, current_weight=0, current_priority=0, selected=[]):
    # Base case: if we've considered all packages
    if index == len(packages):
        return current_priority, selected[:]
    
    # Option 1: Skip current package
    max_priority_skip, selected_skip = optimize_with_backtracking(truck_capacity, packages, index+1, current_weight, current_priority, selected)
    
    # Option 2: Take current package (if it fits)
    max_priority_take, selected_take = 0, []
    weight, priority, pkg_id = packages[index]
    if current_weight + weight <= truck_capacity:
        selected.append(pkg_id)
        max_priority_take, selected_take = optimize_with_backtracking(truck_capacity, packages, index+1, current_weight + weight, current_priority + priority, selected)
        selected.pop()  # backtrack
    
    # Return the better of the two options
    if max_priority_take > max_priority_skip:
        return max_priority_take, selected_take
    else:
        return max_priority_skip, selected_skip

# Package data: (weight, priority, package_id)
packages_data = [
    (10, 60, 'PKG001'),
    (20, 100, 'PKG002'),
    (30, 120, 'PKG003'),
    (40, 140, 'PKG004'),
    (50, 150, 'PKG005'),
    (60, 160, 'PKG006')
]

# Metadata storage using hash table
package_metadata = defaultdict(dict)
package_metadata['PKG001'] = {'fragile': True, 'destination': 'ZoneA'}
package_metadata['PKG002'] = {'fragile': False, 'destination': 'ZoneB'}
package_metadata['PKG003'] = {'fragile': True, 'destination': 'ZoneC'}
package_metadata['PKG004'] = {'fragile': False, 'destination': 'ZoneA'}
package_metadata['PKG005'] = {'fragile': True, 'destination': 'ZoneB'}
package_metadata['PKG006'] = {'fragile': False, 'destination': 'ZoneC'}

# Weight management using min-heap
package_weights = [pkg[0] for pkg in packages_data]
heapq.heapify(package_weights)

# Truck capacity
truck_capacity = 100

# Greedy loading
_, greedy_selection = load_packages_greedy(truck_capacity, packages_data)

# Backtracking optimization
max_priority, optimal_selection = optimize_with_backtracking(truck_capacity, packages_data)

# Count fragile packages in optimal selection
fragile_count = sum(1 for pkg_id in optimal_selection if package_metadata[pkg_id]['fragile'])

# Adjust priority based on fragile package count
max_priority -= fragile_count * 5

print(f'Result: {max_priority}')