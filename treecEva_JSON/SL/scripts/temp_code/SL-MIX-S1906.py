class TreeNode:
    def __init__(self, rule_id, children=None):
        self.rule_id = rule_id
        self.children = children if children else []

def evaluate_compatibility(species_set):
    forbidden_pairs = [{1, 3}, {2, 5}, {4, 6}]
    for pair in forbidden_pairs:
        if pair.issubset(species_set):
            return False
    return True

def traverse_with_backtracking(node, current_path, all_paths):
    current_path.append(node.rule_id)
    
    # If it's a leaf node, check the configuration
    if not node.children:
        species_in_path = frozenset(current_path)
        if evaluate_compatibility(species_in_path):
            all_paths.append(list(current_path))
    else:
        # Explore children
        for child in node.children:
            traverse_with_backtracking(child, current_path, all_paths)
    
    # Backtrack
    current_path.pop()

# Constructing the ecosystem decision tree
root = TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

root.children = [node1, node2]
node1.children = [node3, node4]
node2.children = [node5, node6]

# Initialize tracking variables
stable_configurations = []
initial_path = []

# Begin traversal
traverse_with_backtracking(root, initial_path, stable_configurations)

# Count valid configurations
configuration_count = len(stable_configurations)
print(f"Result: {configuration_count}")