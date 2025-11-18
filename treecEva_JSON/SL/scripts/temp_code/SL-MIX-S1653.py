import heapq
import math
from collections import defaultdict

class FrequencyNode:
    def __init__(self, freq=0, left=None, right=None):
        self.freq = freq
        self.left = left
        self.right = right
    
    def compute_frequency(self):
        if not self.left and not self.right:
            return self.freq
        left_val = self.left.compute_frequency() if self.left else 0
        right_val = self.right.compute_frequency() if self.right else 0
        # Logarithmic adjustment with base 2
        log_factor = math.log2(max(1, abs(left_val ^ right_val) + 1))
        self.freq = (left_val ^ right_val) & int(log_factor)
        return self.freq

def build_frequency_tree():
    # Leaf nodes
    leaf_a = FrequencyNode(12)
    leaf_b = FrequencyNode(7)
    leaf_c = FrequencyNode(25)
    leaf_d = FrequencyNode(18)
    
    # Intermediate nodes
    node_x = FrequencyNode()
    node_x.left = leaf_a
    node_x.right = leaf_b
    
    node_y = FrequencyNode()
    node_y.left = leaf_c
    node_y.right = leaf_d
    
    # Root node
    root = FrequencyNode()
    root.left = node_x
    root.right = node_y
    
    return root

tree_root = build_frequency_tree()
sync_point_frequency = tree_root.compute_frequency() ^ (tree_root.left.freq << 2)
print(f"Result: {sync_point_frequency}")