from functools import reduce
from collections import defaultdict

def compute_adjusted_performance(transactions):
    volume_weights = defaultdict(float)
    daily_returns = []
    
    for day, trades in enumerate(transactions):
        daily_volume = sum(trade['quantity'] for trade in trades)
        if daily_volume == 0:
            continue
            
        weighted_return = 0.0
        for trade in trades:
            weight = trade['quantity'] / daily_volume
            volume_weights[trade['symbol']] += weight
            weighted_return += weight * trade['return_rate']
            
        if day > 0 and abs(weighted_return) > 0.05:
            weighted_return *= 1.1  # Volatility adjustment
            
        daily_returns.append(weighted_return)
    
    avg_daily_return = reduce(lambda x, y: x + y, daily_returns) / len(daily_returns) if daily_returns else 0
    concentration_factor = reduce(lambda acc, w: acc + w**2, volume_weights.values(), 0)
    
    portfolio_index = round((avg_daily_return * 1000) / (1 + concentration_factor), 2)
    return portfolio_index

# Transaction log data
transaction_log = [
    [{'symbol': 'TECH', 'quantity': 150, 'return_rate': 0.023}, {'symbol': 'ENERGY', 'quantity': 100, 'return_rate': -0.012}],
    [{'symbol': 'TECH', 'quantity': 200, 'return_rate': 0.031}, {'symbol': 'HEALTH', 'quantity': 120, 'return_rate': 0.018}],
    [{'symbol': 'FINANCE', 'quantity': 80, 'return_rate': -0.025}, {'symbol': 'ENERGY', 'quantity': 90, 'return_rate': 0.041}],
    [{'symbol': 'TECH', 'quantity': 110, 'return_rate': 0.067}, {'symbol': 'HEALTH', 'quantity': 70, 'return_rate': -0.009}]
]

portfolio_index = compute_adjusted_performance(transaction_log)
print(f"Result: {portfolio_index}")