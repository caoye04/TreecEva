import math
from collections import deque

class PriceNode:
    def __init__(self, price_change, next_node=None):
        self.price_change = price_change
        self.next = next_node

def calculate_volatility(head_node):
    volatility_stack = []
    transaction_queue = deque()
    volatility_score = 0.0
    
    # Initialize queue with absolute values of changes
    current = head_node
    while current:
        transaction_queue.append(abs(current.price_change))
        current = current.next
    
    # Process transactions
    while transaction_queue:
        change = transaction_queue.popleft()
        if change == 0:
            continue
        elif change < 0.5:
            # Small change case - use linear scaling
            scaled_change = change * 2
            volatility_stack.append(scaled_change)
        elif change >= 0.5 and change < 2.0:
            # Medium change case - use logarithmic scaling
            scaled_change = math.log(change + 1)
            volatility_stack.append(scaled_change)
        else:
            # Large change case - use exponential dampening
            scaled_change = 1 - math.exp(-change)
            volatility_stack.append(scaled_change)
    
    # Calculate final score
    while volatility_stack:
        value = volatility_stack.pop()
        if value > 0.8:
            volatility_score += value * 1.5
        elif value > 0.3:
            volatility_score += value
        else:
            volatility_score += value * 0.5
    
    return round(volatility_score, 6)

# Create linked list: 0.1 -> 1.5 -> 3.0 -> 0.0 -> 0.75
node5 = PriceNode(0.75)
node4 = PriceNode(0.0, node5)
node3 = PriceNode(3.0, node4)
node2 = PriceNode(1.5, node3)
node1 = PriceNode(0.1, node2)

volatility_score = calculate_volatility(node1)
print(f"Result: {volatility_score}")