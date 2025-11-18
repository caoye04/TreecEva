import math
from collections import defaultdict
from itertools import combinations_with_replacement

class TernaryTreeNode:
    def __init__(self, value=0, depth=0):
        self.value = value
        self.depth = depth
        self.children = []

# Initialize root node
root = TernaryTreeNode(value=100, depth=0)

# Build ternary tree up to depth 3
nodes_at_depth = defaultdict(list)
nodes_at_depth[0].append(root)

for d in range(1, 4):
    for parent in nodes_at_depth[d-1]:
        # Each node has 3 children in a ternary tree
        for i in range(3):
            child_value = parent.value // (2 + i)  # Decreasing child values
            child = TernaryTreeNode(child_value, d)
            parent.children.append(child)
            nodes_at_depth[d].append(child)

# Calculate signal strength for each node at depth 3
cumulative_signal = 0
signal_factors = []

for node in nodes_at_depth[3]:
    # Logarithmic decay factor based on node value
    log_factor = math.log(node.value + 1)
    
    # Combinatorial amplification using node value digits
    digit_sum = sum(int(digit) for digit in str(node.value))
    comb_amplification = len(list(combinations_with_replacement(range(digit_sum % 5 + 1), 2)))
    
    # Signal strength is product of factors
    signal_strength = log_factor * comb_amplification
    signal_factors.append(signal_strength)

# Apply exponential weighting to cumulative calculation
for i, factor in enumerate(signal_factors):
    weighted_factor = factor * (math.e ** (i % 3))
    cumulative_signal += weighted_factor

# Final adjustment using bit manipulation pattern
bit_pattern = int('10110', 2)
cumulative_signal = int(cumulative_signal) ^ bit_pattern

print(f"Result: {cumulative_signal}")