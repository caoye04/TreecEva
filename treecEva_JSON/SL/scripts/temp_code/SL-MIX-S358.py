import math

def transform_data(data):
    transformed = []
    for i, item in enumerate(data):
        if isinstance(item, int):
            transformed.append(math.factorial(item % 7))
        elif isinstance(item, str):
            transformed.append(len(item) ** 2)
        else:
            transformed.append(0)
    return transformed

def process_nested(nested_dict):
    results = {}
    for key, value in nested_dict.items():
        if isinstance(value, list):
            results[key] = sum(transform_data(value))
        elif isinstance(value, dict):
            sub_results = process_nested(value)
            results[key] = sum(sub_results.values())
        else:
            results[key] = value * 3
    return results

data_structure = {
    'level1_a': [4, 'hello', 12, 'world!'],
    'level1_b': {
        'level2_a': [3, 'test', 8],
        'level2_b': [1, 2, 'longerstring']
    },
    'level1_c': 7
}

processed = process_nested(data_structure)
aggregated = sum(processed.values())

# Perform bit shifting and masking operations
shifted = (aggregated << 2) & 0xFF
masked = shifted ^ 0xAA

# Apply trigonometric transformation
angle_rad = masked * (math.pi / 180)
trig_result = int(math.sin(angle_rad) * 1000)

# Final adjustment using logarithmic scaling
if trig_result > 0:
    final_result = int(math.log(trig_result) * 100)
else:
    final_result = -1

print(f'Result: {final_result}')