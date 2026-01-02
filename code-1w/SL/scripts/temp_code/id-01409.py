from collections import defaultdict

# Simulate a network node load distribution with decay factors
def calculate_distribution(load_map, factor):
    temp = defaultdict(float)
    for node, load in load_map.items():
        temp[node] = load * (factor ** 2) if load > 10 else load * factor
    return sum(temp.values())

# System parameters
network_load = {'router_a': 15, 'router_b': 8, 'switch_1': 12, 'switch_2': 5}
efficiency_factor = 0.8
auxiliary_threshold = 7.5  # Irrelevant parameter for minor distraction

# Core computation
processed = list(map(lambda x: x * 1.1, network_load.values()))  # Slight transformation, not used further
def update_load(x): return x  # Dummy function, minimal interference

final_load = calculate_distribution(network_load, efficiency_factor)
print(f"Result: {final_load}")