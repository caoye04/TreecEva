from collections import namedtuple

def assign_truck_id(weight, capacity):
    return (weight * 3 + 7) % capacity

def process_packages():
    Package = namedtuple('Package', ['weight', 'priority'])
    packages = [
        Package(12, 5),
        Package(7, 8),
        Package(15, 3),
        Package(9, 6),
        Package(4, 9)
    ]
    
    # Sort packages by priority (descending), then by weight (ascending)
    sorted_packages = sorted(packages, key=lambda p: (-p.priority, p.weight))
    
    truck_capacity = 10
    total_priority = 0
    
    for pkg in sorted_packages:
        truck_id = assign_truck_id(pkg.weight, truck_capacity)
        if truck_id % 2 == 0:  # Only load on even-numbered trucks
            total_priority += pkg.priority
    
    return total_priority

# Main execution
final_result = process_packages()
print(f"Result: {final_result}")