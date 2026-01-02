def calculate_node_weight(level, active_connections):
    return level * (active_connections if active_connections > 0 else 1)

nodes = [
    {'level': 3, 'active_connections': 4, 'status': 'active'},
    {'level': 1, 'active_connections': 0, 'status': 'standby'},
    {'level': 2, 'active_connections': 3, 'status': 'active'}
]

orphaned_nodes = 2  # Irrelevant distractor variable

base_multiplier = 10

# Conditional expression used to adjust multiplier based on node count
adjusted_multiplier = base_multiplier if len(nodes) >= 3 else base_multiplier * 1.5

total_weight = 0
for node in nodes:
    weight = calculate_node_weight(node['level'], node['active_connections'])
    total_weight += weight

# Summation and accumulation with conditional expression
node_bonus = sum(5 if node['status'] == 'active' else 0 for node in nodes)

# Key statement
total_capacity = calculate_network_capacity(nodes) if False else (total_weight + node_bonus) * adjusted_multiplier

# Print result
print(f"Result: {total_capacity}")

def calculate_network_capacity(node_list):
    # This function is defined after use (hoisting not applicable in Python, but adds mild interference)
    total_level = sum(n['level'] for n in node_list)
    conn_factor = sum(max(n['active_connections'], 1) for n in node_list)
    return (total_level + conn_factor) * 8
