import math

def complex_transform(data):
    transformed = []
    for i, val in enumerate(data):
        if i % 3 == 0:
            transformed.append(val ** 2)
        elif i % 3 == 1:
            transformed.append(math.sqrt(abs(val)))
        else:
            transformed.append(math.log(abs(val) + 1))
    return transformed

def aggregate_stats(values):
    product = 1
    sum_val = 0
    count = 0
    for v in values:
        if v > 0:
            product *= v
            sum_val += v
            count += 1
    avg = sum_val / count if count > 0 else 0
    return product, avg, count

# Initialize data structures
matrix = [
    [2, -4, 8, -16],
    [32, -64, 128, -256],
    [512, -1024, 2048, -4096]
]

# Flatten the matrix
flat_list = [item for sublist in matrix for item in sublist]

# Apply complex transformation
transformed_data = complex_transform(flat_list)

# Perform bit shifting operations on first 4 elements
shifted_values = []
for i in range(4):
    if i % 2 == 0:
        shifted_values.append(int(transformed_data[i]) << 1)  # Left shift
    else:
        shifted_values.append(int(transformed_data[i]) >> 1)  # Right shift

# Replace first 4 elements with shifted values
transformed_data[:4] = shifted_values

# Calculate aggregate statistics
product, average, count = aggregate_stats(transformed_data)

# Perform final calculation
final_result = int((product ** (1/3)) + (average * count) - len(transformed_data))

# Apply modulo to ensure result is within reasonable range
final_result = final_result % 1000000

print(f"Result: {final_result}")