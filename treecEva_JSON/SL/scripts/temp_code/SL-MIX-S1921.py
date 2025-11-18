from collections import defaultdict
import itertools

class SpeciesNode:
    def __init__(self, abundance=0):
        self.abundance = abundance
        self.left = None
        self.right = None

def count_paths_to_leaves(node, path_counts):
    if not node:
        return {}
    if not node.left and not node.right:  # leaf node
        path_counts[id(node)] = 1
        return {id(node): 1}
    
    left_paths = count_paths_to_leaves(node.left, path_counts)
    right_paths = count_paths_to_leaves(node.right, path_counts)
    
    current_paths = defaultdict(int)
    for lid, lcount in left_paths.items():
        for rid, rcount in right_paths.items():
            path_counts[(lid, rid)] += lcount * rcount
        current_paths[lid] += lcount
    for rid, rcount in right_paths.items():
        current_paths[rid] += rcount
    
    return current_paths

# Build ecosystem tree
root = SpeciesNode(0)
root.left = SpeciesNode(0)
root.right = SpeciesNode(0)
root.left.left = SpeciesNode(5)  # Oak
root.left.right = SpeciesNode(3)  # Pine
root.right.left = SpeciesNode(7)  # Maple
root.right.right = SpeciesNode(2)  # Birch

# Calculate interaction scores
path_counts = defaultdict(int)
count_paths_to_leaves(root, path_counts)

leaf_nodes = [
    root.left.left,
    root.left.right,
    root.right.left,
    root.right.right
]

# Compute pairwise interactions
interactions = []
for node1, node2 in itertools.combinations(leaf_nodes, 2):
    path_key = (id(node1), id(node2))
    if path_key in path_counts:
        interaction = node1.abundance * node2.abundance * path_counts[path_key]
        interactions.append(interaction)

# Sum all interaction scores
total_interaction_score = sum(interactions)
print(f"Result: {total_interaction_score}")