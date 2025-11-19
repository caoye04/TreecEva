import itertools
from contextlib import contextmanager

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

@contextmanager
def track_max_memory():
    max_mem = [0]
    try:
        yield max_mem
    finally:
        pass

def sieve_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = False
    return {i for i, is_prime in enumerate(sieve) if is_prime}

with track_max_memory() as mem_tracker:
    prime_set_a = sieve_primes(100)
    prime_set_b = sieve_primes(150)
    common_primes = prime_set_a & prime_set_b
    unique_primes = prime_set_a ^ prime_set_b
    
    # Calculate LCM of first three common primes
    sorted_common = sorted(list(common_primes))[:3]
    current_lcm = sorted_common[0]
    for prime in sorted_common[1:]:
        current_lcm = lcm(current_lcm, prime)
    
    # Count primes in arithmetic progression: 5k + 2
    progression_primes = {p for p in unique_primes if p % 5 == 2}
    
    # Find primes that are also Fibonacci numbers using generator
    def fib_generator():
        a, b = 1, 1
        while True:
            yield a
            a, b = b, a + b
    
    fib_nums = set(itertools.takewhile(lambda x: x <= 150, fib_generator()))
    fib_primes = prime_set_b & fib_nums
    
    # Calculate final count
    max_prime_count = len(progression_primes) * len(fib_primes) + current_lcm
    
print(f"Result: {max_prime_count}")