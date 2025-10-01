import math

def complex_transform(data):
    result = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            result.append(val ** 2)
        else:
            result.append(math.sqrt(abs(val)))
    return result

def nested_operation(container):
    total = 0
    for key, value in container.items():
        if isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    for k, v in item.items():
                        total += v if isinstance(v, (int, float)) else 0
                else:
                    total += item if isinstance(item, (int, float)) else 0
        elif isinstance(value, dict):
            for k, v in value.items():
                total += v if isinstance(v, (int, float)) else 0
    return total

# Initialize data structures
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

nested_dict = {
    'a': [10, {'inner': 20}],
    'b': {'x': 30, 'y': [40, 50]},
    'c': 60
}

# Perform transformations
flattened = [item for sublist in matrix for item in sublist]
transformed = complex_transform(flattened)
aggregated = sum(transformed)

# Bitwise operations
bitwise_result = (aggregated & 0xFF) | ((aggregated >> 4) ^ 0xF)

# String manipulations
encoded = ''.join([chr((ord(c) + 5) % 128) for c in str(aggregated)])
char_sum = sum(ord(c) for c in encoded)

# Mathematical operations
log_val = math.log(abs(char_sum))
sin_val = math.sin(log_val)
cos_val = math.cos(log_val)
trig_result = sin_val * cos_val * 1000

# Nested structure operations
nested_sum = nested_operation(nested_dict)

# Final calculation
final_result = int((bitwise_result * trig_result + nested_sum) % 1000000)

print(f"Result: {final_result}")