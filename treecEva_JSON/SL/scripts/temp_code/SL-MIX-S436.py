from collections import defaultdict, deque

class FunctionNode:
    def __init__(self, node_id, cost):
        self.node_id = node_id
        self.cost = cost
        self.children = []

def build_tree():
    # Create nodes
    nodes = {i: FunctionNode(i, cost) for i, cost in enumerate([12, -5, 7, 20, -3, 15, 8, -10, 9, 11])}
    # Define tree structure (parent: [children])
    edges = {
        0: [1, 2],
        1: [3, 4],
        2: [5, 6],
        3: [7, 8],
        5: [9]
    }
    for parent, children in edges.items():
        nodes[parent].children = [nodes[child] for child in children]
    return nodes[0]  # Return root

def prune_and_calculate_max_cost(root):
    # Prune nodes with cost < 0
    def prune(node):
        if not node:
            return None
        if node.cost < 0:
            return None
        node.children = [prune(child) for child in node.children]
        node.children = [child for child in node.children if child is not None]
        return node
    
    root = prune(root)
    if not root:
        return 0
    
    # Dynamic programming to find max path cost
    memo = {}
    def dp(node):
        if not node:
            return 0
        if node.node_id in memo:
            return memo[node.node_id]
        if not node.children:
            memo[node.node_id] = node.cost
            return node.cost
        
        max_child_cost = float('-inf')
        for child in node.children:
            child_cost = dp(child)
            if child_cost > max_child_cost:
                max_child_cost = child_cost
            if child_cost < 0:  # Early termination logic
                break
        
        result = node.cost + max_child_cost
        memo[node.node_id] = result
        return result
    
    return dp(root)

tree_root = build_tree()
max_path_cost = prune_and_calculate_max_cost(tree_root)
print(f"Result: {max_path_cost}")