import math
from collections import defaultdict, deque

def compute_volatility_adjustments():
    # Market data represented as (day, return_percentage)
    market_returns = [(1, 2.5), (2, -1.2), (3, 3.8), (4, -0.5), (5, 1.1)]
    weights = [0.1, 0.15, 0.2, 0.25, 0.3]
    
    # Step 1: Calculate weighted log returns
    weighted_log_returns = []
    for i, (_, ret) in enumerate(market_returns):
        log_return = math.log(1 + ret/100)
        weighted_log_returns.append(log_return * weights[i])
    
    # Step 2: Binary tree construction for smoothing (simplified)
    # Each node stores sum of its children
    tree = defaultdict(float)
    leaves_start_index = 4  # For 5 leaves, internal nodes start at index 4
    
    # Fill leaves
    for i in range(5):
        tree[leaves_start_index + i] = weighted_log_returns[i]
    
    # Build tree bottom-up
    for i in range(leaves_start_index - 1, -1, -1):
        tree[i] = tree[2*i+1] + tree[2*i+2]
    
    # Step 3: Greedy selection of adjustment factors
    # We select factors from a predefined set that minimize cumulative error
    adjustment_options = [0.95, 0.97, 0.99, 1.0, 1.01, 1.03, 1.05]
    target_value = tree[0]  # Root of the tree
    
    best_error = float('inf')
    final_adjustment_factor = 1.0
    
    for factor in adjustment_options:
        adjusted_value = target_value * factor
        error = abs(math.exp(abs(adjusted_value)) - math.exp(abs(target_value)))
        if error < best_error:
            best_error = error
            final_adjustment_factor = factor
    
    # Final calculation combines exponentiation and a last adjustment
    final_value = math.exp(tree[0]) * final_adjustment_factor
    
    # Update the adjustment factor with a precision-based modification
    precision_boost = 1 + (final_adjustment_factor - 1) / 2
    final_adjustment_factor = round(final_adjustment_factor * precision_boost, 4)
    
    return final_adjustment_factor

# Execute the computation
final_adjustment_factor = compute_volatility_adjustments()
print(f"Result: {final_adjustment_factor}")