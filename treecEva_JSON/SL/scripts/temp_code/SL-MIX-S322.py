import math

def complex_transform(data):
    transformed = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            transformed.append(val ** 2)
        else:
            transformed.append(math.sqrt(abs(val)))
    return transformed

def nested_operation(matrix):
    flattened = [item for sublist in matrix for item in sublist]
    processed = complex_transform(flattened)
    return sum(processed) / len(processed)

def bitwise_shuffle(value, shifts):
    result = value
    for i, shift in enumerate(shifts):
        if i % 2 == 0:
            result ^= (result << shift) & 0xFFFFFFFF
        else:
            result ^= (result >> shift)
        result &= 0xFFFFFFFF
    return result

data_structure = {
    'matrix_a': [[1, -4, 9], [16, -25, 36]],
    'matrix_b': [[49, -64, 81], [100, -121, 144]],
    'bitwise_keys': [3, 2, 5, 1],
    'scalar_base': 2023
}

# Intermediate processing steps
avg_a = nested_operation(data_structure['matrix_a'])
avg_b = nested_operation(data_structure['matrix_b'])

# Bitwise manipulation
shuffled_base = bitwise_shuffle(data_structure['scalar_base'], data_structure['bitwise_keys'])

# Mathematical combination
intermediate = (avg_a * avg_b) + math.log(shuffled_base)

# String operation influence
key_string = "COMPLEX_EVALUATION"
char_sum = sum(ord(c) for c in key_string)
char_factor = char_sum % 10

# Final calculation step
result = int(intermediate) ^ char_factor

print(f"Result: {result}")