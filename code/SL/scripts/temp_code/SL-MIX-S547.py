from collections import defaultdict
import math

def find_arbitrage_gain(exchange_rates, currencies, depth_limit=3):
    max_gain = 0.0
    memo = {}
    
    def dfs(current_currency, target_currency, depth, current_amount):
        if depth > depth_limit:
            return 0.0
        
        state = (current_currency, target_currency, depth)
        if state in memo:
            return memo[state]
            
        if current_currency == target_currency and depth > 0:
            return current_amount - 1.0  # Profit from starting amount of 1.0
        
        best_profit = 0.0
        for next_currency in currencies:
            if next_currency in exchange_rates[current_currency]:
                rate = exchange_rates[current_currency][next_currency]
                profit = dfs(next_currency, target_currency, depth + 1, current_amount * rate)
                best_profit = max(best_profit, profit)
        
        memo[state] = best_profit
        return best_profit
    
    for start_currency in currencies:
        for end_currency in currencies:
            gain = dfs(start_currency, end_currency, 0, 1.0)
            max_gain = max(max_gain, gain)
    
    return round(max_gain, 6)

# Exchange rates between currencies represented as a graph
exchange_network = defaultdict(dict)
exchange_network['USD']['EUR'] = 0.85
exchange_network['EUR']['GBP'] = 0.88
exchange_network['GBP']['JPY'] = 151.32
exchange_network['JPY']['USD'] = 0.0067
exchange_network['USD']['JPY'] = 149.25
exchange_network['JPY']['EUR'] = 0.0059

available_currencies = frozenset(['USD', 'EUR', 'GBP', 'JPY'])

max_arbitrage_gain = find_arbitrage_gain(exchange_network, available_currencies, 4)
print(f"Result: {max_arbitrage_gain}")