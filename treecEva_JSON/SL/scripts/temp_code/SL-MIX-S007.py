import math

def complex_transform(data_list):
    transformed = []
    for item in data_list:
        if isinstance(item, str):
            transformed.append(len(item) * 2)
        elif isinstance(item, int):
            transformed.append(item ^ 0xF)  # XOR with 15
        elif isinstance(item, float):
            transformed.append(int(math.floor(item * 3.14)))
        else:
            transformed.append(0)
    return transformed

def nested_operation(container):
    total = 0
    for key, value in container.items():
        if isinstance(value, list):
            for i, elem in enumerate(value):
                if i % 2 == 0:
                    total += elem << 1  # Left shift by 1 (multiply by 2)
                else:
                    total += elem >> 1  # Right shift by 1 (integer division by 2)
        elif isinstance(value, dict):
            sub_total = 0
            for sub_key, sub_value in value.items():
                sub_total += (sub_key * sub_value) % 7
            total += sub_total
    return total

# Initialize complex nested data structure
data = {
    'alpha': [3, 8, 5, 12],
    'beta': {
        2: 4,
        5: 9,
        3: 7
    },
    'gamma': ['hello', 3.14159, 42, 'world!']
}

# Perform nested operation on data
intermediate_value = nested_operation(data)

# Transform gamma values
transformed_gamma = complex_transform(data['gamma'])

# Calculate accumulator using transformed values and intermediate value
accumulator = 0
for i, val in enumerate(transformed_gamma):
    accumulator += (val * (i + 1)) ^ intermediate_value

# Apply mathematical transformation
accumulator = int(math.sqrt(accumulator) * 10) & 0xFF  # Mask to 8-bit

# Final calculation step
result = (accumulator << 2) + (intermediate_value % 5) - sum(transformed_gamma)

print(f'Result: {result}')