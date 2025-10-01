import math

def complex_transform(data):
    transformed = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            transformed.append(val ** 2)
        else:
            transformed.append(math.sqrt(abs(val)))
    return transformed

def aggregate_stats(numbers):
    product = 1
    for num in numbers:
        product *= num if num != 0 else 1
    return {
        'sum': sum(numbers),
        'product': product,
        'mean': sum(numbers) / len(numbers) if numbers else 0
    }

# Initialize complex nested data structure
matrix = [
    [3, -4, 5],
    [2, 0, -1],
    [7, 8, -9]
]

# Flatten and apply transformations
flat_list = [item for sublist in matrix for item in sublist]
transformed_data = complex_transform(flat_list)

# Perform statistical aggregations
stats = aggregate_stats(transformed_data)

# Nested dictionary with computed values
computations = {
    'layer1': {
        'a': stats['sum'] * 2,
        'b': stats['product'] // 1000
    },
    'layer2': {
        'x': math.floor(stats['mean']),
        'y': (stats['sum'] + stats['product']) % 100
    }
}

# Bitwise and mathematical operations
bitwise_result = (computations['layer1']['a'] & 0xFF) ^ computations['layer2']['x']
trig_operation = math.sin(math.radians(30)) * computations['layer1']['b']

# String manipulation and encoding
encoded = ''.join(chr(ord(c) ^ 42) for c in str(bitwise_result))
value_from_string = sum(ord(c) for c in encoded)

# Final calculation step
result = int((value_from_string * trig_operation) // computations['layer2']['y'])

print(f'Result: {result}')