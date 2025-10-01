import math

def complex_transform(data):
    transformed = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            transformed.append(val ** 2)
        else:
            transformed.append(math.sqrt(abs(val)))
    return transformed

def aggregate_values(matrix):
    totals = []
    for row in matrix:
        total = 0
        for val in row:
            total += val if val > 0 else -val
        totals.append(total)
    return totals

data_structure = [
    [1, -4, 9, -16, 25],
    [36, -49, 64, -81, 100],
    [-121, 144, -169, 196, -225]
]

# Process the data structure
processed_data = []
for sublist in data_structure:
    processed_data.append(complex_transform(sublist))

# Aggregate values
aggregated = aggregate_values(processed_data)

# Perform bitwise operations
bitwise_result = aggregated[0]
for i in range(1, len(aggregated)):
    if i % 2 == 1:
        bitwise_result = bitwise_result & int(aggregated[i])
    else:
        bitwise_result = bitwise_result ^ int(aggregated[i])

# Mathematical transformation
transformed_value = math.log(abs(bitwise_result)) * math.sin(math.pi / 4)

# String manipulation and final combination
str_parts = [str(int(transformed_value)), str(len(aggregated)), str(sum(aggregated))]
combined_str = ''.join(str_parts)

# Final calculation step
result = (int(combined_str) // 10) + (bitwise_result % 7) - len(str_parts)

print(f"Result: {result}")