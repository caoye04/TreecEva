def calculate_node_load(node_config):
    base_load = node_config['weight'] * node_config['factor']
    overhead = node_config.get('overhead', 0.1) * base_load
    adjusted_load = base_load + overhead
    efficiency_penalty = 0.05 if adjusted_load > 100 else 0
    return adjusted_load - efficiency_penalty

network_nodes = [
    {'weight': 23, 'factor': 4, 'overhead': 0.15, 'tag': 'primary'},
    {'weight': 18, 'factor': 5, 'overhead': 0.12, 'tag': 'backup'},
    {'weight': 31, 'factor': 3, 'tag': 'primary'},
    {'weight': 14, 'factor': 6, 'overhead': 0.18, 'tag': 'secondary'}
]

node_scores = []
temp_weights = []
for node in network_nodes:
    score = calculate_node_load(node)
    node_scores.append(score)
    temp_weights.append(node['weight'])

consolidated_map = {i: score for i, score in enumerate(node_scores)}

# Irrelevant aggregation
weight_sum = sum(temp_weights)
weight_avg = weight_sum / len(temp_weights)
dummy_ratio = weight_sum / (weight_avg + 1e-5)

high_priority_count = 0
for node in network_nodes:
    if node['weight'] > 20:
        high_priority_count += 1

scaling_factor = 1.2 if high_priority_count >= 2 else 1.0

intermediate_total = 0
for idx, score in consolidated_map.items():
    if idx % 2 == 0:
        intermediate_total += score * 0.9
    else:
        intermediate_total += score * scaling_factor

buffer_contribution = 0
for char in "buffer_zone":
    buffer_contribution += ord(char) % 5

# Misleading adjustment
phantom_offset = buffer_contribution * 0.01
intermediate_total += phantom_offset

stability_check = len(network_nodes) > 3 and all(isinstance(n['factor'], int) for n in network_nodes)

def calculate_system_throughput(nodes):
    raw_total = 0
    for node in nodes:
        load = calculate_node_load(node)
        if node.get('tag') == 'primary':
            raw_total += load * 1.1
        elif node.get('tag') == 'backup':
            raw_total += load * 0.8
        else:
            raw_total += load * 0.6
    return int(raw_total // 1)

final_capacity = calculate_system_throughput(network_nodes)
print(f"Result: {final_capacity}")