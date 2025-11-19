from dataclasses import dataclass
from typing import List, Tuple
import math

def calculate_volatility_modifier(base_value: float, trade_count: int) -> float:
    return 1.0 + (math.log(trade_count + 1) / 10) if trade_count > 0 else 1.0

def apply_market_sentiment(value: float, sentiment: str) -> float:
    return value * (1.1 if sentiment == 'bullish' else 0.95 if sentiment == 'bearish' else 1.0)

@dataclass
class Portfolio:
    assets: dict
    performance_weights: dict
    
    def get_weighted_value(self, asset_name: str) -> float:
        base_value = self.assets.get(asset_name, 0)
        weight = self.performance_weights.get(asset_name, 1.0)
        return base_value * weight

# Initialize portfolio with cryptocurrency holdings
portfolio_data = {
    'BTC': 2.5,
    'ETH': 15.0,
    'SOL': 100.0,
    'ADA': 5000.0
}

weight_mapping = {
    'BTC': 1.2,
    'ETH': 1.1,
    'SOL': 0.9,
    'ADA': 0.8
}

portfolio = Portfolio(portfolio_data, weight_mapping)

# Transaction processing log
transactions = [
    ('BTC', -0.5, 'bullish'),
    ('ETH', 5.0, 'neutral'),
    ('SOL', -25.0, 'bearish'),
    ('ADA', 1000.0, 'bullish')
]

trade_counts = {'BTC': 12, 'ETH': 8, 'SOL': 5, 'ADA': 20}

# Processing engine
adjusted_values = {}
for asset, amount, sentiment in transactions:
    if asset in portfolio.assets:
        portfolio.assets[asset] += amount
        raw_value = portfolio.get_weighted_value(asset)
        vol_modifier = calculate_volatility_modifier(raw_value, trade_counts[asset])
        adjusted_value = apply_market_sentiment(raw_value * vol_modifier, sentiment)
        adjusted_values[asset] = adjusted_value
    else:
        continue

# Calculate portfolio metrics
portfolio_sum = sum(adjusted_values.values())
threshold_check = portfolio_sum > 1000

final_adjusted_value = (
    portfolio_sum * 1.05 if threshold_check else 
    sum([v for k, v in adjusted_values.items() if k in ['BTC', 'ETH']])
) if len(adjusted_values) >= 3 else 0.0

print(f"Result: {final_adjusted_value}")