import math

def process_nested_data(data_structure):
    result = 0
    for key, value in data_structure.items():
        if isinstance(value, dict):
            sub_result = process_nested_data(value)
            result += sub_result * len(key)
        elif isinstance(value, list):
            for i, item in enumerate(value):
                if isinstance(item, (int, float)):
                    result += item * (i + 1) * (-1 if i % 2 == 1 else 1)
                elif isinstance(item, str):
                    result += len(item) * hash(key) % 100
        elif isinstance(value, (int, float)):
            result += value if value > 0 else abs(value) ** 1.5
    return result

data = {
    'level1': {
        'level2a': [10, -5, 3.14, 'hello', 42],
        'level2b': {
            'level3': [math.sqrt(16), -3, 2**3, 'world', 7],
            'value': -8
        },
        'list_data': [1, [2, 3], {'nested': [4, 5, 6]}]
    },
    'numbers': [math.log(math.e), math.cos(0), math.sin(math.pi/2)],
    'mixed': {
        'a': 100,
        'b': [-1, -2, -3],
        'c': 'test_string'
    }
}

# Process the data structure
intermediate_result = process_nested_data(data)

# Perform additional transformations
transformed_value = (intermediate_result ** 0.5) * math.log10(abs(intermediate_result) + 1)

# Apply bit operations
bit_adjusted = int(transformed_value) & 0xFF
bit_shifted = bit_adjusted >> 2

# Final calculation sequence
final_result = bit_shifted ^ 0x3C
final_result = final_result * 3 - 7
final_result = final_result % 100 + 15

print(f"Result: {final_result}")