from functools import reduce
from math import gcd

def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0:2] = [False, False]
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]

mod_exp = lambda base, exp, mod: pow(base, exp, mod)
gcd_list = lambda lst: reduce(gcd, lst)
lcm = lambda a, b: abs(a * b) // gcd(a, b) if a and b else 0
lcm_list = lambda lst: reduce(lcm, lst, 1)

prime_numbers = sieve_of_eratosthenes(30)
selected_primes = list(filter(lambda p: p > 5 and p < 25, prime_numbers))
exponents = [2, 3, 5]
modulus = 19

modular_results = [mod_exp(p, e, modulus) for p, e in zip(selected_primes, exponents)]
hash_components = list(map(lambda x: x ^ 0xF, modular_results))
combined_hash = reduce(lambda x, y: x ^ y, hash_components, 0)
cryptographic_signature = combined_hash + gcd_list(modular_results) * lcm_list(exponents)
print(f"Result: {cryptographic_signature}")