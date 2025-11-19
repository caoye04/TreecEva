from collections import defaultdict, deque
import itertools

class SensorNode:
    def __init__(self, delay):
        self.delay = delay
        self.left = None
        self.right = None

def generate_delay_permutations(base_pattern):
    return list(itertools.permutations(base_pattern))

def build_sensor_tree():
    # Binary tree with specific delay values
    root = SensorNode(3)
    root.left = SensorNode(1)
    root.right = SensorNode(2)
    root.left.left = SensorNode(4)
    root.left.right = SensorNode(5)
    root.right.left = SensorNode(6)
    root.right.right = SensorNode(7)
    return root

def traverse_and_count(root, target_delay_sum, valid_patterns):
    if not root:
        return 0
    
    path_counter = 0
    queue = deque([(root, [root.delay])])
    
    while queue:
        current_node, current_path = queue.popleft()
        
        # Check if we're at a leaf node
        if not current_node.left and not current_node.right:
            # Verify sum matches target
            if sum(current_path) == target_delay_sum:
                # Check if path is a permutation of valid pattern
                path_tuple = tuple(current_path)
                if path_tuple in valid_patterns:
                    path_counter += 1
        else:
            # Continue traversal
            if current_node.left:
                queue.append((current_node.left, current_path + [current_node.left.delay]))
            if current_node.right:
                queue.append((current_node.right, current_path + [current_node.right.delay]))
    
    return path_counter

tree_root = build_sensor_tree()
pattern_base = [3, 1, 4]  # Root to one specific leaf
valid_sequence_perms = set(generate_delay_permutations(pattern_base))
target_sum_threshold = 8

matching_paths_count = traverse_and_count(tree_root, target_sum_threshold, valid_sequence_perms)
print(f"Result: {matching_paths_count}")