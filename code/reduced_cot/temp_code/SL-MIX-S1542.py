import math

def xor_shift_cipher(data, key):
    return (data ^ key) >> 1

def modular_exp(base, exp, mod):
    return pow(base, exp, mod)

def entropy_pool_update(pool, new_data):
    return pool | new_data

def secure_hash_chain(seed, iterations):
    current = seed
    for _ in range(iterations):
        current = (current * 13 + 7) & 0xFFFF
    return current

# Initialize security parameters
prime_modulus = 65521
base_generator = 3
initial_entropy = frozenset([1, 3, 7, 15])

# Phase 1: Entropy accumulation
entropy_pool = initial_entropy
additional_entropy = frozenset([2, 6, 14, 30])
entropy_pool = entropy_pool_update(entropy_pool, additional_entropy)
pool_value = sum(entropy_pool)

# Phase 2: Key derivation
exponent_secret = int(math.log2(pool_value)) + 3
partial_key = modular_exp(base_generator, exponent_secret, prime_modulus)
shifted_key = partial_key << 2

# Phase 3: Session key generation
cipher_input = secure_hash_chain(shifted_key, 4)
session_key = xor_shift_cipher(cipher_input, 0x1F4A)

print(f"Result: {session_key}")