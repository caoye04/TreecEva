import heapq
from functools import reduce

def compute_volatility(asset_tree, market_state):
    # State machine for market conditions
    state_weights = {'bull': 1.2, 'bear': 1.8, 'neutral': 1.0}
    adjustment_factor = state_weights.get(market_state, 1.0)
    
    # Binary tree traversal to collect risk factors
    risk_heap = []
    stack = [asset_tree]
    
    while stack:
        node = stack.pop()
        if isinstance(node, dict):
            factor = node.get('risk', 0)
            weight = node.get('weight', 1)
            adjusted = factor * weight * adjustment_factor
            heapq.heappush(risk_heap, -adjusted)  # Max-heap using negative values
            
            # Traverse children
            left = node.get('left')
            right = node.get('right')
            if left: stack.append(left)
            if right: stack.append(right)
    
    # Nested loop processing with lambda and ternary
    cumulative_impact = 0
    for _ in range(min(3, len(risk_heap))):
        top_risk = -heapq.heappop(risk_heap)
        modifiers = [lambda x: x*1.1, lambda x: x*0.95, lambda x: x+2]
        temp_value = top_risk
        for mod in modifiers:
            temp_value = mod(temp_value) if temp_value > 10 else temp_value
        cumulative_impact += temp_value
    
    # Final calculation using reduce and ternary operator
    base_index = reduce(lambda acc, val: acc + (val**2 if val > 5 else val*2), [cumulative_impact, 3.5, 2.1], 0)
    final_risk_score = base_index if base_index > 50 else base_index * 1.5
    return final_risk_score

# Asset hierarchy as binary tree
portfolio = {
    'risk': 12,
    'weight': 1.5,
    'left': {
        'risk': 8,
        'weight': 1.2,
        'left': {'risk': 5, 'weight': 1.0},
        'right': {'risk': 3, 'weight': 0.8}
    },
    'right': {
        'risk': 15,
        'weight': 1.8,
        'left': {'risk': 7, 'weight': 1.1},
        'right': {'risk': 10, 'weight': 1.3}
    }
}

final_risk_score = compute_volatility(portfolio, 'bear')
print(f"Result: {final_risk_score}")