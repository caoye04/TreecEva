import math

def transform_data(data):
    processed = []
    for item in data:
        if isinstance(item, dict):
            temp = []
            for k, v in item.items():
                if isinstance(v, list):
                    reduced = sum([x**2 for x in v if isinstance(x, (int, float))])
                    temp.append((k, math.sqrt(reduced)))
                else:
                    temp.append((k, v))
            processed.append(dict(temp))
        elif isinstance(item, list):
            flattened = [elem for sublist in item for elem in (sublist if isinstance(sublist, list) else [sublist])]
            numeric_vals = [x for x in flattened if isinstance(x, (int, float))]
            if numeric_vals:
                avg_val = sum(numeric_vals) / len(numeric_vals)
                processed.append(round(avg_val, 2))
            else:
                processed.append(0)
        else:
            processed.append(item)
    return processed

data_input = [
    {'a': [1, 2, 3], 'b': ['text', 4.5]},
    [{'nested_list': [10, 20]}, [7, 14, 21]],
    ('tuple_element', 99),
    [None, [math.pi, 2.718], 'string'],
    {'c': [5, -3, 2], 'd': []}
]

transformed = transform_data(data_input)

# Further processing
aggregated_values = []
for element in transformed:
    if isinstance(element, dict):
        total = sum([v for v in element.values() if isinstance(v, (int, float))])
        aggregated_values.append(total)
    elif isinstance(element, (int, float)):
        aggregated_values.append(element * 2)
    elif isinstance(element, tuple):
        # Take second element of tuple if numeric
        if len(element) > 1 and isinstance(element[1], (int, float)):
            aggregated_values.append(element[1] ** 0.5)
        else:
            aggregated_values.append(0)
    else:
        aggregated_values.append(0)

# Final aggregation
final_result = round(sum(aggregated_values) + math.log(sum([x for x in aggregated_values if x > 0])), 4)
print(f"Result: {final_result}")