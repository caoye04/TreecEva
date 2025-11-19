import math
from functools import reduce

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

numbers = [17, 24, 29, 35, 41, 48, 53]
filtered_primes = list(filter(is_prime, numbers))
log_values = [int(math.log2(p)) for p in filtered_primes]
crypto_key = reduce(lambda x, y: x ^ y, log_values)
print(f"Result: {crypto_key}")