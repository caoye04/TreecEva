import math

class InterestNode:
    def __init__(self, adjustment_factor, next_node=None):
        self.factor = adjustment_factor
        self.next = next_node

# Build linked list with adjustment factors
root = InterestNode(1.05)
root.next = InterestNode(0.98)
root.next.next = InterestNode(1.02)
root.next.next.next = InterestNode(1.07)

# Initial values
principal = 10000.0
scaling_base = 2.71828  # e

# Process adjustments using list comprehension and lambda
adjustments = []
node = root
while node:
    adjustments.append(node.factor)
    node = node.next

# Apply compounded adjustments with logarithmic scaling
log_sum = sum([math.log(factor) for factor in adjustments])
compound_effect = math.exp(log_sum)

# Calculate final yield with lambda transformation
yield_transform = lambda p, effect: p * (effect + 0.01 * math.log(effect))
final_yield = yield_transform(principal, compound_effect)

print(f"Result: {final_yield}")