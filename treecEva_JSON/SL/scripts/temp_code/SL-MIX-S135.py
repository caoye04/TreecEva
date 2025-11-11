import math

class FrequencyNode:
    def __init__(self, frequency, gain):
        self.frequency = frequency
        self.gain = gain
        self.left = None
        self.right = None

def build_frequency_tree():
    root = FrequencyNode(1000, 2.5)
    root.left = FrequencyNode(500, 1.8)
    root.right = FrequencyNode(2000, 3.2)
    root.left.left = FrequencyNode(250, 1.2)
    root.left.right = FrequencyNode(750, 2.1)
    root.right.left = FrequencyNode(1500, 2.8)
    root.right.right = FrequencyNode(4000, 4.0)
    return root

def process_band_gain(node):
    if not node:
        return 0
    
    # Process left subtree
    left_result = process_band_gain(node.left)
    
    # Apply gain processing with modular arithmetic
    processed_gain = (math.floor(node.gain * 10) % 7) + 1
    
    # Early return for specific condition
    if node.frequency == 750:
        return processed_gain * 3
    
    # Process right subtree
    right_result = process_band_gain(node.right)
    
    # Combine results with floating point operations
    combined = (left_result + right_result + processed_gain) * 0.5
    
    return combined

def compute_signal_output():
    tree = build_frequency_tree()
    raw_output = process_band_gain(tree)
    
    # Apply final transformations
    final_output = math.ceil(raw_output * 100) / 100
    
    return final_output

final_output = compute_signal_output()
print(f"Result: {final_output}")