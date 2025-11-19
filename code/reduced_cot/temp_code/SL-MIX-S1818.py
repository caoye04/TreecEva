from functools import reduce
from collections import deque

def log_loading(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

class PackageStack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def is_empty(self):
        return len(self.items) == 0

@log_loading
def load_trucks(packages, truck_capacity):
    # Sort packages by priority/weight ratio (greedy approach)
    packages.sort(key=lambda x: x[1]/x[0], reverse=True)
    
    # Initialize trucks
    trucks = [[] for _ in range(3)]
    truck_weights = [0, 0, 0]
    
    # Process packages
    for weight, priority in packages:
        # Find first truck that can fit the package
        for i in range(3):
            if truck_weights[i] + weight <= truck_capacity:
                trucks[i].append((weight, priority))
                truck_weights[i] += weight
                break
    
    return truck_weights

# Package data: (weight, priority)
inventory = [
    (15, 8), (22, 15), (10, 7), (25, 18), (12, 9),
    (18, 12), (30, 20), (8, 5), (20, 14), (16, 11)
]

# Truck capacity
max_load = 50

# Load trucks using greedy algorithm
loaded_weights = load_trucks(inventory.copy(), max_load)

# Calculate using stack operations
package_stack = PackageStack()
for w in loaded_weights:
    package_stack.push(w)

# Pop first two values (first and second truck)
package_stack.pop()
package_stack.pop()

# Third truck weight is our target
third_truck_weight = package_stack.pop()

print(f'Result: {third_truck_weight}')