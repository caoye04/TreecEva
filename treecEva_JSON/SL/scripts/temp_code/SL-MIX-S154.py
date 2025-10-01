import math

def complex_transform(data_dict):
    transformed = {}
    for key, value in data_dict.items():
        if isinstance(value, list):
            transformed[key] = [math.log(x) if x > 0 else 0 for x in value]
        elif isinstance(value, dict):
            transformed[key] = {k: v**2 for k, v in value.items()}
        else:
            transformed[key] = value
    return transformed

def aggregate_stats(data):
    total = 0
    count = 0
    for item in data:
        if isinstance(item, (int, float)):
            total += item
            count += 1
        elif isinstance(item, list):
            sub_total, sub_count = aggregate_stats(item)
            total += sub_total
            count += sub_count
    return total, count

# Initialize complex nested data structure
data_structure = {
    'alpha': [math.e, math.pi, 2.718],
    'beta': {
        'x': 3,
        'y': 4,
        'z': [{'p': 2, 'q': 3}, 5, [6, 7]]
    },
    'gamma': [
        [1, 2, {'a': 3, 'b': [4, 5]}],
        {'m': [8, 9], 'n': 10}
    ]
}

# Transform the data
transformed_data = complex_transform(data_structure)

# Extract and process values
values_list = []
for key, value in transformed_data.items():
    if isinstance(value, list):
        for item in value:
            if isinstance(item, (int, float)):
                values_list.append(item)
            elif isinstance(item, list):
                values_list.extend(item)
            elif isinstance(item, dict):
                for k, v in item.items():
                    if isinstance(v, list):
                        values_list.extend(v)
                    else:
                        values_list.append(v)
    elif isinstance(value, dict):
        for k, v in value.items():
            values_list.append(v)

# Perform statistical aggregation
sum_val, count_val = aggregate_stats(values_list)
average_val = sum_val / count_val if count_val != 0 else 0

# Bitwise and mathematical operations
bitwise_result = (int(average_val) & 0xF) | (int(sum_val) >> 2)

# Final calculation step
result = (bitwise_result ^ int(math.sqrt(sum_val))) + len(values_list) * 3

print(f"Result: {result}")