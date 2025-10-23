from dataclasses import dataclass
from typing import List, Dict
import math

def calculate_sharpe_ratio(returns: float, volatility: float) -> float:
    return returns / volatility if volatility != 0 else 0

def compute_transaction_cost(shares: int, price: float, fee_rate: float) -> float:
    return shares * price * fee_rate

def greedy_asset_selector(assets: List[Dict], budget: float) -> List[Dict]:
    # Sort by Sharpe ratio descending
    sorted_assets = sorted(assets, key=lambda x: x['sharpe'], reverse=True)
    selected = []
    total_cost = 0.0
    
    for asset in sorted_assets:
        cost = asset['shares'] * asset['price']
        if total_cost + cost <= budget:
            selected.append(asset)
            total_cost += cost
        else:
            break
    return selected

def dp_optimize_sequence(assets: List[Dict], max_transactions: int) -> float:
    n = len(assets)
    if n == 0:
        return 0.0
    
    # dp[i][j] represents max profit with i transactions using first j assets
    dp = [[0.0 for _ in range(n+1)] for _ in range(max_transactions+1)]
    
    for i in range(1, max_transactions+1):
        max_diff = -float('inf')
        for j in range(1, n+1):
            # Profit from selling current asset
            profit = assets[j-1]['expected_return'] - compute_transaction_cost(
                assets[j-1]['shares'], 
                assets[j-1]['price'], 
                assets[j-1]['fee_rate']
            )
            max_diff = max(max_diff, dp[i-1][j-1] - profit)
            dp[i][j] = max(dp[i][j-1], max_diff + profit)
    
    return dp[max_transactions][n]

# Asset data with financial metrics
financial_assets = [
    {'symbol': 'TECH', 'shares': 100, 'price': 150.50, 'volatility': 0.25, 'expected_return': 1200.0, 'fee_rate': 0.005},
    {'symbol': 'BIOTECH', 'shares': 50, 'price': 85.75, 'volatility': 0.35, 'expected_return': 800.0, 'fee_rate': 0.007},
    {'symbol': 'ENERGY', 'shares': 200, 'price': 65.25, 'volatility': 0.20, 'expected_return': 950.0, 'fee_rate': 0.003},
    {'symbol': 'REIT', 'shares': 75, 'price': 110.00, 'volatility': 0.15, 'expected_return': 600.0, 'fee_rate': 0.004},
    {'symbol': 'BOND', 'shares': 300, 'price': 95.40, 'volatility': 0.05, 'expected_return': 250.0, 'fee_rate': 0.002}
]

# Calculate Sharpe ratios for all assets
for asset in financial_assets:
    asset['sharpe'] = calculate_sharpe_ratio(asset['expected_return'], asset['volatility'])

# Apply greedy selection with budget constraint
budget_limit = 15000.0
selected_assets = greedy_asset_selector(financial_assets, budget_limit)

# Optimize transaction sequence with DP
max_allowed_transactions = 3
optimal_sequence_profit = dp_optimize_sequence(selected_assets, max_allowed_transactions)

# Adjust for market impact factor
market_impact_factor = 0.95
adjusted_profit = optimal_sequence_profit * market_impact_factor

# Final calculation incorporating risk-free rate
risk_free_rate = 0.02
final_adjusted_value = adjusted_profit * (1 + risk_free_rate)

# Update optimal_sequence_profit with final calculation
optimal_sequence_profit = round(final_adjusted_value, 2)
print(f"Result: {optimal_sequence_profit}")