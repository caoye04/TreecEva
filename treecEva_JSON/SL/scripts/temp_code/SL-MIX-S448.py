import math

def process_nested_data(data):
    result = 0
    for key, value in data.items():
        if isinstance(value, dict):
            result += process_nested_data(value)
        elif isinstance(value, list):
            for i, item in enumerate(value):
                if isinstance(item, (int, float)):
                    result += item * (i + 1)
                elif isinstance(item, str):
                    result += len(item) * (key.count('a') + 1)
        elif isinstance(value, (int, float)):
            result += value * key.count('e')
    return result

def complex_calculation(x, y, z):
    a = math.pow(x, 2) + math.sqrt(abs(y))
    b = math.log(abs(z) + 1) * math.sin(a)
    c = (a + b) / (math.cos(b) + 1)
    d = int(c) ^ int(a)  # XOR operation
    return d

data_structure = {
    'level1a': {
        'level2a': [10, 'hello', 3.5],
        'level2b': 7,
        'level2c': {
            'level3a': [20, 'world', 4.2],
            'level3b': 'nested'
        }
    },
    'level1b': [5, 'test', 2.8, 'example'],
    'level1c': {
        'level2a': 15,
        'level2b': [1, 2, 3, 'deep']
    }
}

# Process the nested data structure
processed_value = process_nested_data(data_structure)

# Perform complex calculation with the processed value
x = processed_value % 100
y = processed_value / 7
z = processed_value - 100

# Apply bit shifting
shifted_x = x << 2  # Left shift by 2
shifted_y = y >> 1  # Right shift by 1 (as integer)

# Perform complex calculation with shifted values
intermediate_result = complex_calculation(shifted_x, shifted_y, z)

# Apply additional transformations
final_result = ((intermediate_result & 0xFF) + 100) % 97  # Bitwise AND with 255, add 100, then modulo 97

print(f"Result: {final_result}")