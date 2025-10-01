import math

def complex_transform(data_dict):
    result = []
    for key, value in data_dict.items():
        if isinstance(value, list):
            transformed = [math.sqrt(abs(x)) if x >= 0 else -math.sqrt(abs(x)) for x in value]
            result.append(sum(transformed))
        elif isinstance(value, dict):
            sub_sum = sum([v for v in value.values() if isinstance(v, (int, float))])
            result.append(math.log(sub_sum + 1) if sub_sum > 0 else 0)
        else:
            result.append(value ** 2 if value > 0 else - (value ** 2))
    return result

data = {
    'a': [16, -9, 4, -1],
    'b': {'x': 2.5, 'y': 3.5, 'z': 'ignore'},
    'c': -5,
    'd': [0, -4, 9],
    'e': {'p': 1, 'q': 2.2, 'r': 3.8}
}

transformed_list = complex_transform(data)

# Perform advanced aggregation
aggregated = 0
for i, val in enumerate(transformed_list):
    if i % 2 == 0:
        aggregated += math.ceil(val)
    else:
        aggregated += math.floor(val)

# Apply final transformation
final_result = (aggregated & 0xFF) ^ (aggregated >> 4)

print(f"Result: {final_result}")