import math

def complex_transform(data):
    transformed = []
    for i, val in enumerate(data):
        if isinstance(val, int):
            transformed.append(val ** 2 if i % 2 == 0 else math.sqrt(val))
        elif isinstance(val, str):
            transformed.append(val[::-1].upper())
        else:
            transformed.append(val)
    return transformed

def aggregate_values(items):
    total = 0
    for item in items:
        if isinstance(item, (int, float)):
            total += item
        elif isinstance(item, str):
            total += len(item)
    return total

# Initial data setup
matrix = [
    [1, 'hello', 3.5],
    [lambda x: x * 2, 16, 'world'],
    [9, 'test', 25]
]

# Transformation phase 1
for i in range(len(matrix)):
    matrix[i] = complex_transform(matrix[i])

# Intermediate processing
intermediate = []
for row in matrix:
    processed_row = []
    for item in row:
        if callable(item):
            processed_row.append(item(5))
        else:
            processed_row.append(item)
    intermediate.append(processed_row)

# Aggregation and further computation
aggregated = [aggregate_values(row) for row in intermediate]

# Mathematical operations
x = aggregated[0]
y = aggregated[1]
z = aggregated[2]

a = (x * y) // z
b = math.log(a, 2) if a > 0 else 0
c = int(b) ^ 0xF0

# Final complex calculation
final_result = (c * 3) + (x % 7) - (y // 4) + int(math.sin(z) * 100)

print(f'Result: {final_result}')