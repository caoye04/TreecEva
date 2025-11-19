import heapq
from bisect import bisect_left

class Package:
    def __init__(self, weight, priority):
        self.weight = weight
        self.priority = priority
    
    def __lt__(self, other):
        return self.priority > other.priority  # Max heap based on priority

def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

def load_truck_greedy(packages, capacity):
    # Create max heap of packages
    heap = []
    for p in packages:
        heapq.heappush(heap, p)
    
    loaded_packages = []
    total_weight = 0
    total_priority = 0
    
    # Greedily load packages
    while heap:
        pkg = heapq.heappop(heap)
        if total_weight + pkg.weight <= capacity:
            loaded_packages.append(pkg)
            total_weight += pkg.weight
            # Apply Fibonacci surcharge for high priority (>50)
            if pkg.priority > 50:
                surcharge = fibonacci(pkg.priority % 10)
                total_priority += pkg.priority * surcharge
            else:
                total_priority += pkg.priority
    
    return total_priority, loaded_packages

def count_arrangements(loaded_packages):
    # Count possible arrangements using combinatorics
    n = len(loaded_packages)
    if n <= 1:
        return 1
    # For simplicity, return n! arrangements
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Package data: (weight, priority)
package_data = [
    (10, 65), (15, 45), (8, 75), (12, 55), (20, 35),
    (5, 85), (18, 40), (7, 90), (25, 30), (9, 70),
    (14, 50), (6, 80), (16, 42), (11, 60), (22, 38),
    (13, 58), (19, 44), (4, 95), (17, 46), (21, 36)
]

packages = [Package(w, p) for w, p in package_data]

# Truck capacities
truck_capacities = [50, 60, 70, 55, 65]

# Process each truck
results = []
for i, capacity in enumerate(truck_capacities):
    priority_score, loaded = load_truck_greedy(packages, capacity)
    arrangements = count_arrangements(loaded)
    results.append((priority_score, len(loaded), arrangements))

# Get result for third truck (index 2)
third_truck_priority = results[2][0]
print(f"Result: {third_truck_priority}")