import math

def complex_transform(data_list):
    transformed = []
    for item in data_list:
        if isinstance(item, dict):
            temp = 0
            for k, v in item.items():
                if isinstance(v, list):
                    temp += sum(v) * len(k)
                else:
                    temp += v * len(k)
            transformed.append(temp)
        elif isinstance(item, list):
            transformed.append(sum([x**2 for x in item if isinstance(x, (int, float))]))
        else:
            transformed.append(item * 3)
    return transformed

def process_strings(str_list):
    results = []
    for s in str_list:
        if 'x' in s:
            results.append(s.count('x') * 2)
        elif 'y' in s:
            results.append(s.count('y') * 3)
        else:
            results.append(len(s))
    return results

# Initialize complex nested data structure
data = [
    {'alpha': [1, 2, 3], 'beta': 4},
    [2, 3, 4, 5],
    {'gamma': [{'delta': 5}, 6], 'epsilon': [7, 8, 9]},
    'example_xxxx',
    'test_yyy',
    10
]

# Perform transformations
stage1 = complex_transform(data[:3])
stage2 = process_strings(data[3:5])
combined = stage1 + stage2 + [data[5]]

# Mathematical operations
squared_sum = sum([x**2 for x in combined if isinstance(x, (int, float))])
log_value = math.log(squared_sum, 2) if squared_sum > 0 else 0

# Bitwise operations
bitwise_result = (int(log_value) & 15) | (int(log_value) >> 2)

# Final calculation step
result = (bitwise_result * 3) + (int(log_value) % 7) - len(combined)

print(f"Result: {result}")