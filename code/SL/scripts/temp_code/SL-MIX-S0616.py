import math
from collections import deque

class InvestmentNode:
    def __init__(self, principal, rate, children=None):
        self.principal = principal
        self.rate = rate
        self.children = children if children else []

# Tree construction
portfolio_tree = InvestmentNode(1000.0, 0.05, [
    InvestmentNode(2000.0, 0.03),
    InvestmentNode(1500.0, 0.04, [
        InvestmentNode(3000.0, 0.02),
        InvestmentNode(2500.0, 0.035)
    ])
])

# Stack for tree traversal
traversal_stack = [portfolio_tree]
# Queue for processing results
processing_queue = deque()

# Process tree nodes using stack
while traversal_stack:
    node = traversal_stack.pop()
    # Calculate compound interest: P * e^(r*t) for t=1
    compounded_value = node.principal * math.exp(node.rate * 1.0)
    processing_queue.append(compounded_value)
    # Add children to stack
    traversal_stack.extend(node.children)

# Aggregate results using functional programming
final_yield = sum(map(lambda x: round(x, 2), processing_queue))

print(f"Result: {final_yield}")