import hashlib
import itertools

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def custom_hash(s, mod=1000000007):
    hash_val = 0
    for i, char in enumerate(s):
        hash_val = (hash_val + ord(char) * pow(31, i, mod)) % mod
    return hash_val

dataset = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
hash_values = []
collision_metric = 0

for word in dataset:
    pf_sum = sum(prime_factors(len(word)))
    modified_word = word[::-1] + str(pf_sum)
    hash_val = custom_hash(modified_word)
    hash_values.append(hash_val)

unique_hashes = set()
for h in hash_values:
    if h in unique_hashes:
        collision_metric += 1
    else:
        unique_hashes.add(h)

# Additional processing with itertools
permutations = list(itertools.permutations(hash_values, 2))
for a, b in permutations:
    if a % 100 == b % 100:
        collision_metric += 1

print(f"Result: {collision_metric}")