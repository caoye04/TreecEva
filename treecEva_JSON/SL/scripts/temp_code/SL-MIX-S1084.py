from collections import deque

class FrequencyNode:
    def __init__(self, frequency_band=None):
        self.band = frequency_band
        self.left = None
        self.right = None
        self.processed_value = 0.0

def build_frequency_tree():
    # Build a small binary tree representing frequency bands
    root = FrequencyNode(128.5)
    root.left = FrequencyNode(64.25)
    root.right = FrequencyNode(32.125)
    root.left.left = FrequencyNode(16.0625)
    root.left.right = FrequencyNode(8.03125)
    return root

def process_signal_tree(node):
    if not node:
        return 0
    
    # Base case: leaf nodes
    if not node.left and not node.right:
        # Convert frequency to integer for bitwise ops, then back to float
        int_part = int(node.band * 10000) & 0xFFFF
        node.processed_value = float(int_part) / 10000.0
        return int_part
    
    # Process children first
    left_val = process_signal_tree(node.left)
    right_val = process_signal_tree(node.right)
    
    # Apply different operations based on node band value
    band_int = int(node.band)
    if band_int > 100:
        result = left_val ^ right_val
    elif band_int > 50:
        result = left_val & right_val
    else:
        result = left_val | right_val
    
    # Add floating point adjustment
    node.processed_value = float(result) + (node.band - int(node.band))
    return result

tree_root = build_frequency_tree()
final_root_value = process_signal_tree(tree_root)
print(f"Result: {final_root_value}")