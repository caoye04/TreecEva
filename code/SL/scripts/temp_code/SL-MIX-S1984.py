import math
from contextlib import contextmanager

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

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

@contextmanager
def observation_window(duration):
    print(f"Starting observation for {duration} seconds")
    try:
        yield duration
    finally:
        print(f"Observation completed for {duration} seconds")

# Signal processing parameters
frequencies = [12, 18, 24, 30]
prime_factors = []

for freq in frequencies:
    temp = []
    for i in range(2, freq + 1):
        if freq % i == 0 and is_prime(i):
            temp.append(i)
    prime_factors.append(temp)

# Calculate LCM of all frequencies
lcm_value = frequencies[0]
for i in range(1, len(frequencies)):
    lcm_value = lcm(lcm_value, frequencies[i])

# Context manager usage
with observation_window(lcm_value) as obs_duration:
    sync_base = sum(map(lambda x: sum(x), prime_factors))
    sync_metric = sync_base * (obs_duration // 6)

print(f"Result: {sync_metric}")