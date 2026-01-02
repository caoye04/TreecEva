from collections import defaultdict

def calculate_subnet_load(size):
    return size * 0.85 if size > 20 else size * 0.65

def calculate_network_capacity(subnets):
    base_map = defaultdict(float)
    for region, size in subnets.items():
        base_map[region] = calculate_subnet_load(size)
    
    adjustment_factor = 1.1
    total = sum(base_map.values())
    total *= adjustment_factor
    return int(total)

# Irrelevant auxiliary variable (minimal distraction)
unused_buffer = [0] * 10

subnets = {
    'east': 30,
    'west': 25,
    'north': 15,
    'south': 40
}

initial_estimate = sum(subnets.values())
total_capacity = calculate_network_capacity(subnets)

print(f"Result: {total_capacity}")