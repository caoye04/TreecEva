def calculate_network_capacity(nodes):
    base_load = 10
    peak_multiplier = 1.5
    capacities = [int(base_load * (node[1] ** 2) * peak_multiplier) for node in nodes if node[0] != "maintenance"]
    total_capacity = sum(capacities)
    redundant_node = 50  # Irrelevant variable (minimal distraction)
    return total_capacity

nodes_list = [("active", 2), ("standby", 3), ("maintenance", 4), ("active", 1)]
total_capacity = calculate_network_capacity(nodes_list)
print(f"Result: {total_capacity}")