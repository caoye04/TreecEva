from collections import defaultdict

class Package:
    def __init__(self, id, weight, priority):
        self.id = id
        self.weight = weight
        self.priority = priority
        self.ratio = priority / weight if weight > 0 else 0

# Define packages with ID, weight, and priority
packages = [
    Package('A1', 10, 30),
    Package('B2', 20, 45),
    Package('C3', 15, 35),
    Package('D4', 25, 60),
    Package('E5', 5, 10)
]

# Truck capacity
truck_capacity = 40

# Sort packages by priority-to-weight ratio in descending order
sorted_packages = sorted(packages, key=lambda p: p.ratio, reverse=True)

# Greedy loading
loaded_priority_score = 0
remaining_capacity = truck_capacity

for pkg in sorted_packages:
    if pkg.weight <= remaining_capacity:
        loaded_priority_score += pkg.priority
        remaining_capacity -= pkg.weight
    if remaining_capacity == 0:
        break

print(f"Result: {loaded_priority_score}")