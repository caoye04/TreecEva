import math

def transform_data(data):
    transformed = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            transformed.append(val ** 2)
        else:
            transformed.append(math.sqrt(val))
    return transformed

def aggregate(values):
    total = 0
    for v in values:
        total ^= int(v)
    return total

data_dict = {
    'group_a': [4, 9, 16, 25],
    'group_b': [36, 49, 64, 81],
    'group_c': [100, 121, 144, 169]
}

nested_list = [
    [data_dict['group_a'][0], data_dict['group_b'][1]],
    [data_dict['group_c'][2], data_dict['group_a'][3]],
    [data_dict['group_b'][0], data_dict['group_c'][1]]
]

mapped_values = list(map(lambda x: x[0] * x[1], nested_list))

transformed_mapped = transform_data(mapped_values)

bitwise_aggregation = aggregate(transformed_mapped)

# Perform modulus with a complex expression
complex_modulus_base = (bitwise_aggregation + 17) * 3 - 5
final_modulus = complex_modulus_base % 19

# Final adjustment using trigonometric scaling
scale_factor = round(math.sin(math.pi / 6) * 10)
final_result = final_modulus * scale_factor + 1

print(f'Result: {final_result}')