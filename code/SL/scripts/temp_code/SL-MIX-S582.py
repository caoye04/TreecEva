from functools import reduce
import hashlib

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Protocol initialization
participants = {'Alice', 'Bob', 'Charlie'}
shared_secrets = frozenset(['secret1', 'secret2', 'secret3'])
prime_indices = [2, 3, 5, 7, 11]

# Generate base values from prime-indexed Fibonacci numbers
fib_values = [fibonacci(p) for p in prime_indices]
modulus_base = reduce(lcm, fib_values[:3])

# Hash shared secrets and combine
hashes = [int(hashlib.sha256(s.encode()).hexdigest(), 16) for s in shared_secrets]
combined_hash = sum(hashes) % modulus_base

# Compute session key using remaining Fibonacci values and transformations
transformed_values = [((f % combined_hash) if combined_hash != 0 else 1) for f in fib_values[3:]]
string_transform = ''.join(chr((ord(c) + 13) % 256) for c in "crypto")
hashed_transform = int(hashlib.md5(string_transform.encode()).hexdigest(), 16)

# Final computation
if combined_hash > 0:
    session_key = (reduce(lambda x, y: (x * y) % combined_hash, transformed_values, 1) + hashed_transform) % modulus_base
else:
    session_key = hashed_transform % 1000000

print(f"Result: {session_key}")