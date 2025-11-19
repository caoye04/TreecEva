from collections import namedtuple

# Define warehouse data structure
Warehouse = namedtuple('Warehouse', ['id', 'package_count', 'priority'])

# Fleet and warehouse data
vehicle_capacities = [75, 85, 95]
warehouses = [
    Warehouse(1, 30, 2),
    Warehouse(2, 25, 1),
    Warehouse(3, 40, 3),
    Warehouse(4, 20, 2),
    Warehouse(5, 35, 1)
]

# Sort warehouses by priority (ascending) then by package count (descending)
warehouses_sorted = sorted(warehouses, key=lambda w: (w.priority, -w.package_count))

# Calculate maximum packages per vehicle
max_packages_collected = 0
for capacity in vehicle_capacities:
    current_load = 0
    for warehouse in warehouses_sorted:
        if current_load + warehouse.package_count <= capacity:
            current_load += warehouse.package_count
        else:
            break
    max_packages_collected = max(max_packages_collected, current_load)

print(f"Result: {max_packages_collected}")