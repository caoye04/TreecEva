import math

def complex_transform(data):
    transformed = []
    for i, val in enumerate(data):
        if isinstance(val, int):
            transformed.append(val ** 2 if i % 2 == 0 else math.sqrt(val))
        elif isinstance(val, str):
            transformed.append(len(val) * 3)
        else:
            transformed.append(sum(val) if isinstance(val, list) else -1)
    return transformed

def process_nested(nested_dict):
    results = []
    for key, value in nested_dict.items():
        if isinstance(value, dict):
            sub_result = process_nested(value)
            results.append(sum(sub_result) if sub_result else 0)
        else:
            results.append(value * 2 if isinstance(value, int) else len(value))
    return results

data_structure = {
    'a': [1, 4, [2, 3]],
    'b': {'c': [5, 6], 'd': 7},
    'e': 'hello world',
    'f': [[1, 2], [3, [4, 5]]]
}

# Step 1: Process the nested dictionary
step1_result = process_nested(data_structure)

# Step 2: Flatten and transform the data
flat_list = []
for item in step1_result:
    if isinstance(item, list):
        flat_list.extend(item)
    else:
        flat_list.append(item)

transformed_data = complex_transform(flat_list)

# Step 3: Perform mathematical operations
computed_values = []
for i, val in enumerate(transformed_data):
    if isinstance(val, (int, float)):
        if i % 3 == 0:
            computed_values.append(math.log(val + 1) if val > 0 else 0)
        elif i % 3 == 1:
            computed_values.append(math.sin(val))
        else:
            computed_values.append(math.cos(val))
    else:
        computed_values.append(0)

# Step 4: Aggregate results with bitwise operations
aggregate = 0
for i, val in enumerate(computed_values):
    if isinstance(val, (int, float)):
        bits = int(val * 1000) & 0xFF
        aggregate ^= bits

# Step 5: Final calculation
final_result = (aggregate * 13) % 1000
print(f'Result: {final_result}')