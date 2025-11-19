from collections import defaultdict
import math

def compute_daily_rates(base_rate, days):
    fib_cache = defaultdict(int)
    fib_cache[0], fib_cache[1] = 1, 1
    
    def fib(n):
        if n in fib_cache:
            return fib_cache[n]
        fib_cache[n] = fib(n-1) + fib(n-2)
        return fib_cache[n]
    
    rates = []
    for i in range(days):
        adjustment = fib(i) * 0.0001
        daily_rate = base_rate + adjustment
        rates.append(daily_rate)
    return rates

def compound_interest_with_fibonacci_modifiers(principal, base_rate, days):
    rates = compute_daily_rates(base_rate, days)
    balance = principal
    for rate in rates:
        balance *= (1 + rate)
        balance = round(balance, 2)  # Financial rounding
    return balance

# Parameters
initial_investment = 10000.00
annual_base_rate = 0.05
compounding_days = 10

# Convert annual rate to daily equivalent
base_daily_rate = annual_base_rate / 365

# Compute final balance
accumulated_balance = compound_interest_with_fibonacci_modifiers(initial_investment, base_daily_rate, compounding_days)
print(f"Result: {accumulated_balance}")