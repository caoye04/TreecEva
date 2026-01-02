def calculate_node_score(node):
    base = node['load'] + node['redundancy']
    if node['active']:
        base *= node['efficiency']
    return int(base)

hosting_nodes = [
    {'load': 12, 'redundancy': 3, 'active': True, 'efficiency': 1.5},
    {'load': 8, 'redundancy': 5, 'active': False, 'efficiency': 1.2},
    {'load': 10, 'redundancy': 4, 'active': True, 'efficiency': 1.8}
]

node_scores = []
for node in hosting_nodes:
    score = calculate_node_score(node)
    node_scores.append(score)

aggregated_load = sum(n['load'] for n in hosting_nodes)
dummy_counter = 0
while dummy_counter < len(node_scores):
    if node_scores[dummy_counter] > 20:
        aggregated_load += 5
    dummy_counter += 1

scaling_factor = 1.2
total_score = sum(node_scores) * scaling_factor
final_capacity = int(total_score / len(hosting_nodes))
print(f"Target result: {final_capacity}")