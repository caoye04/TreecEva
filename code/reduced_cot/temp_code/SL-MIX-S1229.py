from math import gcd
from itertools import combinations

def generate_coprime_pairs(limit):
    return [(a, b) for a in range(2, limit) for b in range(a+1, limit) if gcd(a, b) == 1]

def build_ternary_tree(nodes, depth=0):
    if depth >= 3 or not nodes:
        return None
    root_val = nodes[0]
    remaining = nodes[1:]
    left_child = build_ternary_tree(remaining[:len(remaining)//3], depth+1)
    middle_child = build_ternary_tree(remaining[len(remaining)//3:2*len(remaining)//3], depth+1)
    right_child = build_ternary_tree(remaining[2*len(remaining)//3:], depth+1)
    return {
        'value': root_val,
        'left': left_child,
        'middle': middle_child,
        'right': right_child
    }

def traverse_and_score(node):
    if not node:
        return 0
    left_score = traverse_and_score(node['left'])
    middle_score = traverse_and_score(node['middle'])
    right_score = traverse_and_score(node['right'])
    
    children_values = [child['value'] for child in [node['left'], node['middle'], node['right']] if child]
    combinatorial_factor = sum(1 for _ in combinations(children_values, 2)) if len(children_values) >= 2 else 0
    
    node_score = node['value'] + left_score + middle_score + right_score + combinatorial_factor
    return node_score

# Main execution
key_components = [x[0] * x[1] for x in generate_coprime_pairs(12) if x[0] * x[1] < 100][:10]
tree_root = build_ternary_tree(key_components)
security_index = traverse_and_score(tree_root) if tree_root else 0
print(f"Result: {security_index}")