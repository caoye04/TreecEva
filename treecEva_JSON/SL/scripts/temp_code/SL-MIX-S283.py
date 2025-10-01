import math

def process_data(data):
    processed = []
    for item in data:
        if isinstance(item, dict):
            temp = 0
            for k, v in item.items():
                if isinstance(v, list):
                    temp += sum(v)
                elif isinstance(v, int):
                    temp += v * 2
            processed.append(temp)
        elif isinstance(item, list):
            inner_sum = 0
            for elem in item:
                if isinstance(elem, str):
                    inner_sum += len(elem)
                elif isinstance(elem, int):
                    inner_sum += elem ** 2
            processed.append(inner_sum)
    return processed

data_structure = [
    {'a': [1, 2, 3], 'b': 10},
    [4, 'hello', 5],
    {'x': [6, 7], 'y': [8, 9, 10], 'z': 3},
    ['world', 2, 'test']
]

processed_list = process_data(data_structure)

# Further transformation using mathematical operations
transformed_values = []
for val in processed_list:
    sqrt_val = math.sqrt(val) if val >= 0 else 0
    transformed_values.append(sqrt_val)

# Bitwise operations on integer parts
bitwise_results = []
for tval in transformed_values:
    intval = int(tval)
    if intval > 0:
        shifted = intval << 2  # Left shift by 2 bits
        xor_result = shifted ^ 5
        bitwise_results.append(xor_result)
    else:
        bitwise_results.append(0)

# Final aggregation with exponentiation
aggregated = sum(bitwise_results)
final_result = aggregated ** 2 + math.log(aggregated + 1) if aggregated > 0 else 0
print(f'Result: {final_result}')