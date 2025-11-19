import math
from collections import defaultdict

def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

security_tokens = [24, 35, 49, 77]
factor_counts = defaultdict(int)

for token in security_tokens:
    factors = prime_factors(token)
    for f in factors:
        factor_counts[f] += 1

weight_function = lambda p, count: int(math.log(p) * count * pow(p, count % 3))
total_weight = sum(weight_function(prime, count) for prime, count in factor_counts.items())

modulus = 10007
base_exponent = sum(factor_counts.values())
derived_key = (total_weight * pow(3, base_exponent, modulus)) % modulus

print(f"Result: {derived_key}")