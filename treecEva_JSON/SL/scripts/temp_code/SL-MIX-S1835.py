from math import gcd
from functools import reduce

def lcm(a, b):
    return abs(a * b) // gcd(a, b) if a and b else 0

def build_ternary_tree():
    # Node ids are primes: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37
    # Tree structure:
    #       2
    #    /  |  \
    #   3   5   7
    #  /|\   \   \
    # 11 13 17  19
    #    |        \
    #    23       29
    #              |
    #             31
    #              |
    #             37
    return {
        'id': 2,
        'children': [
            {'id': 3, 'children': [
                {'id': 11, 'children': []},
                {'id': 13, 'children': [{'id': 23, 'children': []}]},
                {'id': 17, 'children': []}
            ]},
            {'id': 5, 'children': [
                {'id': 19, 'children': [
                    {'id': 29, 'children': [
                        {'id': 31, 'children': [
                            {'id': 37, 'children': []}
                        ]}
                    ]}
                ]}
            ]},
            {'id': 7, 'children': []}
        ]
    }

def dfs(node, current_path_ids, depth):
    global security_metric
    current_path_ids.append(node['id'])
    
    if not node['children']:
        # Leaf node: calculate contribution
        path_lcm = reduce(lcm, current_path_ids)
        security_metric += path_lcm * depth
    else:
        # Internal node: recurse
        for child in node['children']:
            dfs(child, current_path_ids[:], depth + 1)

# Initialize
security_metric = 0
tree_root = build_ternary_tree()

# Compute security metric
with open('dummy.txt', 'w') as f:
    f.write('Computing...')
    dfs(tree_root, [], 1)
    f.write(f'Done: {security_metric}')

print(f'Result: {security_metric}')