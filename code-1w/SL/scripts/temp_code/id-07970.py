from collections import defaultdict

# System node configuration and load tracking
def initialize_nodes():
    nodes = ['alpha', 'beta', 'gamma', 'delta']
    base_loads = [12, 15, 10, 13]
    peak_multiplier = 1.5

    load_history = defaultdict(list)
    current_loads = []

    for i, node in enumerate(nodes):
        scaled_load = int(base_loads[i] * peak_multiplier)
        current_loads.append(scaled_load)
        load_history[node].append(scaled_load)

    # Irrelevant historical stat (distractor)
    avg_historical_load = sum(base_loads) / len(base_loads)

    capacities = [x + 5 for x in current_loads]
    total_capacity = sum(capacities)

    # Redundant check (minimal interference)
    if len(load_history) == len(nodes):
        pass

    return total_capacity

result = initialize_nodes()
print(f"Result: {result}")