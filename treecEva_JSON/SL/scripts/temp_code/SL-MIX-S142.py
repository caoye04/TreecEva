import math

def complex_transform(data):
    result = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            result.append(val ** 2)
        else:
            result.append(math.sqrt(abs(val)))
    return result

def nested_operation(matrix):
    transformed = []
    for row in matrix:
        transformed_row = complex_transform(row)
        transformed.append(transformed_row)
    return transformed

def calculate_determinant_2x2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def process_data_structure(container):
    values = []
    for key in sorted(container.keys()):
        if isinstance(container[key], list):
            values.extend(container[key])
        elif isinstance(container[key], dict):
            sub_values = process_data_structure(container[key])
            values.extend(sub_values)
        else:
            values.append(container[key])
    return values

# Main execution starts here
a, b, c = 3, 4, 5
initial_matrix = [[a, b], [c, a+b]]

# Step 1: Apply nested operations
processed_matrix = nested_operation(initial_matrix)

# Step 2: Calculate determinant of processed matrix
intermediate_result = calculate_determinant_2x2(processed_matrix)

# Step 3: Create complex data structure
complex_data = {
    'level1_a': [intermediate_result, 2*intermediate_result, intermediate_result**0.5],
    'level1_b': {
        'level2_a': [a*c, b**2, 2*(a+b+c)],
        'level2_b': [math.log(math.e**a), c%b, a^b]  # Note: ^ is XOR in Python
    },
    'level1_c': a << 2  # Left shift operation
}

# Step 4: Process the complex data structure
flattened_values = process_data_structure(complex_data)

# Step 5: Perform final calculation
final_sum = sum(flattened_values)
final_result = int(final_sum) & 0xFF  # Bitwise AND with 255 (0xFF)

print(f"Result: {final_result}")