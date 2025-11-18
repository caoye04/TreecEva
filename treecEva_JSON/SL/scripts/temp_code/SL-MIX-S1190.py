import itertools

def load_packages_greedy(package_list, max_weight):
    # Sort packages by value-to-weight ratio descending (greedy approach)
    package_list.sort(key=lambda p: p['value']/p['weight'], reverse=True)
    
    current_weight = 0
    total_loaded_value = 0
    loaded_packages = []
    
    for pkg in package_list:
        if current_weight + pkg['weight'] <= max_weight:
            current_weight += pkg['weight']
            total_loaded_value += pkg['value']
            loaded_packages.append(pkg)
    
    return total_loaded_value, loaded_packages

# Package data: list of dictionaries with 'id', 'weight', and 'value'
packages = [
    {'id': 'PKG001', 'weight': 10, 'value': 60},
    {'id': 'PKG002', 'weight': 20, 'value': 100},
    {'id': 'PKG003', 'weight': 30, 'value': 120},
    {'id': 'PKG004', 'weight': 15, 'value': 90},
    {'id': 'PKG005', 'weight': 25, 'value': 75}
]

truck_capacity = 50

# Simulate logging with context manager
logfile = "delivery_log.txt"
with open(logfile, 'w') as f:
    result_value, loaded = load_packages_greedy(packages, truck_capacity)
    f.write(f"Loaded packages: {[pkg['id'] for pkg in loaded]}\n")
    f.write(f"Total value: {result_value}\n")

# Post-processing step with itertools combinations
combinations_count = sum(1 for _ in itertools.combinations(range(len(packages)), 2))
adjusted_result = result_value if combinations_count > 10 else result_value * 2

# Ternary operator for final adjustment based on weight distribution
weight_sum = sum(pkg['weight'] for pkg in packages)
average_weight = weight_sum / len(packages) if len(packages) > 0 else 0
total_loaded_value = adjusted_result if average_weight > 20 else adjusted_result + 10

print(f"Result: {total_loaded_value}")