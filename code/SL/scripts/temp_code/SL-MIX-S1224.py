from collections import defaultdict
import base64

def decode_sequence(encoded_str):
    return base64.b64decode(encoded_str).decode('utf-8')

def build_nary_tree():
    # Tree structure: root -> [child1, child2]
    # child1 -> [leaf1, leaf2], child2 -> [leaf3]
    tree = {}
    tree['root'] = ['child1', 'child2']
    tree['child1'] = ['leaf1', 'leaf2']
    tree['child2'] = ['leaf3']
    tree['leaf1'] = []
    tree['leaf2'] = []
    tree['leaf3'] = []
    return tree

def get_sequence_length(node_name):
    sequences = {
        'leaf1': 'QVRH',  # ATG
        'leaf2': 'VEFB',  # TAA
        'leaf3': 'VEFHVQ=='  # TAGT
    }
    if node_name in sequences:
        decoded = decode_sequence(sequences[node_name])
        return len(decoded)
    return 0

tree_structure = build_nary_tree()
node_lengths = defaultdict(int)

# Process each node to calculate sequence lengths
for node in tree_structure:
    if not tree_structure[node]:  # Leaf node
        node_lengths[node] = get_sequence_length(node)

# Calculate phylo_sum using functional programming
leaf_nodes = [node for node in node_lengths if node.startswith('leaf')]
phylo_values = list(map(lambda x: node_lengths[x] * (2 if x.endswith('1') else 3), leaf_nodes))
phylo_sum = sum(filter(lambda x: x > 3, phylo_values))

print(f"Result: {phylo_sum}")