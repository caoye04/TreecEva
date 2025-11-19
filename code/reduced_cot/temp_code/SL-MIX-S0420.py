from functools import reduce
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Stock performance returns over the last quarter (in percentages)
stock_returns = [2.5, -1.2, 3.8, 0, -0.5, 4.1, -2.3, 1.9, 3.3, -1.1]

# Step 1: Filter out non-positive returns and sort them
positive_returns = sorted(filter(lambda x: x > 0, stock_returns))

# Step 2: Apply a greedy selection of top performing stocks up to a limit
max_stocks = 5
selected_returns = []
for r in reversed(positive_returns):  # Greedy: pick from highest
    if len(selected_returns) < max_stocks and r > 1.0:
        selected_returns.append(r)

# Step 3: Compute mean and variance of selected returns
if selected_returns:
    mean_return = sum(selected_returns) / len(selected_returns)
    variance = sum((x - mean_return) ** 2 for x in selected_returns) / len(selected_returns)
else:
    mean_return, variance = 0, 0

# Step 4: Find prime numbers related to the length of selected returns
length_related_number = len(selected_returns) * 10
primes_in_range = [i for i in range(2, length_related_number + 1) if is_prime(i)]
prime_count = len(primes_in_range)

# Step 5: Calculate adjustment coefficient using number theory and statistics
if prime_count > 0 and variance > 0:
    lcm_value = reduce(lcm, primes_in_range[:min(3, len(primes_in_range))], 1)
    adjustment_coefficient = (mean_return * prime_count) / math.sqrt(variance) + lcm_value
else:
    adjustment_coefficient = 0

print(f"Result: {adjustment_coefficient}")