from collections import defaultdict

class SignalNode:
    def __init__(self, value=None, left=None, right=None, operation=None):
        self.value = value
        self.left = left
        self.right = right
        self.operation = operation  # 'XOR' for internal nodes

# Build a binary tree representing signal propagation
#       root
#      /    \
#    xor1   leaf4(7)
#   /   \
# leaf1 leaf2
# (3)   (5)

leaf1 = SignalNode(value=3)
leaf2 = SignalNode(value=5)
xor1 = SignalNode(left=leaf1, right=leaf2, operation='XOR')
leaf4 = SignalNode(value=7)
root = SignalNode(left=xor1, right=leaf4, operation='XOR')

def propagate_signal(node):
    if node.value is not None:  # Leaf node
        return node.value
    else:  # Internal node
        left_val = propagate_signal(node.left)
        right_val = propagate_signal(node.right)
        if node.operation == 'XOR':
            node.value = left_val ^ right_val
            return node.value
        # For this problem, we only have XOR operations

# Propagate signals through the tree
final_output = propagate_signal(root)
print(f"Result: {final_output}")