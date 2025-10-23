import math
from collections import deque
from statistics import mean

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def harmonic_mean(data):
    if len(data) == 0:
        return 0
    return len(data) / sum(1/x for x in data if x != 0)

# Simulated daily returns for a portfolio
portfolio_returns = [0.02, -0.01, 0.03, 0.05, -0.02, 0.04, -0.03, 0.06, 0.01, -0.04, 0.02, 0.03, -0.01, 0.05, 0.04]

# Step 1: Compute mean and standard deviation
return_mean = sum(portfolio_returns) / len(portfolio_returns)
return_std = (sum((x - return_mean) ** 2 for x in portfolio_returns) / len(portfolio_returns)) ** 0.5

# Step 2: Filter outliers (z-score > 2.0 or < -2.0)
filtered_returns = [r for r in portfolio_returns if abs((r - return_mean) / return_std) <= 2.0]

# Step 3: Compute EWMA with decay factor 0.9
ewma_values = []
if filtered_returns:
    ewma = filtered_returns[0]
    for ret in filtered_returns:
        ewma = 0.9 * ewma + 0.1 * ret
        ewma_values.append(ewma)

# Step 4: Collect prime-indexed returns from original list
prime_indexed_returns = [portfolio_returns[i] for i in range(len(portfolio_returns)) if is_prime(i)]

# Step 5: Compute harmonic mean of prime-indexed returns
h_mean = harmonic_mean(prime_indexed_returns)

# Step 6: Apply correction factor to latest EWMA value
latest_ewma = ewma_values[-1] if ewma_values else 0
adjusted_risk = latest_ewma * (1 + h_mean)

print(f"Result: {adjusted_risk}")