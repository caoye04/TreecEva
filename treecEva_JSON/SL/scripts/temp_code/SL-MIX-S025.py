import math

def transform_data(data):
    transformed = []
    for item in data:
        if isinstance(item, dict):
            temp = {}
            for k, v in item.items():
                if isinstance(v, list):
                    temp[k] = sum(v) * len(v)
                else:
                    temp[k] = v ** 2
            transformed.append(temp)
        elif isinstance(item, tuple):
            transformed.append({"tuple_sum": sum(item)})
        else:
            transformed.append({"value": item * 3})
    return transformed

data_structure = [
    {"a": [1, 2, 3], "b": 4},
    (5, 6, 7),
    8,
    {"c": [2, 4, 6, 8], "d": 3, "e": [1]},
    (10, 20)
]

processed_data = transform_data(data_structure)

aggregated_values = []
for entry in processed_data:
    if 'a' in entry:
        aggregated_values.append(entry['a'] + entry['b'])
    elif 'tuple_sum' in entry:
        aggregated_values.append(entry['tuple_sum'] * 2)
    elif 'c' in entry:
        aggregated_values.append(sum([entry['c'], entry['d']**2, len(entry['e'])]))
    elif 'value' in entry:
        aggregated_values.append(entry['value'] // 2)

# Perform advanced mathematical computation
log_sum = sum([math.log(x) for x in aggregated_values if x > 0])
exp_avg = math.exp(sum(aggregated_values) / len(aggregated_values))

# Combine results using bitwise operations
bitwise_combined = int(log_sum) & int(exp_avg)

# Final complex calculation
final_result = (bitwise_combined ^ 0xFF) + (bitwise_combined << 2) - (len(aggregated_values) * 3)

print(f"Result: {final_result}")