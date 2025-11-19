def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i*i, limit + 1, i):
                primes[j] = False
    return [i for i, is_prime in enumerate(primes) if is_prime]

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Signal processing pipeline
signal_blocks = [24, 36, 48, 60, 72]
prime_set = frozenset(sieve_of_eratosthenes(100))

block_transforms = {}
for idx, block_id in enumerate(signal_blocks):
    factors = {p for p in prime_set if block_id % p == 0}
    block_transforms[block_id] = {
        'prime_factors': factors,
        'factor_count': len(factors),
        'modular_signature': pow(block_id, 3, 17)
    }

# Compute aggregate metrics
unique_primes = set()
total_lcm = 1
for block_id, transform in block_transforms.items():
    unique_primes.update(transform['prime_factors'])
    total_lcm = lcm(total_lcm, block_id)

# Apply modular aggregation
aggregated_modulus = sum(
    transform['modular_signature'] 
    for transform in block_transforms.values()
) % 13

# Final signal strength calculation
processed_signal_strength = (
    len(unique_primes) * aggregated_modulus + 
    (total_lcm % 19)
) % 100

print(f"Result: {processed_signal_strength}")