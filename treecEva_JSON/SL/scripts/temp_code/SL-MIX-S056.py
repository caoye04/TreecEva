import itertools

def load_trucks_greedy(package_weights, truck_capacity=1000):
    # Sort packages in descending order for greedy selection
    sorted_weights = sorted(package_weights, reverse=True)
    trucks = []
    
    for weight in sorted_weights:
        # Try to fit package in existing truck
        placed = False
        for truck in trucks:
            if truck['remaining'] >= weight:
                truck['remaining'] -= weight
                truck['packages'].append(weight)
                placed = True
                break
        
        # If package doesn't fit in any existing truck, create new truck
        if not placed:
            new_truck = {'remaining': truck_capacity - weight, 'packages': [weight]}
            trucks.append(new_truck)
    
    return trucks

# Package weights in kg
packages = [350, 200, 150, 400, 300, 250, 100, 500, 175, 225, 325, 275]
loaded_trucks = load_trucks_greedy(packages)

# Calculate total unused capacity
unused_capacity = sum(truck['remaining'] for truck in loaded_trucks)

print(f"Result: {unused_capacity}")