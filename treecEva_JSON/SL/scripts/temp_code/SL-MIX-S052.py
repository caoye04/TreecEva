import math

def complex_transform(data):
    transformed = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            transformed.append(val ** 2)
        else:
            transformed.append(math.sqrt(abs(val)))
    return transformed

def nested_operation(matrix):
    result = 0
    for row in matrix:
        temp = 1
        for elem in row:
            temp *= elem if elem != 0 else 1
        result += temp
    return result

data_structure = {
    'level1': {
        'level2a': [3, -4, 5, -6],
        'level2b': [
            {'inner1': 2, 'inner2': [7, 8]},
            {'inner1': 3, 'inner2': [9, 10]}
        ]
    },
    'level1b': [
        [1, 2, 0],
        [3, 0, 4],
        [0, 5, 6]
    ]
}

# Process level2a
processed_a = complex_transform(data_structure['level1']['level2a'])

# Process level2b
processed_b_values = []
for item in data_structure['level1']['level2b']:
    processed_b_values.extend(item['inner2'])
processed_b = complex_transform(processed_b_values)

# Combine processed results
combined = processed_a + processed_b

# Perform aggregation
aggregated = 0
for i, val in enumerate(combined):
    if i % 3 == 0:
        aggregated += val
    elif i % 3 == 1:
        aggregated -= val
    else:
        aggregated *= val if val != 0 else 1

# Process level1b matrix
matrix_result = nested_operation(data_structure['level1b'])

# Final calculation
final_result = int((aggregated + matrix_result) / (len(combined) - len(processed_b)))

print(f"Result: {final_result}")