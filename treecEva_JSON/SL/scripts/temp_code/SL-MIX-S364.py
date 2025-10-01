import math

def process_data(data):
    processed = []
    for item in data:
        if isinstance(item, dict):
            temp = []
            for k, v in item.items():
                if isinstance(v, list):
                    reduced = sum([x**2 for x in v if isinstance(x, (int, float))])
                    temp.append((k, math.sqrt(reduced)))
                else:
                    temp.append((k, v * 2 if isinstance(v, (int, float)) else str(v).upper()))
            processed.append(dict(temp))
        elif isinstance(item, (list, tuple)):
            flat = [elem for sublist in item for elem in (sublist if isinstance(sublist, (list, tuple)) else [sublist])]
            numeric = [x for x in flat if isinstance(x, (int, float))]
            if numeric:
                avg = sum(numeric) / len(numeric)
                processed.append(round(avg, 2))
            else:
                processed.append(''.join(map(str, flat)).lower())
        else:
            processed.append(item)
    return processed

data_structure = [
    {'a': [1, 2, 3], 'b': [4, 5]},
    ([10, 20], [30, 40]),
    {'name': 'test', 'values': [2, 4, 6, 8]},
    ('x', 'y', 'z'),
    [{'p': 5}, [7, 14]],
    100
]

processed_list = process_data(data_structure)

# Further transformation using bitwise and modular arithmetic
transformed_values = []
for idx, element in enumerate(processed_list):
    if isinstance(element, dict):
        total = sum(v for v in element.values() if isinstance(v, (int, float)))
        transformed_values.append(int(total) & 0xFF)
    elif isinstance(element, (int, float)):
        shifted = (int(element) << 2) % 256
        transformed_values.append(shifted)
    elif isinstance(element, str):
        hash_val = sum(ord(c) for c in element)
        transformed_values.append(hash_val % 100)
    else:
        transformed_values.append(0)

# Final aggregation step
aggregated = {}
for i, val in enumerate(transformed_values):
    key = i % 3
    if key not in aggregated:
        aggregated[key] = []
    aggregated[key].append(val)

# Compute final result from aggregated data
final_computation = []
for key in sorted(aggregated.keys()):
    values = aggregated[key]
    if key == 0:
        result = max(values) ^ min(values)
    elif key == 1:
        result = sum(values) | (len(values) << 4)
    else:
        result = (sum(values) * 3) >> 2
    final_computation.append(result)

final_result = sum(final_computation) % 1000
print(f'Result: {final_result}')