class TreeNode:
    def __init__(self, threshold, left=None, right=None, classification=None):
        self.threshold = threshold
        self.left = left
        self.right = right
        self.classification = classification

def build_decision_tree():
    # Leaf nodes
    node_7 = TreeNode(threshold=0, classification=7)
    node_8 = TreeNode(threshold=0, classification=8)
    node_9 = TreeNode(threshold=0, classification=9)
    node_10 = TreeNode(threshold=0, classification=10)
    
    # Internal nodes
    node_3 = TreeNode(threshold=15.5, left=node_7, right=node_8)
    node_4 = TreeNode(threshold=22.3, left=node_9, right=node_10)
    node_1 = TreeNode(threshold=12.7, left=node_3, right=node_4)
    
    node_5 = TreeNode(threshold=0, classification=5)
    node_6 = TreeNode(threshold=0, classification=6)
    node_2 = TreeNode(threshold=8.9, left=node_5, right=node_6)
    
    root = TreeNode(threshold=10.2, left=node_1, right=node_2)
    return root

tree_root = build_decision_tree()
leaf_profile_metrics = [11.5, 18.2, 9.7]

# Lambda for ternary evaluation with comparison
traverse_step = lambda node, metric: node.left if metric <= node.threshold else node.right

current_node = tree_root
for metric in leaf_profile_metrics:
    if current_node.classification is not None:
        break
    current_node = traverse_step(current_node, metric)

final_classification_index = current_node.classification if current_node.classification is not None else -1
print(f"Result: {final_classification_index}")