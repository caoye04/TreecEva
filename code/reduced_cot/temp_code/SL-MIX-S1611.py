import itertools
from collections import defaultdict

def calculate_shipment_priority(truck_capacity, packages):
    # Sort packages by priority-to-weight ratio (greedy approach)
    packages.sort(key=lambda x: x[1]/x[0] if x[0] > 0 else 0, reverse=True)
    
    current_weight = 0
    accumulated_priority = 0
    
    for weight, priority in packages:
        if current_weight + weight <= truck_capacity:
            current_weight += weight
            accumulated_priority += priority
        else:
            # Early return if adding any more would exceed capacity
            break
    
    return accumulated_priority

def analyze_package_combinations(all_packages):
    # Count how often pairs of packages appear together
    combination_counter = defaultdict(int)
    
    for package_list in all_packages:
        # Generate all 2-package combinations
        for combo in itertools.combinations(package_list, 2):
            combination_counter[tuple(sorted(combo))] += 1
    
    return combination_counter

# Define truck capacities and package lists
truck_capacities = [100, 150, 200]
shipment_manifests = [
    [(30, 45), (40, 60), (20, 30), (35, 50)],  # (weight, priority)
    [(50, 70), (60, 80), (45, 65), (25, 35), (30, 40)],
    [(70, 90), (80, 100), (55, 75), (40, 55)]
]

# Process each shipment with greedy optimization
priority_results = []
for i in range(len(truck_capacities)):
    capacity = truck_capacities[i]
    packages = shipment_manifests[i][:]  # Create a copy
    priority_results.append(calculate_shipment_priority(capacity, packages))

# Analyze package combinations across all shipments
combination_frequencies = analyze_package_combinations(shipment_manifests)

# Find most frequent combination
most_frequent_combo = max(combination_frequencies.items(), key=lambda x: x[1]) if combination_frequencies else (None, 0)

# Calculate final optimization metric
optimal_priority_sum = sum(priority_results) + (most_frequent_combo[1] if most_frequent_combo[0] else 0)

print(f"Result: {optimal_priority_sum}")