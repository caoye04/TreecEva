import math

def complex_transform(data):
    transformed = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            transformed.append(val ** 2)
        else:
            transformed.append(math.sqrt(abs(val)))
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
    [2, -4, 3],
    [-1, 5, -2],
    [0, 7, 4]
]

# Flatten matrix and apply transformation
flat_list = [item for sublist in matrix for item in sublist]
transformed_data = complex_transform(flat_list)

# Perform aggregation
product, average, count = aggregate_stats(transformed_data)

# Bitwise and mathematical operations
bitwise_result = (int(product) & 0xFF) | (int(average) << 2)
log_val = math.log(abs(bitwise_result) + 1)

# Final calculation sequence
x = log_val * 3
y = math.sin(x) * 100
z = int(y) ^ 0xAA
final_result = z % 42

print(f'Result: {final_result}')