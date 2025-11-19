import heapq
from collections import defaultdict

def calculate_max_arbitrage_gain():
    # Currency exchange rates (source, destination, rate)
    exchange_rates = [
        ('USD', 'EUR', 0.85),
        ('EUR', 'GBP', 0.88),
        ('GBP', 'JPY', 150.0),
        ('JPY', 'USD', 0.0067),
        ('USD', 'CAD', 1.25),
        ('CAD', 'AUD', 1.12),
        ('AUD', 'USD', 0.72)
    ]
    
    currencies = ['USD', 'EUR', 'GBP', 'JPY', 'CAD', 'AUD']
    
    # Initialize DP table for max profit from USD to each currency
    max_profit = defaultdict(lambda: 0.0)
    max_profit['USD'] = 1.0
    
    # Priority queue for processing: (-profit, currency)
    pq = [(-1.0, 'USD')]
    
    # Track visited states to avoid cycles
    visited = set()
    
    max_arbitrage_gain = 0.0
    
    while pq:
        neg_profit, current_currency = heapq.heappop(pq)
        current_profit = -neg_profit
        
        if current_currency in visited and current_profit <= max_profit[current_currency]:
            continue
            
        visited.add(current_currency)
        max_profit[current_currency] = max(max_profit[current_currency], current_profit)
        
        # Early termination if we've found a good arbitrage path
        if current_profit > 1.2:
            potential_gain = current_profit - 1.0
            if potential_gain > max_arbitrage_gain:
                max_arbitrage_gain = potential_gain
                if max_arbitrage_gain > 0.3:  # Break early for significant gains
                    break
        
        # Explore neighbors
        for src, dst, rate in exchange_rates:
            if src == current_currency:
                new_profit = current_profit * rate
                if new_profit > max_profit[dst]:
                    max_profit[dst] = new_profit
                    heapq.heappush(pq, (-new_profit, dst))
    
    # Convert to basis points for precision
    max_arbitrage_gain = int(max_arbitrage_gain * 10000)
    return max_arbitrage_gain

# Lambda to adjust final result based on market friction
adjust_for_market_friction = lambda gain: gain - (gain // 10)

raw_gain = calculate_max_arbitrage_gain()
max_arbitrage_gain = adjust_for_market_friction(raw_gain)
print(f"Result: {max_arbitrage_gain}")