import math

def process_nested_data(data):
    total = 0
    for key, values in data.items():
        if isinstance(values, list):
            for i, val in enumerate(values):
                if i % 2 == 0:
                    total += val ** 2
                else:
                    total -= math.sqrt(abs(val))
        elif isinstance(values, dict):
            for sub_key, sub_val in values.items():
                total += len(sub_key) * sub_val
    return int(total)

def transform_string(s):
    parts = s.split('_')
    transformed = []
    for part in parts:
        if len(part) > 3:
            transformed.append(part[::-1])
        else:
            transformed.append(part.upper())
    return ''.join(transformed)

data_structure = {
    'alpha': [4, -9, 2, -16, 5],
    'beta': {'gamma': 7, 'delta_epsilon': 3},
    'theta': [1, 4, 9, -25]
}

string_input = "hello_world_example_test"

numeric_result = process_nested_data(data_structure)
transformed_str = transform_string(string_input)
char_sum = sum(ord(c) for c in transformed_str)

# Apply modulo to keep number manageable
intermediate_value = (numeric_result + char_sum) % 1000

# Final complex calculation involving bitwise and power operations
final_result = (intermediate_value << 2) ^ (intermediate_value >> 1)
final_result = final_result ** 0.5
final_result = int(final_result) + (final_result - int(final_result) >= 0.5)

print(f"Result: {final_result}")