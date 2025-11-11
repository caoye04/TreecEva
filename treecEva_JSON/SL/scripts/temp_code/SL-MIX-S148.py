import math

# Asset data: {asset_id: expected_return}
assets = {
    'AAPL': 0.08,
    'GOOGL': 0.12,
    'MSFT': 0.10,
    'AMZN': 0.15,
    'TSLA': 0.20
}

# Correlation matrix between assets (simplified)
correlations = {
    ('AAPL', 'GOOGL'): 0.7,
    ('AAPL', 'MSFT'): 0.6,
    ('AAPL', 'AMZN'): 0.5,
    ('AAPL', 'TSLA'): 0.3,
    ('GOOGL', 'MSFT'): 0.8,
    ('GOOGL', 'AMZN'): 0.4,
    ('GOOGL', 'TSLA'): 0.2,
    ('MSFT', 'AMZN'): 0.6,
    ('MSFT', 'TSLA'): 0.4,
    ('AMZN', 'TSLA'): 0.1
}

# Convert to symmetric matrix
symmetric_correlations = {}
for (a, b), corr in correlations.items():
    symmetric_correlations[(a, b)] = corr
    symmetric_correlations[(b, a)] = corr

# Add diagonal (self-correlation = 1.0)
for asset in assets:
    symmetric_correlations[(asset, asset)] = 1.0

# Greedy selection function
selection_score = lambda asset, selected: (
    assets[asset] - 0.3 * sum(symmetric_correlations[(asset, s)] for s in selected)
)

# Initialize
selected_assets = []
portfolio_weights = {}

# Greedy selection (3 iterations)
for _ in range(3):
    best_asset = None
    best_score = -float('inf')
    
    for asset in assets:
    
        if asset not in selected_assets:
            score = selection_score(asset, selected_assets)
            if score > best_score:
                best_score = score
                best_asset = asset
    
    if best_asset:
        selected_assets.append(best_asset)
        # Weight calculation (simplified)
        weight = round(math.sqrt(assets[best_asset]) / sum(math.sqrt(assets[a]) for a in selected_assets), 4)
        portfolio_weights[best_asset] = weight

# Calculate diversity score
portfolio_diversity_score = 0.0
for i, asset1 in enumerate(selected_assets):
    for asset2 in selected_assets[i+1:]:
        correlation = symmetric_correlations[(asset1, asset2)]
        weight_product = portfolio_weights[asset1] * portfolio_weights[asset2]
        portfolio_diversity_score += weight_product * (1.0 - correlation)

# Normalize and scale
portfolio_diversity_score = round(portfolio_diversity_score * 100, 2)

print(f"Result: {portfolio_diversity_score}")