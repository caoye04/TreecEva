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
    transposed = list(zip(*matrix))
    processed = []
    for row in transposed:
        processed.append(sum(complex_transform(list(row))))
    return processed

def calculate_checksum(values):
    checksum = 0
    for i, v in enumerate(values):
        checksum ^= (v << (i % 5))
    return checksum

# Main execution starts here
initial_data = [
    [3, -4, 5, -6, 7],
    [-2, 8, -9, 10, -11],
    [1, -3, 4, -5, 6],
    [-7, 9, -8, 11, -10],
    [12, -13, 14, -15, 16]
]

# Step 1: Process the matrix
processed_data = nested_operation(initial_data)

# Step 2: Apply a filter and transformation
filtered_data = [x for x in processed_data if x > 0]
transformed_data = [math.log(x) for x in filtered_data if x > 1]

# Step 3: Calculate aggregate values
sum_val = sum(transformed_data)
product_val = 1
for x in filtered_data:
    product_val *= x

# Step 4: Perform bit operations
bitwise_result = int(sum_val) & int(product_val)

# Step 5: Generate checksum
checksum = calculate_checksum(filtered_data)

# Step 6: Final computation
final_result = (bitwise_result ^ checksum) % 1000

print(f"Result: {final_result}")