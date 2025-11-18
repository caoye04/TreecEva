import re

def modular_power(base, exp, mod):
    return pow(base, exp, mod)

def extract_pattern(sequence):
    pattern = r'(\d+)'
    matches = re.findall(pattern, ''.join(map(str, sequence)))
    return [int(m) for m in matches]

# Initialize cipher parameters
initial_vector = [2, 3, 5, 7, 11]
modulus = 10007
exponents = [i for i in range(1, len(initial_vector) + 1)]

cipher_sequence = [
    modular_power(iv, exp, modulus) 
    for iv, exp in zip(initial_vector, exponents)
]

# Apply pattern extraction and transformation
extracted_values = extract_pattern(cipher_sequence)
transformed_values = [
    (val * 3 + 7) % modulus 
    for val in extracted_values
]

# Divide and conquer approach to compute final key
def divide_conquer_key(values, mod):
    if len(values) == 1:
        return values[0] % mod
    mid = len(values) // 2
    left_key = divide_conquer_key(values[:mid], mod)
    right_key = divide_conquer_key(values[mid:], mod)
    return (left_key * right_key + 1) % mod

# Compute the final cipher key
cipher_key = divide_conquer_key(transformed_values, modulus)
print(f"Result: {cipher_key}")