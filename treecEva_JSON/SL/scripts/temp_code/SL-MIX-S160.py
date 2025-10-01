import math

def complex_transform(data_dict):
    transformed = {}
    for key, value in data_dict.items():
        if isinstance(value, list):
            transformed[key] = [math.log(x) if x > 0 else 0 for x in value]
        elif isinstance(value, dict):
            transformed[key] = {k: v**2 for k, v in value.items()}
        else:
            transformed[key] = value
    return transformed

data = {
    'alpha': [math.e, math.e**2, -1],
    'beta': {'x': 3, 'y': 4, 'z': 5},
    'gamma': 42
}

transformed_data = complex_transform(data)

# Perform nested operations
nested_sum = sum([
    sum(transformed_data['alpha']),
    sum(transformed_data['beta'].values()),
    transformed_data['gamma']
])

# Bitwise and mathematical operations
bitwise_part = (int(nested_sum) & 0xFF) ^ 0xAA
math_part = math.sin(math.pi / 4) * 100

# Conditional assignment with multiple logical operations
conditional_value = math_part if (bitwise_part > 100) and not (nested_sum < 50) else nested_sum

# String manipulation and encoding
encoded_string = ''.join([chr(ord(c) ^ 0x55) for c in 'Secret'])
encoded_sum = sum(ord(c) for c in encoded_string)

# Final calculation step
result_value = int((conditional_value * encoded_sum) % 1000) + (bitwise_part << 2)

print(f"Result: {result_value}")