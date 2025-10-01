import math

def process_data(data):
    processed = []
    for item in data:
        if isinstance(item, int):
            processed.append(item ^ 0xF)
        elif isinstance(item, str):
            num_part = ''.join(filter(str.isdigit, item))
            if num_part:
                processed.append(int(num_part) & 0xFF)
            else:
                processed.append(0)
        elif isinstance(item, float):
            processed.append(math.floor(item * 2))
        else:
            processed.append(0)
    return processed

data_container = [
    [15, "test42", 3.7],
    {"a": 25, "b": ["str123", 5.2]},
    ("hello", 7, 9.1)
]

# Flatten and process data
flat_list = []
for element in data_container:
    if isinstance(element, list):
        flat_list.extend(process_data(element))
    elif isinstance(element, dict):
        flat_list.extend(process_data(list(element.values())))
    elif isinstance(element, tuple):
        flat_list.extend(process_data(list(element)))

# Perform mathematical operations
transformed_values = []
for val in flat_list:
    if val % 2 == 0:
        transformed_values.append(val << 1)
    else:
        transformed_values.append(int(math.sqrt(val) * 10))

# Aggregate results
aggregated = {}
for i, v in enumerate(transformed_values):
    key = i % 3
    if key not in aggregated:
        aggregated[key] = 0
    aggregated[key] += v

# Final computation
final_sum = sum(aggregated.values())
final_xor = 0
for k in aggregated:
    final_xor ^= aggregated[k]

final_result = (final_sum + final_xor) % 1000
print(f'Result: {final_result}')