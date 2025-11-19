import heapq
from functools import reduce

def calculate_volatility(transactions):
    return sum(abs(t['close'] - t['open']) for t in transactions) / len(transactions)

def adjust_weights(market_condition, base_weight):
    return base_weight * 1.5 if market_condition == 'bullish' else base_weight * 0.8 if market_condition == 'bearish' else base_weight

# Portfolio data
portfolio_data = [
    {'symbol': 'TECH', 'transactions': [{'open': 100, 'close': 105}, {'open': 105, 'close': 110}]},
    {'symbol': 'HEALTH', 'transactions': [{'open': 80, 'close': 75}, {'open': 75, 'close': 85}]},
    {'symbol': 'ENERGY', 'transactions': [{'open': 50, 'close': 55}, {'open': 55, 'close': 45}]}
]

market_trend = 'bullish'
base_allocation = {'TECH': 0.4, 'HEALTH': 0.35, 'ENERGY': 0.25}

# Calculate volatility scores and build priority queue
volatility_scores = {item['symbol']: calculate_volatility(item['transactions']) for item in portfolio_data}
heap = [(-volatility_scores[symbol], symbol) for symbol in volatility_scores]
heapq.heapify(heap)

# Process top volatile assets
top_volatile_assets = []
for _ in range(2):
    if heap:
        _, symbol = heapq.heappop(heap)
        top_volatile_assets.append(symbol)

# Adjust weights for top volatile assets
adjusted_weights = {symbol: adjust_weights(market_trend, base_allocation[symbol]) for symbol in top_volatile_assets}

# Calculate rebalancing score using adjusted weights and volatility
rebalancing_components = {symbol: adjusted_weights[symbol] * volatility_scores[symbol] for symbol in adjusted_weights}
rebalancing_score = reduce(lambda x, y: x + y, rebalancing_components.values(), 0) if rebalancing_components else 0

# Apply final adjustment based on number of volatile assets
rebalancing_score = rebalancing_score * 1.2 if len(top_volatile_assets) >= 2 else rebalancing_score

print(f"Result: {round(rebalancing_score, 2)}")