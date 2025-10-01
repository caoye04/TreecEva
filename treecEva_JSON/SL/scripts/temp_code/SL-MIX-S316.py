import math

def complex_transform(data):
    transformed = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            transformed.append(val ** 2)
        else:
            transformed.append(math.sqrt(abs(val)))
    return transformed

def aggregate_metrics(matrix):
    metrics = {}
    metrics['row_sums'] = [sum(row) for row in matrix]
    metrics['col_products'] = []
    for j in range(len(matrix[0])):
        product = 1
        for i in range(len(matrix)):
            product *= matrix[i][j]
        metrics['col_products'].append(product)
    return metrics

def encode_string(s):
    encoded = ''
    for char in s:
        encoded += str(ord(char) % 10)
    return int(encoded) if encoded else 0

# Initialize complex nested data structures
nested_data = [
    [1, -4, 9],
    [16, -25, 36],
    [49, -64, 81]
]

# Process the nested data
processed_rows = []
for row in nested_data:
    processed_rows.append(complex_transform(row))

# Calculate metrics from processed data
metrics = aggregate_metrics(processed_rows)

# Perform string encoding
secret_key = encode_string("ML")

# Complex mathematical combination
intermediate = 0
for i, (row_sum, col_product) in enumerate(zip(metrics['row_sums'], metrics['col_products'])):
    if i % 2 == 0:
        intermediate += row_sum * math.log(abs(col_product) + 1)
    else:
        intermediate -= col_product / (row_sum + 1)

# Final calculation step
result = int((intermediate + secret_key) ** 0.5) ^ (len(metrics['row_sums']) << 2)

print(f"Result: {result}")