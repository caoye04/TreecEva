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

def aggregate_metrics(matrix):
    results = []
    for row in matrix:
        product = 1
        for elem in row:
            product *= elem if elem != 0 else 1
        results.append(product)
    return sum(results)

# Initialize data structures
initial_data = [2, -8, 3, 5, -2, 9, 4, -6, 7, 1, -3, 12]
matrix_data = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]

# Transformation pipeline
step1 = complex_transform(initial_data)
step2 = [round(x, 2) for x in step1]

# Matrix operations
matrix_product_sum = aggregate_metrics(matrix_data)

# Bitwise operations
bitwise_result = 0
for i, val in enumerate(step2):
    if i < len(step2) - 1:
        bitwise_result ^= int(val) & int(step2[i+1])

# Final calculation
final_result = int(matrix_product_sum) ^ bitwise_result

# Apply modulo to keep result in reasonable range
final_result = final_result % 1000

print(f"Result: {final_result}")