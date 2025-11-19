import math

class TernaryCallNode:
    def __init__(self, name, depth):
        self.name = name
        self.depth = depth
        self.children = []

def build_full_ternary_tree(depth, current_depth=0, prefix="root"):
    node = TernaryCallNode(prefix, current_depth)
    if current_depth < depth:
        for i, child_name in enumerate(['child_a', 'child_b', 'child_c']):
            child = build_full_ternary_tree(depth, current_depth + 1, f"{prefix}_{child_name}")
            node.children.append(child)
    return node

def compute_leaf_scores(node):
    if not node.children:  # Leaf node
        name_hash = hash(node.name)
        exp_depth = math.exp(node.depth)
        return name_hash * exp_depth
    else:
        total = 0
        for child in node.children:
            total += compute_leaf_scores(child)
        return total

tree_root = build_full_ternary_tree(3)
final_complexity_score = compute_leaf_scores(tree_root)
print(f"Result: {int(final_complexity_score)}")