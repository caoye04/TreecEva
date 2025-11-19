from functools import reduce

# Security token for authentication
security_token = "SEC2023"

# Prime-based mask generation using lambda and list comprehension
primes_under_10 = [p for p in range(2, 11) if all(p % i != 0 for i in range(2, int(p**0.5)+1))]
generate_mask = lambda x, y: (x << 1) ^ y
mask_sequence = reduce(generate_mask, primes_under_10, 0)

# Token encoding with short-circuit and ternary logic
transformed_chars = []
for idx, char in enumerate(security_token):
    ascii_val = ord(char)
    # Apply conditional transformation based on character type
    modified = ascii_val + (idx & 3) if char.isalpha() else ascii_val ^ (idx | 2)
    # Short-circuit evaluation for boundary check
    adjusted = modified if (modified < 128 and modified > 31) else modified & 0x7F
    transformed_chars.append(adjusted)

# Final encoding step using map and custom function
encoder_func = lambda val: ((val ^ mask_sequence) + 42) & 0xFF
encoded_values = list(map(encoder_func, transformed_chars))

# String reconstruction and final output calculation
encoded_string = ''.join(chr(val) for val in encoded_values if val > 0)
encoded_output = sum(ord(c) * (i + 1) for i, c in enumerate(encoded_string))

print(f"Result: {encoded_output}")