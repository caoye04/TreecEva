import math

def complex_transform(data_dict):
    result = 0
    for key, value in data_dict.items():
        if isinstance(value, list):
            temp_sum = sum(value)
            if temp_sum % 2 == 0:
                result += temp_sum >> 2  # Right shift by 2 (equivalent to dividing by 4)
            else:
                result += (temp_sum ** 2) & 0xFF  # Square and mask to lower 8 bits
        elif isinstance(value, str):
            ascii_sum = sum(ord(c) for c in value)
            result += ascii_sum % 17
        elif isinstance(value, dict):
            nested_result = complex_transform(value)
            result += nested_result ^ 0x55  # XOR with 0x55
    return result

data = {
    'alpha': [3, 7, 2, 9],
    'beta': {
        'gamma': [1, 4, 6],
        'delta': 'hello',
        'epsilon': {
            'zeta': [8, 5],
            'eta': 'world'
        }
    },
    'theta': 'python',
    'iota': [10, 15, 20]
}

intermediate_value = complex_transform(data)

# Apply additional transformations
if intermediate_value > 100:
    final_result = (intermediate_value * 3) % 256
else:
    final_result = (intermediate_value ** 2) % 256

# Final adjustment
final_result = final_result ^ ((final_result << 1) & 0xFF)

print(f'Result: {final_result}')