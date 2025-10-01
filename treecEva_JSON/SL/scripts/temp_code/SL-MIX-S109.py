import math

def process_data(data):
    transformed = []
    for item in data:
        if isinstance(item, dict):
            total = sum(v for v in item.values() if isinstance(v, (int, float)))
            transformed.append(total)
        elif isinstance(item, list):
            product = 1
            for elem in item:
                if isinstance(elem, (int, float)):
                    product *= elem
            transformed.append(product)
        elif isinstance(item, tuple):
            transformed.append(len(item))
        else:
            transformed.append(0)
    return transformed

def aggregate_results(results):
    agg_dict = {}
    for i, val in enumerate(results):
        key = f"agg_{i}"
        if val > 0:
            agg_dict[key] = math.log(val) if val > 1 else val
        else:
            agg_dict[key] = 0
    return agg_dict

data_input = [
    {'a': 2, 'b': 3.5, 'c': -1},
    [2, 3, 4],
    (1, 2, 3, 4, 5),
    "string",
    {'x': 10, 'y': 0, 'z': 5}
]

processed = process_data(data_input)
aggregated = aggregate_results(processed)
values_list = list(aggregated.values())

# Bitwise and mathematical operations
bitwise_result = (int(values_list[0]) << 2) & int(values_list[1] * 10)
complex_expr = (math.sin(bitwise_result) ** 2) + (math.cos(bitwise_result) ** 2)

# Final aggregation
final_result = round((sum(values_list) + bitwise_result) * complex_expr)
print(f"Result: {final_result}")