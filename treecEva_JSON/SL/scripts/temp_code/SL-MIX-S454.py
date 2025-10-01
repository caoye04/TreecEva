import math

def transform_data(data_dict):
    transformed = []
    for key, value in data_dict.items():
        if isinstance(value, list):
            sub_sum = sum(value)
            transformed.append((key, sub_sum))
        elif isinstance(value, dict):
            sub_product = 1
            for v in value.values():
                sub_product *= v
            transformed.append((key, sub_product))
        else:
            transformed.append((key, value))
    return transformed

def calculate_checksum(pairs):
    checksum = 0
    for key, value in pairs:
        key_hash = sum(ord(c) for c in key)
        checksum += key_hash * value
    return checksum

data = {
    'alpha': [1, 2, 3, 4],
    'beta': {'x': 2, 'y': 3},
    'gamma': 10,
    'delta': [5, -2, 7],
    'epsilon': {'m': 4, 'n': 5, 'o': 2}
}

transformed_data = transform_data(data)
checksum = calculate_checksum(transformed_data)

# Apply modular arithmetic and trigonometric transformation
mod_value = checksum % 100
trig_value = math.sin(math.radians(mod_value))

# Nested list comprehension with conditional logic
nested_comp = [
    (i * trig_value) + math.log(j + 1)
    for i in range(1, 6)
    for j in range(i, i + 3)
    if (i + j) % 2 == 0
]

# Bitwise operations and exponentiation
bitwise_result = 0
for idx, val in enumerate(nested_comp):
    bitwise_result ^= int(val * 100) << (idx % 4)

exp_result = bitwise_result ** 0.5

# Final calculation step
result_value = int(exp_result) % 1000

print(f"Result: {result_value}")