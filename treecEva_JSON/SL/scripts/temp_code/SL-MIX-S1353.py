from math import gcd
from functools import reduce

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Prime sieve using lambda and filter
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
primes_under_50 = list(filter(is_prime, range(2, 50)))

# Generate composites as product of consecutive primes
composite_sequence = [primes_under_50[i] * primes_under_50[i+1] for i in range(len(primes_under_50)-1)]

# Divide and conquer LCM calculation using recursive lambda
recursive_lcm = lambda lst: lst[0] if len(lst) == 1 else lcm(lst[0], recursive_lcm(lst[1:]))

# Key derivation process
key_fragments = {i: reduce(lambda x, y: x ^ y, composite_sequence[:i+2]) for i in range(0, len(composite_sequence)-1, 2)}

# Merge fragments using dictionary comprehension
merged_fragments = {k: v ^ recursive_lcm(composite_sequence[k:k+3]) for k, v in key_fragments.items()}

# Final key component derived through number theory operations
derived_key_component = sum(merged_fragments.values()) % (recursive_lcm([7, 11, 13, 17]) - max(merged_fragments.keys()))

print(f"Result: {derived_key_component}")