segments_active = {1, 2, 4, 7}
segment_base_map = {1: 3, 2: 5, 4: 7, 7: 11}
modulus = 13

# Map segments to base values and apply modular exponentiation with lambda
mapped_values = [segment_base_map[s] for s in segments_active]
mod_exp = lambda base, exp, mod: (base ** exp) % mod
encrypted_parts = [mod_exp(base, 2, modulus) for base in mapped_values]

# Combine encrypted parts using modular arithmetic
encrypted_value = sum(encrypted_parts) % modulus
print(f'Result: {encrypted_value}')