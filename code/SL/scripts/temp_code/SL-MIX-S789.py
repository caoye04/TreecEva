from collections import defaultdict

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.children = []

def compute_tree_metric(node):
    if not node.children:
        return node.val
    child_sum = sum(compute_tree_metric(child) for child in node.children)
    return node.val + child_sum * len(node.children)

token_stream = ['{', '{', '{', '}', '{', '}', '}', '{', '}', '}']
block_stack = []
root_node = TreeNode(1)
active_nodes = [root_node]
structural_score = 0
state = 'IDLE'

for token in token_stream:
    if token == '{':
        if state == 'IDLE':
            state = 'BLOCK_OPEN'
        new_node = TreeNode(len(active_nodes)+1)
        if active_nodes:
            active_nodes[-1].children.append(new_node)
        active_nodes.append(new_node)
        block_stack.append('{')
    elif token == '}' and block_stack:
        block_stack.pop()
        closed_node = active_nodes.pop()
        if not block_stack:
            state = 'IDLE'
        else:
            state = 'BLOCK_CLOSE'
        # Calculate contribution only when a top-level block closes
        if not block_stack:
            structural_score += compute_tree_metric(closed_node)

print(f"Result: {structural_score}")