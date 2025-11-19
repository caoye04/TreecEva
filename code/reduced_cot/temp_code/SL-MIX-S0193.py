from collections import defaultdict
import math

class SignalNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Initialize signal processing tree
root = SignalNode(15)
root.left = SignalNode(7)
root.right = SignalNode(22)
root.left.left = SignalNode(3)
root.left.right = SignalNode(11)
root.right.left = SignalNode(19)
root.right.right = SignalNode(25)

# Signal processing function
def process_signal(node):
    if not node:
        return 0
    
    # Apply logarithmic transformation if value > 10
    transformed_value = math.log(node.value) if node.value > 10 else node.value
    
    # Recursively process children and combine with bitwise operations
    left_result = process_signal(node.left)
    right_result = process_signal(node.right)
    
    # Combine results using XOR for left, OR for right
    combined = (int(transformed_value) ^ int(left_result)) | int(right_result)
    
    return combined

# Initial signal parameters
signal_amplitudes = [2, 4, 8, 16, 32]
attenuation_factors = [0.5, 0.25, 0.75, 0.125, 1.0]

# Apply attenuation and collect results
attenuated_signals = [amp * att for amp, att in zip(signal_amplitudes, attenuation_factors)]

# Create lookup for processed signals
signal_lookup = defaultdict(lambda: 0)
for i, signal in enumerate(attenuated_signals):
    signal_lookup[i] = int(signal) if signal.is_integer() else round(signal, 2)

# Process the signal tree
tree_result = process_signal(root)

# Apply final transformation using collected signals
processed_signal_strength = tree_result
for key in sorted(signal_lookup.keys(), reverse=True):
    if key % 2 == 0 and signal_lookup[key] > 5:
        processed_signal_strength = processed_signal_strength & int(signal_lookup[key])
    elif key % 2 != 0 or signal_lookup[key] <= 5:
        processed_signal_strength = processed_signal_strength | int(signal_lookup[key])

# Final adjustment
if processed_signal_strength > 20:
    processed_signal_strength = processed_signal_strength >> 1

print(f"Result: {processed_signal_strength}")