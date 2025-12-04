import itertools

def is_valid_config(config):
    # Check if configuration meets power requirements
    total_power = sum(component_power.get(c, 0) for c in config)
    return total_power <= max_power_limit and len(config) >= min_components

def calculate_efficiency(config):
    # Calculate theoretical efficiency score
    if not config:
        return 0
    power_used = sum(component_power.get(c, 0) for c in config)
    performance = sum(component_performance.get(c, 0) for c in config)
    return performance / power_used if power_used > 0 else 0

def optimize_network(components, target_throughput):
    # Attempt to optimize network configuration (distractor function)
    best_config = []
    max_throughput = 0
    for i in range(1, len(components) + 1):
        for subset in itertools.combinations(components, i):
            throughput = sum(component_throughput.get(c, 0) for c in subset)
            if throughput > max_throughput and throughput <= target_throughput * 1.2:
                max_throughput = throughput
                best_config = subset
    return best_config, max_throughput

# Component specifications
component_power = {
    'A1': 5, 'A2': 8, 'A3': 12,
    'B1': 10, 'B2': 15, 'B3': 7,
    'C1': 3, 'C2': 9, 'C3': 14
}

component_performance = {
    'A1': 10, 'A2': 16, 'A3': 22,
    'B1': 15, 'B2': 25, 'B3': 12,
    'C1': 8, 'C2': 18, 'C3': 28
}

# Distractor data
component_throughput = {
    'A1': 50, 'A2': 80, 'A3': 120,
    'B1': 70, 'B2': 110, 'B3': 60,
    'C1': 40, 'C2': 90, 'C3': 130
}

component_cost = {
    'A1': 100, 'A2': 180, 'A3': 250,
    'B1': 150, 'B2': 220, 'B3': 130,
    'C1': 90, 'C2': 170, 'C3': 280
}

# System constraints
max_power_limit = 25
min_components = 2
target_performance = 45
max_budget = 500  # Distractor variable

# Available components for this system
available_components = ['A1', 'A2', 'B1', 'B3', 'C1', 'C2']

# Generate potential configurations (combinations of 2-4 components)
potential_configs = []
for i in range(min_components, min(5, len(available_components) + 1)):
    potential_configs.extend(list(itertools.combinations(available_components, i)))

# Filter out configurations that exceed budget (distractor code)
budget_configs = [c for c in potential_configs if sum(component_cost.get(comp, 0) for comp in c) <= max_budget]

# Calculate potential throughput (distractor calculation)
potential_throughput = sum(component_throughput.get(c, 0) for c in available_components) // 2
optimal_config, max_throughput = optimize_network(available_components, potential_throughput)

# Find configurations that meet the power requirements
valid_configurations = [c for c in potential_configs if sum(component_power.get(comp, 0) for comp in c) <= max_power_limit]

# Misleading calculation - not the answer
efficient_count = len([c for c in valid_configurations if calculate_efficiency(c) > 1.5])

# This is the actual answer we're looking for
valid_combinations = len([c for c in potential_configs if is_valid_config(c)])

# More distractor calculations
max_efficiency = max([calculate_efficiency(c) for c in valid_configurations]) if valid_configurations else 0
total_power_consumption = sum(component_power.get(c, 0) for c in optimal_config)
performance_ratio = sum(component_performance.get(c, 0) for c in optimal_config) / target_performance if target_performance > 0 else 0

print(f"Result: {valid_combinations}")