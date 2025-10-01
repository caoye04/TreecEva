import math

def process_nested_data(data):
    total = 0
    for key, values in data.items():
        if isinstance(values, list):
            for i, val in enumerate(values):
                if i % 2 == 0:
                    total += val * math.log(i + 2)
                else:
                    total -= val // (i + 1)
        elif isinstance(values, dict):
            for sub_key, sub_val in values.items():
                total += sub_val ** (1/3) if sub_val > 0 else 0
    return int(total)

def transform_string(s):
    vowels = 'aeiouAEIOU'
    transformed = ''
    for char in s:
        if char in vowels:
            transformed += chr(ord(char) ^ 0x5C)
        else:
            transformed += char.upper()
    return transformed

data_structure = {
    'alpha': [7, 14, 21, 28],
    'beta': {'gamma': 64, 'delta': -27, 'epsilon': 125},
    'zeta': [3, 6, 9, 12, 15]
}

string_input = "MachineLearning"
transformed_str = transform_string(string_input)
char_sum = sum(ord(c) for c in transformed_str)

processed_value = process_nested_data(data_structure)
intermediate = (char_sum & processed_value) | (char_sum >> 2)

theta = 5
kappa = 3
lambda_val = 7

for i in range(1, kappa + 1):
    theta ^= (lambda_val << i) + i
    lambda_val += 2

final_computation = ((theta * intermediate) % 1000) + len(transformed_str)
final_result = final_computation if final_computation > 0 else abs(final_computation) + 100
print(f"Result: {final_result}")