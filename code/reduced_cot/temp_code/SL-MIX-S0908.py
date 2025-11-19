from functools import reduce

def compute_portfolio_adjustment():
    transactions = [120, -50, 30, -10, 80, -5, 60]
    cumulative_impacts = [0] * (len(transactions) + 1)
    weights = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
    
    # Lambda to calculate weighted impact
    weighted_impact = lambda val, weight: val * weight if val > 0 else val * (weight + 0.1)
    
    for i in range(1, len(transactions) + 1):
        current_transaction = transactions[i-1]
        current_weight = weights[i-1] if i-1 < len(weights) else 0.7
        
        # Compute the weighted impact
        impact = weighted_impact(current_transaction, current_weight)
        
        # Update cumulative impact
        cumulative_impacts[i] = cumulative_impacts[i-1] + impact
        
        # Early return if cumulative impact drops below -100
        if cumulative_impacts[i] < -100:
            return -1
    
    # Calculate adjustment factor using reduce
    adjustment_factor = reduce(lambda x, y: x + y if y > 0 else x - abs(y), cumulative_impacts, 0)
    return adjustment_factor

# Execution
adjustment_factor = compute_portfolio_adjustment()
print(f"Result: {adjustment_factor}")