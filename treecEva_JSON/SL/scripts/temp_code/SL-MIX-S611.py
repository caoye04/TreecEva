from collections import namedtuple

Package = namedtuple('Package', ['weight', 'priority'])

# Available packages
packages = [
    Package(20, 60),
    Package(30, 90),
    Package(15, 45),
    Package(25, 75),
    Package(10, 30),
    Package(40, 80),
    Package(35, 105)
]

# Calculate priority-to-weight ratios and sort packages
calculate_ratio = lambda pkg: pkg.priority / pkg.weight if pkg.weight > 0 else 0
sorted_packages = sorted(packages, key=calculate_ratio, reverse=True)

# Greedy selection
truck_capacity = 150
current_load = 0
total_priority = 0
selected_count = 0

for pkg in sorted_packages:
    # Ternary operator to check if adding package exceeds capacity
    add_package = True if current_load + pkg.weight <= truck_capacity else False
    if add_package:
        current_load += pkg.weight
        total_priority += pkg.priority
        selected_count += 1
    else:
        # Once we can't add more, break (greedy approach)
        break

# Adjust total_priority if an odd number of packages were selected
adjustment_factor = 2 if selected_count % 2 != 0 else 1
total_priority = total_priority // adjustment_factor if adjustment_factor == 2 else total_priority

print(f"Result: {total_priority}")