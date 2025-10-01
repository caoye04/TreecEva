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

def aggregate_values(values):
    product = 1
    sum_val = 0
    for v in values:
        product *= v if v != 0 else 1
        sum_val += v
    return product, sum_val

data_matrix = [
    [2, -8, 3, 16, -5, 9],
    [4, -27, 25, -32, 49, -64],
    [1, 100, -121, 144, -169, 196]
]

# Process each row with complex_transform
processed_rows = [complex_transform(row) for row in data_matrix]

# Flatten the processed_rows into a single list
flattened = [item for sublist in processed_rows for item in sublist]

# Filter out non-finite values
filtered = [x for x in flattened if math.isfinite(x)]

# Aggregate values to get product and sum
product, sum_val = aggregate_values(filtered)

# Perform bit-wise operations on the integer parts of sum and product
sum_int = int(sum_val)
prod_int = int(product)

bitwise_xor = sum_int ^ prod_int
bitwise_or = sum_int | prod_int

# Calculate final result using multiple operations
final_result = (bitwise_xor * 3 + bitwise_or) % 1000

print(f'Result: {final_result}')