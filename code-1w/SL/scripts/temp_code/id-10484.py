def process_char(c):
    if c.islower():
        return ord(c) - ord('a') + 1
    elif c.isupper():
        return ord(c) - ord('A') + 1
    else:
        return 0

input_string = "PyThon2023"

# Convert each character to positional value and apply transformation
raw_values = [process_char(c) for c in input_string]

# Apply bitwise XOR with index position to obfuscate pattern
transformed = [val ^ i for i, val in enumerate(raw_values)]

# Filter out zero values (non-alphabetic)
cleaned = [x for x in transformed if x != 0]

# Compute weighted sum using alternating signs
weighted = sum((-1) ** i * v for i, v in enumerate(cleaned))

# Finalize checksum using absolute value and modulo
checksum = abs(weighted) % 97

Result: checksum