from collections import deque

def route_packages(package_stack):
    if not package_stack:
        return []
    
    current_package = package_stack.pop()
    if current_package['priority'] > 5:
        # High priority packages get routed immediately
        return [current_package] + route_packages(package_stack)
    else:
        # Low priority packages may need to backtrack
        temp_storage = []
        while package_stack and package_stack[-1]['priority'] <= current_package['priority']:
            temp_storage.append(package_stack.pop())
        
        result = route_packages(package_stack)
        
        # Backtrack - restore packages in sorted order
        while temp_storage:
            package_stack.append(temp_storage.pop())
        package_stack.append(current_package)
        
        return result

# Initialize warehouse conveyor system
conveyor_belt_A = [
    {'id': 101, 'priority': 3, 'destination': 'Zone_D'},
    {'id': 102, 'priority': 7, 'destination': 'Zone_A'},
    {'id': 103, 'priority': 2, 'destination': 'Zone_B'},
    {'id': 104, 'priority': 8, 'destination': 'Zone_C'},
    {'id': 105, 'priority': 1, 'destination': 'Zone_A'}
]

conveyor_belt_B = [
    {'id': 201, 'priority': 6, 'destination': 'Zone_C'},
    {'id': 202, 'priority': 4, 'destination': 'Zone_D'},
    {'id': 203, 'priority': 9, 'destination': 'Zone_B'}
]

# Process packages through routing system
routed_batch_A = route_packages(conveyor_belt_A.copy())
routed_batch_B = route_packages(conveyor_belt_B.copy())

# Count packages that reached target destinations
final_destination_count = 0
zones = {'Zone_A': 0, 'Zone_B': 0, 'Zone_C': 0, 'Zone_D': 0}

for pkg in routed_batch_A + routed_batch_B:
    if pkg['destination'] in zones:
        zones[pkg['destination']] += 1

# Apply sorting to determine final count
sorted_zones = sorted(zones.items(), key=lambda x: x[1], reverse=True)

# Only count zones that received more than 1 package
for zone, count in sorted_zones:
    if count > 1:
        final_destination_count += count * 2
    else:
        final_destination_count -= 1

print(f"Result: {final_destination_count}")