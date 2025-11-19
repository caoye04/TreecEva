import itertools

def rotating_xor_key(data, keys):
    return [datum ^ keys[i % len(keys)] for i, datum in enumerate(data)]

def ascii_transform(token):
    return [ord(c) for c in token]

# Cryptographic tokens
mystery_tokens = ['py', 'thon', 'code', 'eval']

# Transformation keys
xor_keys = [0x5A, 0x3C, 0xF1]

# Process tokens through transformation pipeline
transformed_sequences = list(map(lambda t: rotating_xor_key(ascii_transform(t), xor_keys), mystery_tokens))

# Flatten all transformed sequences
flattened_values = list(itertools.chain.from_iterable(transformed_sequences))

# Validation function with short-circuit evaluation
valid_token_count = 0
for val in flattened_values:
    # Complex condition: value must be > 50 AND (value has even parity OR value is divisible by 3)
    if val > 50 and (bin(val).count('1') % 2 == 0 or val % 3 == 0):
        valid_token_count += 1

print(f"Result: {valid_token_count}")