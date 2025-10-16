from functools import reduce

class FuelTracker:
    def __init__(self):
        self.consumption = 0
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def add_fuel(self, amount):
        self.consumption += amount

def calculate_route_fuel(weights, depth=0):
    if not weights:
        return 0
    
    current_weight = weights[0]
    remaining_weights = weights[1:]
    
    # Calculate base fuel for current package
    base_fuel = (current_weight * 2) + 1
    
    # Recursive calculation for remaining packages
    remaining_fuel = calculate_route_fuel(remaining_weights, depth+1)
    
    # Apply depth-based optimization (lighter packages get priority)
    if depth > 0 and current_weight < 5:
        base_fuel = base_fuel // 2
    
    return base_fuel + remaining_fuel

def process_deliveries(package_manifest):
    # Filter out packages that are too heavy (>20 units)
    valid_packages = list(filter(lambda pkg: pkg[1] <= 20, package_manifest))
    
    # Extract weights
    weights = list(map(lambda pkg: pkg[1], valid_packages))
    
    # Calculate fuel using recursive function
    initial_fuel = calculate_route_fuel(weights)
    
    # Apply global optimization using reduce
    optimized_fuel = reduce(lambda acc, w: acc + (w // 3) if w % 3 == 0 else acc + w, weights, 0)
    
    # Return the maximum of both calculations
    return max(initial_fuel, optimized_fuel)

# Package manifest: (destination_id, weight)
logistics_schedule = [
    ("DP001", 7),
    ("DP002", 12),
    ("DP003", 3),
    ("DP004", 15),
    ("DP005", 8),
    ("DP006", 22),  # This package will be filtered out
    ("DP007", 4)
]

with FuelTracker() as tracker:
    required_fuel = process_deliveries(logistics_schedule)
    tracker.add_fuel(required_fuel)
    total_fuel_consumption = tracker.consumption

print(f"Result: {total_fuel_consumption}")