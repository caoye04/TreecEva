import math

def process_nested_data(data):
    result = 0
    for key, value in data.items():
        if isinstance(value, dict):
            inner_result = 0
            for inner_key, inner_value in value.items():
                if isinstance(inner_value, list):
                    temp_sum = sum(inner_value)
                    inner_result += temp_sum * len(inner_value)
                elif isinstance(inner_value, str):
                    inner_result += len(inner_value) ** 2
                else:
                    inner_result += inner_value
            result += inner_result
        elif isinstance(value, list):
            for i, item in enumerate(value):
                if i % 2 == 0:
                    result += item
                else:
                    result -= item
        else:
            result += value
    return result

def complex_computation(x, y, z):
    a = math.pow(x, 2) + math.sqrt(y)
    b = math.log(z) if z > 0 else 0
    c = math.sin(a) + math.cos(b)
    d = int(c * 1000) & 0xFF
    return d

data_structure = {
    'level1': {
        'level2a': [1, 2, 3, 4],
        'level2b': 'hello',
        'level2c': {
            'level3a': [5, 6],
            'level3b': 'world',
            'level3c': 42
        }
    },
    'array1': [10, 5, 8, 3, 7],
    'value1': 100,
    'value2': 200
}

# Process the nested data structure
processed_value = process_nested_data(data_structure)

# Perform complex mathematical computation
computed_value = complex_computation(processed_value, 144, 1000)

# Bitwise operations
bitwise_result = (computed_value << 2) ^ 0xAA

# Final calculation combining all results
final_result = (processed_value + computed_value + bitwise_result) % 97

print(f'Result: {final_result}')