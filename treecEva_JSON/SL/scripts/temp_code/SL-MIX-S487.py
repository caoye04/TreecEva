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

def aggregate_stats(nums):
    if not nums:
        return 0
    product = 1
    for n in nums:
        product *= n if n != 0 else 1
    geometric_mean = product ** (1.0 / len(nums))
    return geometric_mean

data_matrix = [
    [2, -8, 3, 16, -5],
    [4, 9, -2, 7, 1],
    [6, -3, 12, -4, 8]
]

# Process each row with complex transformation
processed_rows = [complex_transform(row) for row in data_matrix]

# Flatten the processed data
flattened = [item for sublist in processed_rows for item in sublist]

# Filter out non-finite numbers
valid_numbers = [x for x in flattened if math.isfinite(x)]

# Apply bitwise operations on indices where value > 5
bitwise_results = []
for idx, val in enumerate(valid_numbers):
    if val > 5:
        bitwise_results.append(idx & (int(val) ^ 0xF))

# Calculate aggregate statistics
agg_stat = aggregate_stats(bitwise_results)

# Perform final computation
final_result = 0
for i in range(len(valid_numbers)):
    weight = 1.0 / (i + 1)
    adjustment = math.sin(valid_numbers[i]) * math.cos(agg_stat)
    final_result += (valid_numbers[i] + adjustment) * weight

# Round to nearest integer
final_result = round(final_result)

print(f"Result: {final_result}")