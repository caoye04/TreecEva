from collections import defaultdict

def calculate_subtree_contributions(node_id, dependencies, scores):
    if node_id not in dependencies or not dependencies[node_id]:
        return scores.get(node_id, 0)
    
    direct_sum = sum(scores.get(child, 0) for child in dependencies[node_id])
    subtree_sum = sum(calculate_subtree_contributions(child, dependencies, scores) for child in dependencies[node_id])
    
    return direct_sum + subtree_sum * 0.5

dependencies_map = {
    'root': ['modA', 'modB'],
    'modA': ['subX', 'subY'],
    'modB': ['subZ'],
    'subX': [],
    'subY': ['leaf1'],
    'subZ': ['leaf2', 'leaf3']
}

module_scores = {
    'modA': 10,
    'modB': 20,
    'subX': 5,
    'subY': 7,
    'subZ': 15,
    'leaf1': 3,
    'leaf2': 4,
    'leaf3': 2
}

total_contribution = calculate_subtree_contributions('root', dependencies_map, module_scores)
print(f"Result: {int(total_contribution)}")