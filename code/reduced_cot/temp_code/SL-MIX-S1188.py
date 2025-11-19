from functools import reduce
from itertools import permutations

def modular_power(base, exp, mod):
    return pow(base, exp, mod)

def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)

# Initialize cryptographic parameters
prime_modulus = 17
base_generator = 3
key_components = [2, 3, 5]

# Generate candidate keys using permutations
perm_set = set()
for p in permutations(key_components, 3):
    perm_value = reduce(lambda x, y: x * 10 + y, p)
    perm_set.add(perm_value)

# Apply modular exponentiation to each permutation
mod_exp_results = set(map(lambda x: modular_power(base_generator, x, prime_modulus), perm_set))

# Filter results to find valid keys (those that are quadratic residues mod 17)
valid_keys = set(filter(lambda x: pow(x, (prime_modulus-1)//2, prime_modulus) == 1, mod_exp_results))

# Count validated keys
validated_keys_count = len(valid_keys)

print(f"Result: {validated_keys_count}")