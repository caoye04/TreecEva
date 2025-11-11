import hashlib
from collections import defaultdict
from itertools import combinations

def fibonacci_token(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def combinatorial_hash(token_value):
    # Generate all 2-element combinations of token digits
    digits = [int(d) for d in str(token_value)]
    combo_sum = sum(sum(c) for c in combinations(digits, 2))
    return hashlib.md5(str(combo_sum).encode()).hexdigest()

token_seeds = [fibonacci_token(i) for i in range(1, 8)]
hash_chain = defaultdict(str)
final_hash_accumulator = 0

for i, seed in enumerate(token_seeds):
    hash_value = combinatorial_hash(seed)
    hash_chain[i] = hash_value
    # Convert hex to int and apply bitwise operations
    hex_as_int = int(hash_value[:8], 16)
    final_hash_accumulator ^= (hex_as_int >> i)

print(f"Result: {final_hash_accumulator}")