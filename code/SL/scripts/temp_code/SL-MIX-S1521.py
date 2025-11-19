from collections import defaultdict

def calculate_priority_ratio(pkg):
    return pkg['priority'] / pkg['weight']

def load_truck_greedy(available_packages, truck_capacity):
    # Sort packages by priority-to-weight ratio (descending)
    sorted_packages = sorted(available_packages, key=calculate_priority_ratio, reverse=True)
    
    loaded_packages = []
    current_load = 0
    
    for pkg in sorted_packages:
        if current_load + pkg['weight'] <= truck_capacity:
            loaded_packages.append(pkg)
            current_load += pkg['weight']
    
    return loaded_packages

# Package data: id, weight, priority
packages = [
    {'id': 101, 'weight': 15, 'priority': 8},
    {'id': 102, 'weight': 25, 'priority': 12},
    {'id': 103, 'weight': 10, 'priority': 7},
    {'id': 104, 'weight': 30, 'priority': 9},
    {'id': 105, 'weight': 20, 'priority': 15},
    {'id': 106, 'weight': 5, 'priority': 3}
]

truck_max_capacity = 50
loaded = load_truck_greedy(packages, truck_max_capacity)

# Calculate checksum using modular arithmetic
final_checksum = 0
modulus_base = 17

for pkg in loaded:
    final_checksum = (final_checksum * 3 + pkg['id']) % modulus_base

print(f"Result: {final_checksum}")