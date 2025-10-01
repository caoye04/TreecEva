import math

def process_data(data):
    processed = []
    for key, values in data.items():
        temp = []
        for v in values:
            if isinstance(v, int) and v > 0:
                temp.append(math.log(v) * 2)
            elif isinstance(v, str):
                temp.append(len(v) ** 2)
            else:
                temp.append(0)
        processed.append((key, sum(temp)))
    return dict(processed)

def transform_keys(d):
    return {k[::-1].upper(): v for k, v in d.items()}

# Main execution
nested_data = {
    'alpha': [1, 4, 9, 'hello', -3],
    'beta': [16, 'world', 25, None],
    'gamma': ['test', 36, 49, 0]
}

processed_dict = process_data(nested_data)
transformed_dict = transform_keys(processed_dict)

# Perform additional calculations
accumulated = 0
for key in sorted(transformed_dict.keys()):
    val = transformed_dict[key]
    if val > 10:
        accumulated += math.sqrt(val)
    else:
        accumulated += val * 2

final_result = int(accumulated) ^ 0xF0  # XOR with 240
print(f'Result: {final_result}')