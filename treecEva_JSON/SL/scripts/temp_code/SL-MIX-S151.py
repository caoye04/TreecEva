import math

def complex_transform(data):
    result = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            result.append(val ** 2)
        else:
            result.append(math.sqrt(abs(val)))
    return result

def nested_operation(x, y, z):
    temp1 = (x & y) | z
    temp2 = x ^ (y << 2)
    return temp1 + temp2

data_structure = {
    'level1': {
        'level2a': [1, -4, 9, -16, 25],
        'level2b': [
            {'inner1': 3, 'inner2': [2, 4, 8]},
            {'inner1': 5, 'inner2': [1, 3, 9]}
        ]
    },
    'level1b': [10, 20, 30]
}

# Process the nested data
processed_data = complex_transform(data_structure['level1']['level2a'])

# Perform bitwise operations on the first two elements
bitwise_result = nested_operation(int(processed_data[0]), int(processed_data[1]), int(processed_data[2]))

# Extract and transform inner data
inner_list = []
for item in data_structure['level1']['level2b']:
    product = 1
    for num in item['inner2']:
        product *= num
    inner_list.append(item['inner1'] * product)

# Calculate a cumulative value
cumulative = 0
for i, val in enumerate(inner_list):
    if i == 0:
        cumulative = val
    else:
        cumulative = cumulative * val + i

# Final complex calculation
final_result = ((bitwise_result + cumulative) % 1000) * math.log(processed_data[3] + processed_data[4])

# Apply a final transformation
final_result = int(final_result) ^ (len(str(final_result)) << 3)

print(f'Result: {final_result}')