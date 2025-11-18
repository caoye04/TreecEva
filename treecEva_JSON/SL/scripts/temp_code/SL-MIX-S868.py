import math
from itertools import combinations

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

# Generate primes up to 100
primes_list = [i for i in range(2, 101) if is_prime(i)]

# Greedy selection: pick first 5 primes that are 1 mod 4
mod_4_primes = []
for p in primes_list:
    if p % 4 == 1:
        mod_4_primes.append(p)
        if len(mod_4_primes) == 5:
            break

# Calculate base using combination sum
combos = list(combinations(mod_4_primes[:3], 2))
base_sum = sum([math.comb(a, b) if a > b else math.comb(b, a) for a, b in combos])

# Modular exponentiation
exp_result = pow(base_sum, 3, 997)

# Derived key calculation
factorial_digits = [math.factorial(int(d)) for d in str(exp_result)]
derived_key = sum(factorial_digits) % 1000

print(f"Result: {derived_key}")