import math
from functools import lru_cache

def calculate_sharpe(returns, volatility):
    return returns / volatility if volatility != 0 else 0

class Portfolio:
    def __init__(self, assets):
        self.assets = assets
        
    @lru_cache(maxsize=None)
    def get_optimal_weight(self, index, remaining_budget):
        if index >= len(self.assets) or remaining_budget <= 0:
            return 0.0
        
        asset_return, asset_risk = self.assets[index]
        max_sharpe = 0.0
        
        for weight in range(0, int(remaining_budget) + 1):
            allocated = weight * 0.1
            current_sharpe = calculate_sharpe(asset_return * allocated, asset_risk * allocated)
            future_sharpe = self.get_optimal_weight(index + 1, remaining_budget - weight)
            total_sharpe = current_sharpe + future_sharpe * 0.95  # Discount factor
            max_sharpe = max(max_sharpe, total_sharpe)
            
        return max_sharpe

# Asset tuples: (expected_return, risk)
financial_assets = [
    (0.08, 0.12),
    (0.15, 0.25),
    (0.12, 0.18),
    (0.06, 0.09),
    (0.20, 0.30)
]

portfolio_optimizer = Portfolio(financial_assets)
optimal_sharpe_ratio = portfolio_optimizer.get_optimal_weight(0, 10)
print(f"Result: {round(optimal_sharpe_ratio, 6)}")