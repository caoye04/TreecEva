from functools import reduce
from itertools import combinations

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    n += 1
    while not is_prime(n):
        n += 1
    return n

# Initialize protocol parameters
protocol_seeds = [23, 89, 157]
collision_signature = 0
hash_accumulator = []

# Process each seed through prime-based transformations
for idx, seed in enumerate(protocol_seeds):
    prime_chain = []
    current = seed
    
    # Build a chain of 3 consecutive primes starting from seed
    for _ in range(3):
        prime_chain.append(current)
        current = next_prime(current)
    
    # Apply lambda transformation for hash generation
    transform = lambda x: (x * 17 + 23) % 1000
    transformed_chain = list(map(transform, prime_chain))
    
    # Compute pairwise products and accumulate
    pair_products = [a * b for a, b in combinations(transformed_chain, 2)]
    hash_segment = reduce(lambda acc, val: acc ^ val, pair_products, 0)
    hash_accumulator.append(hash_segment)
    
    # Update collision signature with XOR of current segment and its index
    collision_signature ^= (hash_segment << idx)

# Final adjustment using string hashing
team_identifier = "CRYPTO_ANALYSIS_2023"
char_sum = sum(ord(c) for c in team_identifier)
collision_signature = (collision_signature + char_sum) % 997

print(f"Result: {collision_signature}")