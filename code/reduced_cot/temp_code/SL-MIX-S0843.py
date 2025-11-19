from dataclasses import dataclass
from typing import List
import math

def calculate_adjustment_factor(market_signal: str, volatility_index: float) -> float:
    if market_signal == 'bull':
        return 1.0 + (volatility_index * 0.1)
    elif market_signal == 'bear':
        return 1.0 - (volatility_index * 0.05)
    else:  # 'stable'
        return 1.0 + (volatility_index * 0.02)

def process_day(portfolio_value: float, signal: str, vol_idx: float) -> float:
    factor = calculate_adjustment_factor(signal, vol_idx)
    adjusted_value = portfolio_value * factor
    # Transaction cost is 0.1% of transaction volume
    transaction_cost = abs(adjusted_value - portfolio_value) * 0.001
    return adjusted_value - transaction_cost

@dataclass
class MarketDay:
    signal: str
    volatility: float

# Initial portfolio setup
portfolio_value = 100000.0
market_conditions: List[MarketDay] = [
    MarketDay('bull', 0.8),
    MarketDay('stable', 0.2),
    MarketDay('bear', 1.2),
    MarketDay('bull', 0.5),
    MarketDay('bear', 0.9)
]

# Process each market day with greedy strategy (always execute full adjustment)
for day in market_conditions:
    portfolio_value = process_day(portfolio_value, day.signal, day.volatility)
    # Cap adjustment to prevent extreme growth/decline
    if portfolio_value > 150000:
        portfolio_value = 150000
    elif portfolio_value < 50000:
        portfolio_value = 50000

final_portfolio_value = round(portfolio_value, 2)
print(f'Result: {final_portfolio_value}')