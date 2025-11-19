import math
from collections import deque

class SensorNode:
    def __init__(self, signal_strength, left=None, right=None):
        self.signal_strength = signal_strength
        self.left = left
        self.right = right

def calculate_path_score(node, current_path=[]):
    if not node:
        return 0
    
    # Add current node to path
    current_path = current_path + [node.signal_strength]
    
    # Base case: leaf node
    if not node.left and not node.right:
        # Calculate logarithmic aggregate of path
        log_sum = sum(math.log2(strength) for strength in current_path if strength > 0)
        return log_sum * len(current_path)
    
    # Recursive case with backtracking
    left_score = calculate_path_score(node.left, current_path) if node.left else 0
    right_score = calculate_path_score(node.right, current_path) if node.right else 0
    
    # Apply exponential weighting to stronger path
    max_score = max(left_score, right_score)
    weighted_score = max_score * math.exp(-0.1 * abs(left_score - right_score))
    
    return weighted_score

def find_optimal_search_path(root):
    if not root:
        return 0
    
    # Initialize stack for iterative DFS
    stack = [(root, [root.signal_strength])]
    max_aggregate = float('-inf')
    
    while stack:
        node, path = stack.pop()
        
        # If leaf node, calculate path metrics
        if not node.left and not node.right:
            # Apply complex signal processing
            processed_values = [math.log2(val) * math.sin(val) for val in path if val > 0]
            aggregate = sum(processed_values) * math.sqrt(len(path))
            max_aggregate = max(max_aggregate, aggregate)
        
        # Add children to stack
        if node.right:
            stack.append((node.right, path + [node.right.signal_strength]))
        if node.left:
            stack.append((node.left, path + [node.left.signal_strength]))
    
    return max_aggregate

# Create sensor tree
#                       8
#                     /   \
#                    4     12
#                   / \   /  \
#                  2   6 10  16
#                     / \
#                    5   7

root = SensorNode(8)
root.left = SensorNode(4)
root.right = SensorNode(12)
root.left.left = SensorNode(2)
root.left.right = SensorNode(6)
root.left.right.left = SensorNode(5)
root.left.right.right = SensorNode(7)
root.right.left = SensorNode(10)
root.right.right = SensorNode(16)

# Process sensor data using recursive algorithm
recursive_score = calculate_path_score(root)

# Process using iterative backtracking
backtracking_score = find_optimal_search_path(root)

# Combine results with bitwise operation
combined_result = int(recursive_score) ^ int(backtracking_score)

# Apply final transformation
optimal_path_score = combined_result * math.log10(recursive_score + backtracking_score + 1)

print(f"Result: {round(optimal_path_score, 2)}")