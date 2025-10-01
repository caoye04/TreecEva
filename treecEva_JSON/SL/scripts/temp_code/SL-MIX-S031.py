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

def recursive_reduce(value, depth=3):
    if depth == 0:
        return value
    else:
        return recursive_reduce(value / 2.0, depth - 1)

# Initialize complex nested data structure
base_data = [
    [16, -9, 25],
    [4, -16, 36],
    [9, -25, 49]
]

# Perform multi-step transformations
step1 = nested_operation(base_data)
step2 = recursive_reduce(step1)
intermediate = int(step2) * 7

# String manipulation and encoding
secret = "HELLO"
encoded = ''.join([str(ord(c) - 64) for c in secret])
key = int(encoded)

# Bitwise operations
mask = 0xF0
masked_key = key & mask
shifted = masked_key >> 2

# Mathematical operations with multiple steps
angle = math.pi / 4
trig_result = math.sin(angle) * math.cos(angle)
scaled_trig = round(trig_result * 1000)

# Final calculation step
result = (intermediate ^ shifted) + scaled_trig
print(f"Result: {result}")