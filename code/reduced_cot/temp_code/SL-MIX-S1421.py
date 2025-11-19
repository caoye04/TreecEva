import base64
from collections import deque

def build_trait_tree(traits_list):
    if not traits_list:
        return None
    root = {'value': traits_list[0], 'left': None, 'right': None}
    queue = deque([root])
    i = 1
    while queue and i < len(traits_list):
        node = queue.popleft()
        if i < len(traits_list) and traits_list[i] is not None:
            node['left'] = {'value': traits_list[i], 'left': None, 'right': None}
            queue.append(node['left'])
        i += 1
        if i < len(traits_list) and traits_list[i] is not None:
            node['right'] = {'value': traits_list[i], 'left': None, 'right': None}
            queue.append(node['right'])
        i += 1
    return root

def traverse_and_score(tree_root):
    if not tree_root:
        return 0
    stack = [tree_root]
    score = 0
    while stack:
        node = stack.pop()
        if isinstance(node['value'], int):
            score += node['value']
        if node['right']:
            stack.append(node['right'])
        if node['left']:
            stack.append(node['left'])
    return score

encoded_traits = 'WjFfVDJfVDM='  # Encoded string: Z1_T2_T3
decoded_bytes = base64.b64decode(encoded_traits)
trait_string = decoded_bytes.decode('utf-8')

primary_traits = frozenset(['Z1', 'T2', 'T3'])
secondary_traits = {'X1', 'T2', 'Y3', 'Z1'}
common_traits = primary_traits & secondary_traits

trait_values = { 'Z1': 15, 'T2': 25, 'T3': 35, 'X1': 10, 'Y3': 30 }
trait_queue = deque()

for trait in sorted(common_traits):
    if trait in trait_values and (trait_values[trait] > 20 or trait == 'Z1'):
        trait_queue.append(trait_values[trait])

trait_sequence = list(trait_queue)
tree_root = build_trait_tree(trait_sequence)
floral_score = traverse_and_score(tree_root) + (len(primary_traits) ^ len(secondary_traits))

print(f'Result: {floral_score}')