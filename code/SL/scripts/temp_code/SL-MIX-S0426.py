import re
from functools import reduce

# Delivery manifest: format is "priority:weight;priority:weight;..."
delivery_manifest = "1:150;3:200;2:100;1:300;3:75;2:120;1:180;2:90;3:250;1:160"

# Parse manifest into list of (priority, weight) tuples
token_pattern = r'(\d+):(\d+)'
parsed_packages = [(int(p), int(w)) for p, w in re.findall(token_pattern, delivery_manifest)]

# Truck capacities
truck_capacities = [500, 400, 600]

# Sort packages by priority (1 is highest) and then by weight (heaviest first for same priority)
sorted_packages = sorted(parsed_packages, key=lambda x: (x[0], -x[1]))

# Greedy loading: load packages in priority order until truck is full
remaining_packages = sorted_packages[:]
unused_capacity = 0

for capacity in truck_capacities:
    loaded_weight = 0
    i = 0
    while i < len(remaining_packages):
        priority, weight = remaining_packages[i]
        if loaded_weight + weight <= capacity:
            loaded_weight += weight
            remaining_packages.pop(i)
        else:
            i += 1
    unused_capacity += (capacity - loaded_weight)

# Calculate final result using functional programming
final_result = reduce(lambda x, y: x + y, [capacity for capacity in truck_capacities]) - (reduce(lambda x, y: x + y, [w for p, w in sorted_packages]) - reduce(lambda x, y: x + y, [w for p, w in remaining_packages]))

print(f"Result: {unused_capacity}")