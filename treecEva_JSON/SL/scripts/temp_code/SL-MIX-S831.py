from functools import reduce

def mod_exp(base, exp, mod):
    return pow(base, exp, mod)

def generate_keys():
    key_sequence = [7]
    for i in range(1, 6):
        prev_key = key_sequence[i-1]
        # Bitwise operations
        shifted = (prev_key << 2) & 0xFF
        xor_result = shifted ^ 0x5A
        # Modular exponentiation with dynamic programming approach
        exp_val = reduce(lambda x, y: x * y, [j for j in range(1, i+1)], 1) if i > 0 else 1
        new_key = mod_exp(xor_result, exp_val, 251)
        key_sequence.append(new_key)
    return key_sequence

# Generate the key sequence
keys = generate_keys()

# Apply final transformation using backtracking concept
final_transform = keys[5] ^ (keys[4] & 0xF0)
keys.append(final_transform)

print(f"Result: {keys[5]}")