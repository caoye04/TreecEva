from collections import defaultdict, deque
import heapq

def calculate_arbitrage_opportunities(exchange_rates, start_currency):
    # Initialize distance dictionary with infinity
    distances = defaultdict(lambda: float('inf'))
    distances[start_currency] = 0
    
    # Relax edges repeatedly
    for _ in range(len(exchange_rates) - 1):
        for currency_from in exchange_rates:
            for currency_to, rate in exchange_rates[currency_from]:
                if distances[currency_from] + (-rate) < distances[currency_to]:
                    distances[currency_to] = distances[currency_from] + (-rate)
    
    # Check for negative-weight cycles
    max_profit = 0
    for currency_from in exchange_rates:
        for currency_to, rate in exchange_rates[currency_from]:
            if distances[currency_from] + (-rate) < distances[currency_to]:
                # Arbitrage opportunity found
                cycle_profit = abs(distances[currency_from] + (-rate) - distances[currency_to])
                max_profit = max(max_profit, cycle_profit)
    
    return max_profit

# Define exchange rates as a graph
exchange_graph = {
    'USD': [('EUR', -0.85), ('GBP', -0.75)],
    'EUR': [('JPY', -130.0), ('USD', -1.18)],
    'GBP': [('USD', -1.33), ('CAD', -1.71)],
    'JPY': [('EUR', -0.0077)],
    'CAD': [('GBP', -0.58)]
}

# Calculate maximum arbitrage profit
max_profit = calculate_arbitrage_opportunities(exchange_graph, 'USD')
print(f"Result: {max_profit}")