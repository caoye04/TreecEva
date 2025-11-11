import heapq
from collections import deque

def calculate_arbitrage_potential(rates, principal):
    # Priority queue for best rates (max heap using negative values)
    max_heap = []
    for rate in rates:
        heapq.heappush(max_heap, -rate)
    
    # Stack for transaction history
    transaction_log = deque()
    
    # Greedy selection of top 3 rates
    selected_rates = []
    for _ in range(min(3, len(max_heap))):
        selected_rates.append(-heapq.heappop(max_heap))
    
    # Ternary-based validation and profit calculation
    cumulative_gain = principal
    for i, rate in enumerate(selected_rates):
        is_valid = (rate > 1.0) and (i < 2 or (cumulative_gain > 1000))
        cumulative_gain = cumulative_gain * rate if is_valid else cumulative_gain
        transaction_log.append((rate, is_valid))
    
    # Final adjustment using lambda for fee calculation
    fee_deduction = (lambda amt: amt * 0.02 if amt > 1100 else amt * 0.01)(cumulative_gain)
    return cumulative_gain - fee_deduction

# Market data
exchange_rates = [1.02, 1.05, 0.99, 1.08, 1.03]
initial_capital = 1000

# Execution
final_profit = calculate_arbitrage_potential(exchange_rates, initial_capital)
print(f'Result: {final_profit}')