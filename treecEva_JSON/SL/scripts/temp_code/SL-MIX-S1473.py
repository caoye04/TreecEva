import statistics
from collections import defaultdict

class RoutingNode:
    def __init__(self, delay=0):
        self.delay = delay
        self.left = None
        self.right = None

def compute_subtree_delays(node):
    if not node:
        return []
    if not node.left and not node.right:
        return [node.delay]
    left_delays = compute_subtree_delays(node.left)
    right_delays = compute_subtree_delays(node.right)
    return left_delays + right_delays

def calculate_path_stability(root):
    if not root:
        return 0
    subtree_delays = compute_subtree_delays(root)
    if len(subtree_delays) < 2:
        return 0
    return statistics.variance(subtree_delays)

# Constructing path trees
path_a = RoutingNode(0)
path_a.left = RoutingNode(0)
path_a.right = RoutingNode(0)
path_a.left.left = RoutingNode(12)
path_a.left.right = RoutingNode(18)
path_a.right.left = RoutingNode(22)
path_a.right.right = RoutingNode(28)

path_b = RoutingNode(0)
path_b.left = RoutingNode(15)
path_b.right = RoutingNode(25)
path_b.right.right = RoutingNode(35)

paths = [path_a, path_b]
aggregate_stability_index = 0

for idx, path_root in enumerate(paths):
    path_stability = calculate_path_stability(path_root)
    aggregate_stability_index += path_stability * (idx + 1)

print(f"Result: {int(aggregate_stability_index)}")