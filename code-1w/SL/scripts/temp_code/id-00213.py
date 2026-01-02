import re
from collections import deque
from dataclasses import dataclass
from typing import List, Optional

def tokenize_config(config_str: str) -> List[str]:
    return re.findall(r'\b\w+|[/.=]', config_str)

@dataclass
class TreeNode:
    value: str
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None

def build_decision_tree(tokens: List[str]) -> TreeNode:
    stack = []
    for token in tokens:
        if token in ('AND', 'OR'):
            node = TreeNode(token)
            if stack:
                node.left = stack.pop()
            stack.append(node)
        elif token not in ('ALLOW', 'TCP', 'FROM', 'TO', 'IF'):
            if stack and stack[-1].right is None:
                stack[-1].right = TreeNode(token)
            else:
                stack.append(TreeNode(token))
    return stack[0] if stack else None

def evaluate_tree(node: TreeNode) -> bool:
    if not node:
        return False
    if node.value in ('80', '443'):
        return True
    if node.value == 'OR':
        return evaluate_tree(node.left) or evaluate_tree(node.right)
    if node.value == 'AND':
        return evaluate_tree(node.left) and evaluate_tree(node.right)
    return False

def process_network_config(config: str) -> int:
    tokens = tokenize_config(config)
    decision_tree = build_decision_tree(tokens)
    route_queue = deque(["192.168.1.1:80", "192.168.1.2:22", "10.0.0.5:443", "172.16.0.1:8080"])
    matched_routes = 0
    
    while route_queue:
        route = route_queue.popleft()
        port = route.split(':')[1]
        temp_tree = TreeNode(port)
        if decision_tree:
            # Create a new tree with the port condition
            condition_tree = TreeNode('OR')
            condition_tree.left = decision_tree
            condition_tree.right = temp_tree
            if evaluate_tree(condition_tree):
                matched_routes += 1
        elif evaluate_tree(temp_tree):
            matched_routes += 1
            
    return matched_routes

config_string = 'ALLOW TCP FROM 192.168.1.0/24 TO 10.0.0.0/8 IF PORT == 80 OR PORT == 443'
matched_routes = process_network_config(config_string)
print(f"Result: {matched_routes}")