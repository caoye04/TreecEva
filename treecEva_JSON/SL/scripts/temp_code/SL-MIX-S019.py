import math

def process_nested_data(data):
    total = 0
    for key, value in data.items():
        if isinstance(value, list):
            for i, item in enumerate(value):
                if isinstance(item, dict) and 'value' in item:
                    total += item['value'] * (i + 1)
        elif isinstance(value, dict):
            for sub_key, sub_value in value.items():
                if isinstance(sub_value, str):
                    total += len(sub_value)
    return total

data_structure = {
    'alpha': [
        {'value': 5}, 
        {'value': 10}, 
        {'value': 15}
    ],
    'beta': {
        'gamma': 'hello',
        'delta': 'world!'
    },
    'epsilon': [
        {'name': 'test'},
        {'value': 7},
        {'value': 3, 'extra': True}
    ]
}

# Initial computation
base_value = process_nested_data(data_structure)

# Mathematical transformations
x = base_value / 2.0
y = math.sqrt(x) * 4
z = math.log(y) if y > 0 else 0

# Bitwise operations
a = int(z) & 15  # Bitwise AND with 15 (0b1111)
b = a << 2       # Left shift by 2
c = b ^ 42       # XOR with 42

# String manipulations based on computations
hex_string = hex(c)[2:]  # Remove '0x' prefix
reversed_hex = hex_string[::-1]
char_sum = sum(ord(char) for char in reversed_hex)

# Final complex calculation
final_result = ((c + char_sum) * 3 - 100) // 7
print(f'Result: {final_result}')