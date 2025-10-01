import math

def complex_transform(data):
    transformed = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            transformed.append(val ** 2)
        else:
            transformed.append(math.sqrt(abs(val)))
    return transformed

def aggregate_metrics(series):
    metrics = {
        'sum': sum(series),
        'product': 1,
        'count': len(series)
    }
    for num in series:
        if num != 0:
            metrics['product'] *= num
    return metrics

def evaluate_expression(a, b, c):
    x = (a & b) ^ c
    y = a | (b << 2)
    z = ~(x ^ y)
    return (x + y) % (abs(z) + 1)

# Main execution starts here
matrix = [
    [3, -4, 5],
    [-2, 7, -1],
    [6, 0, -8]
]

flattened = [item for sublist in matrix for item in sublist]
transformed_data = complex_transform(flattened)
metrics = aggregate_metrics(transformed_data)

# Perform bit operations on metrics
bitwise_result = evaluate_expression(
    int(metrics['sum']), 
    int(metrics['product'] % 1000), 
    int(metrics['count'])
)

# Final calculation
final_result = (
    (math.floor(math.log(abs(bitwise_result) + 1)) + 1) *
    (len(str(abs(bitwise_result))) + 1) +
    (bin(bitwise_result).count('1') if bitwise_result >= 0 else bin(bitwise_result & 0xFFFFFFFF).count('1'))
) % 100

print(f"Result: {final_result}")