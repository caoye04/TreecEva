def mod_exp(base, exp, mod):
    return pow(base, exp, mod)

def transform_char(c, shift):
    return chr((ord(c) - ord('a') + shift) % 26 + ord('a'))

# Character to number mapping using dictionary comprehension
char_map = {chr(ord('a') + i): i+1 for i in range(26)}
valid_keys = {k for k,v in char_map.items() if v % 3 != 0}
filtered_values = {char_map[k] for k in valid_keys}

# Apply modular arithmetic and transformations
transformed_chars = ''.join([transform_char(k, 5) for k in sorted(valid_keys)])
mod_results = [mod_exp(v, 3, 17) for v in sorted(filtered_values)]

# Store intermediate results in frozenset
intermediate_storage = frozenset(mod_results)

# Final cryptographic computation
cipher_sum = sum(intermediate_storage) * len(transformed_chars)
print(f"Result: {cipher_sum}")