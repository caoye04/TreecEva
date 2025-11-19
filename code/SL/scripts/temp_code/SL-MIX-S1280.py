import math

def calculate_volatility(prices):
    returns = [math.log(prices[i]/prices[i-1]) for i in range(1, len(prices))]
    mean_return = sum(returns) / len(returns)
    variance = sum((r - mean_return)**2 for r in returns) / len(returns)
    return math.sqrt(variance)

class PortfolioManager:
    def __init__(self, assets):
        self.assets = assets
        self.weights = {asset: 1/len(assets) for asset in assets}
    
    def rebalance_greedily(self, target_weights, max_adjustment=0.1):
        adjustments = {}
        for asset in self.assets:
            diff = target_weights.get(asset, 0) - self.weights[asset]
            # Greedy adjustment: move maximum allowed toward target
            adjustments[asset] = max(-max_adjustment, min(diff, max_adjustment))
        return adjustments

def simulate_quarterly_rebalancing():
    assets = ['TECH', 'BONDS', 'COMMODITIES', 'REIT']
    manager = PortfolioManager(assets)
    
    # Quarterly target weight adjustments
    quarterly_targets = [
        {'TECH': 0.4, 'BONDS': 0.3, 'COMMODITIES': 0.2, 'REIT': 0.1},
        {'TECH': 0.35, 'BONDS': 0.35, 'COMMODITIES': 0.2, 'REIT': 0.1},
        {'TECH': 0.3, 'BONDS': 0.4, 'COMMODITIES': 0.2, 'REIT': 0.1},
        {'TECH': 0.25, 'BONDS': 0.45, 'COMMODITIES': 0.2, 'REIT': 0.1}
    ]
    
    cumulative_adjustments = {asset: 0.0 for asset in assets}
    
    for q, targets in enumerate(quarterly_targets, 1):
        adjustments = manager.rebalance_greedily(targets)
        for asset, adj in adjustments.items():
            cumulative_adjustments[asset] += adj
            manager.weights[asset] += adj
    
    # Calculate the optimal quarterly adjustment as the sum of absolute adjustments
    optimal_quarterly_adjustment = sum(abs(adj) for adj in cumulative_adjustments.values())
    
    # Apply a volatility-based modifier using the calculate_volatility function
    price_series = [100, 105.5, 102.3, 108.7, 110.2]
    vol_modifier = calculate_volatility(price_series)
    
    # Final adjustment incorporates market volatility
    optimal_quarterly_adjustment *= (1 + vol_modifier)
    
    return round(optimal_quarterly_adjustment, 6)

# Execute the simulation
optimal_quarterly_adjustment = simulate_quarterly_rebalancing()
print(f"Result: {optimal_quarterly_adjustment}")