from collections import deque
from math import gcd

def get_primes_up_to(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

# Initialize cryptographic components
prime_cache = get_primes_up_to(100)
transformation_stack = deque()
seed_value = 42

# Stage 1: Prime factorization and GCD chain
factors = []
temp_seed = seed_value
for p in prime_cache:
    while temp_seed % p == 0:
        factors.append(p)
        temp_seed //= p
    if temp_seed == 1:
        break

# Stage 2: Build transformation stack with LCM operations
for i in range(len(factors)):
    if i == 0:
        transformation_stack.append(factors[i])
    else:
        prev = transformation_stack[-1]
        current_lcm = (prev * factors[i]) // gcd(prev, factors[i])
        transformation_stack.append(current_lcm)

# Stage 3: Apply stack-based transformations with lambda operations
transform_ops = [
    lambda x: x ^ 0xF0F0,
    lambda x: (x << 2) & 0xFFFF,
    lambda x: x | 0x0F00
]

processed_values = []
while transformation_stack:
    val = transformation_stack.pop()
    for op in transform_ops:
        val = op(val)
    processed_values.append(val)

# Stage 4: Final key derivation using dictionary comprehension and merging
derived_components = {i: val for i, val in enumerate(processed_values) if val % 3 == 0}
additional_components = {i+len(derived_components): val for i, val in enumerate(processed_values) if val % 5 == 0}
merged_components = {**derived_components, **additional_components}

# Calculate final derived key
derived_key = sum(merged_components.values()) & 0xFFFF
print(f"Result: {derived_key}")