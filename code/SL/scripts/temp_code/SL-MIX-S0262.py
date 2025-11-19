import math

def compute_portfolio_score(returns, categories):
    # Normalize returns using logarithmic scaling
    scaled_returns = [math.log(r + 1) for r in returns]
    
    # Greedy selection: pick top 2 returns
    scaled_returns.sort(reverse=True)
    selected = scaled_returns[:2]
    
    # Calculate exponential weight sum
    weighted_sum = sum(math.exp(r) for r in selected)
    
    # Set operations on categories
    unique_categories = frozenset(categories)
    base_set = {'equity', 'bond', 'commodity'}
    intersection = unique_categories & base_set
    
    # Logical operations to determine bonus
    has_equity = 'equity' in intersection
    has_bond = 'bond' in intersection
    bonus = 1.5 if (has_equity and not has_bond) else 1.0
    
    # Final score calculation
    final_score = weighted_sum * len(intersection) * bonus
    return final_score

# Portfolio data
asset_returns = [0.05, 0.12, 0.08, 0.15, 0.03]
asset_categories = ['equity', 'real_estate', 'equity', 'commodity', 'bond']

# Compute and print result
final_score = compute_portfolio_score(asset_returns, asset_categories)
print(f"Result: {final_score}")