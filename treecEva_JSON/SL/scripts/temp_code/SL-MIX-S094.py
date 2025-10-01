import math

def process_data(data):
    processed = []
    for key, values in data.items():
        if isinstance(values, list):
            temp = []
            for v in values:
                if isinstance(v, (int, float)):
                    temp.append(math.sqrt(abs(v)) if v < 0 else v**2)
                elif isinstance(v, str):
                    temp.append(len(v) * 2)
            processed.append(sum(temp) // len(temp) if temp else 0)
        elif isinstance(values, dict):
            sub_sum = sum(process_data({k: v})[0] for k, v in values.items() if isinstance(v, (list, dict)))
            processed.append(sub_sum)
    return processed

def transform_keys(d):
    return {k[::-1].upper(): v for k, v in d.items() if isinstance(v, (int, float, list, dict))}

# Main execution starts here
data_structure = {
    'alpha': [16, -9, 'hello', 3.5],
    'beta': {
        'gamma': [4, -16, 'world'],
        'delta': {
            'epsilon': [25, -4, 'test', 2.25],
            'zeta': 42
        }
    },
    'theta': 100
}

transformed_data = transform_keys(data_structure)
processed_values = process_data(transformed_data)
aggregated_value = sum(processed_values)

# Final complex calculation sequence
x = aggregated_value
y = math.log(x) if x > 0 else 0
z = int(y) ^ 0xF0  # XOR with hexadecimal
final_result = (z << 2) + (z >> 1)  # Bit shift operations

print(f'Result: {final_result}')