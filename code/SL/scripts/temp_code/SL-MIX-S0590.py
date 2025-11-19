import itertools

def load_trucks(package_batches):
    truck_capacity = 1000
    total_unused_capacity = 0
    
    for batch in package_batches:
        # Sort packages in descending order for greedy selection
        sorted_packages = sorted(batch, reverse=True)
        remaining_capacity = truck_capacity
        loaded_weight = 0
        
        # Greedily load packages
        for pkg in sorted_packages:
            if pkg <= remaining_capacity:
                remaining_capacity -= pkg
                loaded_weight += pkg
        
        total_unused_capacity += remaining_capacity
    
    return total_unused_capacity

# Package batches (weights in kg)
shipment_manifest = [
    [150, 200, 100, 300, 250],
    [400, 100, 150, 200],
    [500, 300, 100, 100],
    [200, 200, 200, 200, 200]
]

# Calculate using list comprehension for efficiency
fleet_metrics = [load_trucks([batch]) for batch in shipment_manifest]
total_unused_capacity = sum(fleet_metrics)

print(f"Result: {total_unused_capacity}")