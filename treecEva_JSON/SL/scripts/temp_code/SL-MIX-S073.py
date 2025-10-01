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
        elif isinstance(item, tuple):
            processed.append(math.prod(item))
        else:
            processed.append(item ** 2)
    return processed

data_structure = [
    {'a': [1, 2, 3], 'b': 4},
    (2, 3, 5),
    7,
    {'x': [10, -2], 'y': 3, 'z': [0]},
    (1, 1, 1, 2),
    9
]

processed_list = process_data(data_structure)

# Perform cumulative operations
accumulated = []
current_sum = 0
for val in processed_list:
    current_sum += val
    accumulated.append(current_sum)

# Apply transformation using lambda and filter
transformed = list(map(lambda x: x // 2 if x % 2 == 0 else x * 3, accumulated))
filtered_vals = list(filter(lambda x: x > 10, transformed))

# Final aggregation step
nested_dict = {
    'level1': {
        'level2': {
            'values': filtered_vals,
            'computed': sum(filtered_vals) if filtered_vals else 0
        }
    },
    'auxiliary': [100, 200, 300]
}

# Extract and compute final result
final_result = nested_dict['level1']['level2']['computed'] + len(nested_dict['auxiliary']) * max(nested_dict['auxiliary'])
print(f"Result: {final_result}")