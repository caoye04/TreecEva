from math import gcd
from functools import reduce

def euler_totient(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def primitive_root_check(g, p):
    if gcd(g, p) != 1:
        return False
    phi = euler_totient(p)
    factors = set()
    n = phi
    d = 2
    while d * d <= n:
        if n % d == 0:
            factors.add(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        factors.add(n)
    for factor in factors:
        if pow(g, phi // factor, p) == 1:
            return False
    return True

primes_under_20 = [2, 3, 5, 7, 11, 13, 17, 19]
primitive_roots_map = {}
for p in primes_under_20[2:]:
    roots = []
    for g in range(2, p):
        if primitive_root_check(g, p):
            roots.append(g)
    if roots:
        primitive_roots_map[p] = roots[0]

mod_sequence = []
for p, g in primitive_roots_map.items():
    mod_val = pow(g, euler_totient(p), p)
    mod_sequence.append(mod_val)

unique_mods = frozenset(mod_sequence)
cryptographic_key = reduce(lambda x, y: (x * y) % 1000, unique_mods, 1)
print(f"Result: {cryptographic_key}")