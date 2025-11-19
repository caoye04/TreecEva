from collections import deque

class EncryptionNode:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

def hybrid_traversal(root):
    if not root:
        return 0
    
    cryptographic_evidence = 0
    stack = [(root, 0)]  # (node, level)
    
    while stack:
        current_node, level = stack.pop()
        
        # Apply transformation using lambda
        transform = lambda x: x * 2 if x % 2 == 0 else x + 3
        transformed_value = transform(current_node.value)
        
        # Short-circuit evaluation to skip branches
        if not (transformed_value > 10 and len(current_node.children) < 2):
            cryptographic_evidence += transformed_value
        
        # Hybrid traversal logic
        if level % 2 == 0:  # Even level - DFS
            for child in reversed(current_node.children):
                stack.append((child, level + 1))
        else:  # Odd level - BFS
            queue = deque([(child, level + 1) for child in current_node.children])
            while queue:
                node, lvl = queue.popleft()
                stack.insert(0, (node, lvl))
    
    return cryptographic_evidence

# Build encryption tree
root = EncryptionNode(5)
root.children = [EncryptionNode(3), EncryptionNode(8)]
root.children[0].children = [EncryptionNode(1), EncryptionNode(7)]
root.children[1].children = [EncryptionNode(12)]
root.children[0].children[0].children = [EncryptionNode(4)]
root.children[1].children[0].children = [EncryptionNode(2), EncryptionNode(9)]

# Execute analysis
cryptographic_evidence = hybrid_traversal(root)
print(f"Result: {cryptographic_evidence}")