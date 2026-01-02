from collections import defaultdict

def calculate_subnet_load(subnet):
    base = sum([x ** 2 for x in subnet if x > 0])
    offset = len(subnet) // 2
    return base - offset

def calculate_network_capacity(groups):
    capacity = 0
    for group in groups:
        load = calculate_subnet_load(group)
        capacity += max(load, 0)
    return capacity

# Irrelevant utility function (minimal interference)
def unused_helper(data):
    return [x for x in data if x % 2 == 0]

# Simulate network subnet traffic groups
subnet_groups = [
    [3, -1, 4, 1],
    [2, 0, -3],
    [5, 2, -2, 1, 1]
]

initial_flag = True
buffer_size = len(subnet_groups) * 2  # Distractor variable

# Core computation
total_capacity = calculate_network_capacity(subnet_groups)

Result: {total_capacity}