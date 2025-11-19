from math import gcd
from functools import reduce

def fibo_transform(n):
    if n <= 1:
        return (n + n) % 17
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, (a + b) % 17
    return (b + n) % 17

# Calculate signal strengths using map and lambda
positions = range(1, 16)
signal_strengths = list(map(lambda k: gcd(k, fibo_transform(k)), positions))

# Get distinct values using set
unique_signals = set(signal_strengths)

# Sum using reduce
space_signal_sum = reduce(lambda x, y: x + y, unique_signals, 0)

print(f"Result: {space_signal_sum}")