from functools import reduce
import math

def fibonacci_sequence(n):
    a, b = 1, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

def parse_stock_prices(raw_data):
    tokens = raw_data.split(',')
    return [float(token.strip()) for token in tokens]

# Stock data and parameters
stock_data = "10.5, 20.0, 15.25, 30.75, 25.0"
budget = 100.0

# Process pipeline
prices = parse_stock_prices(stock_data)
fib_multipliers = fibonacci_sequence(len(prices))
adjusted_prices = [p * m for p, m in zip(prices, fib_multipliers)]

# Greedy selection of stocks
remaining_budget = budget
total_shares = 0
for price in sorted(adjusted_prices):
    if remaining_budget >= price:
        shares = math.floor(remaining_budget / price)
        total_shares += shares
        remaining_budget -= shares * price
    else:
        break

print(f"Result: {total_shares}")