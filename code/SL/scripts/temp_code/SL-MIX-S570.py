from collections import defaultdict, deque
from itertools import permutations
import math

def calculate_arbitrage_opportunity(rates_chain):
    profit = 1.0
    for i in range(len(rates_chain) - 1):
        if rates_chain[i] == rates_chain[i+1]:
            return 0  # No profit in same currency exchange
        profit *= exchange_matrix[rates_chain[i]][rates_chain[i+1]]
    return profit - 1.0  # Net profit minus initial investment

def update_max_profit(current_path):
    global max_arbitrage_profit
    profit = calculate_arbitrage_opportunity(current_path)
    if profit > max_arbitrage_profit:
        max_arbitrage_profit = profit

# Currency exchange matrix representing exchange rates
exchange_matrix = defaultdict(lambda: defaultdict(float))
currencies = ['USD', 'EUR', 'GBP', 'JPY', 'CAD']

# Initialize exchange rates
rates_data = [
    ('USD', 'EUR', 0.85),
    ('USD', 'GBP', 0.75),
    ('USD', 'JPY', 110.0),
    ('USD', 'CAD', 1.25),
    ('EUR', 'GBP', 0.88),
    ('EUR', 'JPY', 129.0),
    ('EUR', 'CAD', 1.47),
    ('GBP', 'JPY', 147.0),
    ('GBP', 'CAD', 1.67),
    ('JPY', 'CAD', 0.011)
]

for src, dst, rate in rates_data:
    exchange_matrix[src][dst] = rate
    exchange_matrix[dst][src] = 1.0 / rate

# State machine for processing arbitrage detection
state = 'INIT'
max_arbitrage_profit = 0.0
visited_paths = set()

for perm in permutations(currencies, 4):
    path_key = ''.join(perm)
    if path_key in visited_paths:
        continue
    
    # Add reverse path to avoid duplication
    visited_paths.add(path_key)
    reverse_key = ''.join(reversed(perm))
    visited_paths.add(reverse_key)
    
    # State transitions
    if state == 'INIT':
        state = 'PROCESSING' if len(perm) >= 3 else 'SKIP'
    
    if state == 'PROCESSING':
        # Check for early termination conditions
        if perm[0] == perm[-1]:
            state = 'CYCLE_COMPLETE'
            continue
        
        cycle_path = list(perm) + [perm[0]]  # Complete the cycle
        update_max_profit(cycle_path)
        
        # Optimization: break if profit exceeds threshold
        if max_arbitrage_profit > 0.2:
            state = 'THRESHOLD_REACHED'
            break
    elif state == 'SKIP':
        continue
    elif state == 'CYCLE_COMPLETE':
        if max_arbitrage_profit > 0.15:
            break
    elif state == 'THRESHOLD_REACHED':
        break

# Final adjustment based on market volatility
if max_arbitrage_profit > 0:
    max_arbitrage_profit = round(max_arbitrage_profit, 4)

print(f"Result: {max_arbitrage_profit}")