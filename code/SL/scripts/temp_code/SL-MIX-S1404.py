import re
from collections import defaultdict

class TreeNode:
    def __init__(self, name, characteristics=None):
        self.name = name
        self.characteristics = characteristics or {}
        self.left = None
        self.right = None

def build_sample_tree():
    # Creating a sample botanical classification tree
    root = TreeNode('Fabaceae')
    root.left = TreeNode('Acacia')
    root.right = TreeNode('Astragalus')
    root.left.left = TreeNode('Acacia dealbata')
    root.left.right = TreeNode('Acacia nilotica')
    root.right.left = TreeNode('Astragalus membranaceus')
    root.right.right = TreeNode('Astragalus mongholicus')
    return root

def collect_leaf_names(node, leaf_names):
    if not node:
        return
    if not node.left and not node.right:  # Leaf node
        leaf_names.append(node.name)
    collect_leaf_names(node.left, leaf_names)
    collect_leaf_names(node.right, leaf_names)

tree_root = build_sample_tree()
species_list = []
collect_leaf_names(tree_root, species_list)

# Botanical naming pattern: Genus followed by specific epithet
botanical_pattern = r'^[A-Z][a-z]+ [a-z]+$'
matching_species_count = sum(1 for species in species_list if re.match(botanical_pattern, species))

print(f"Result: {matching_species_count}")