import math

def process_data(data):
    transformed = []
    for i, val in enumerate(data):
        if isinstance(val, int):
            transformed.append(math.factorial(val))
        elif isinstance(val, str):
            transformed.append(len(val) * 2)
        else:
            transformed.append(sum(val))
    return transformed

def calculate_checksum(values):
    checksum = 0
    for v in values:
        checksum ^= v
    return checksum

data_structure = [
    [2, 3],
    "hello",
    4,
    [1, 1, 1, 1, 1],
    "world!",
    3
]

processed = process_data(data_structure)
checksum = calculate_checksum(processed)

# Apply transformation based on checksum parity
if checksum % 2 == 0:
    adjusted = [x + 1 for x in processed]
else:
    adjusted = [x * 2 for x in processed]

# Nested dictionary creation and manipulation
nested_dict = {
    'level1': {
        'level2a': {
            'values': adjusted[:3]
        },
        'level2b': {
            'values': adjusted[3:]
        }
    }
}

total_sum = sum(nested_dict['level1']['level2a']['values']) + sum(nested_dict['level1']['level2b']['values'])

# Final computation involving exponentiation and modulus
final_result = (total_sum ** 2) % (checksum + 10)

print(f"Result: {final_result}")