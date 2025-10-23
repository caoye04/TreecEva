import math
from functools import wraps

def precompute_values(func):
    cache = {}
    @wraps(func)
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

@precompute_values
def modular_power(base, exponent, modulus):
    return pow(base, exponent, modulus)

def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = False
    return [i for i, prime in enumerate(sieve) if prime]

primes = sieve_of_eratosthenes(30)
prime_powers = {p: modular_power(p, 3, 100) for p in primes}

# Select primes at indices that are Fibonacci numbers (0, 1, 1, 2, 3, 5, 8, 13...)
fib_indices = [0, 1, 2, 3, 5, 8, 13]
selected_primes = [primes[i] for i in fib_indices if i < len(primes)]

# Calculate the product of selected primes
product = 1
for p in selected_primes:
    product *= p

# Compute cryptographic key using GCD and LCM
gcd_value = math.gcd(product, 1001)  # 1001 = 7*11*13
lcm_value = (product * 1001) // gcd_value

cryptographic_key = (lcm_value % 97) + int(math.log2(len(primes)))
print(f"Result: {cryptographic_key}")