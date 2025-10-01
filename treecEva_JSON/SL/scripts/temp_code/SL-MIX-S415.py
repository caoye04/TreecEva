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
    for v in values:
        product *= v if v != 0 else 1
        sum_val += v
    return product, sum_val

# Initialize data structures
matrix = [
    [2, -4, 3],
    [5, -2, 7],
    [1, 8, -3]
]

# Process matrix diagonals
primary_diag = [matrix[i][i] for i in range(len(matrix))]
secondary_diag = [matrix[i][len(matrix)-1-i] for i in range(len(matrix))]

# Apply transformations
processed_primary = complex_transform(primary_diag)
processed_secondary = complex_transform(secondary_diag)

# Aggregate statistics
primary_product, primary_sum = aggregate_stats(processed_primary)
secondary_product, secondary_sum = aggregate_stats(processed_secondary)

# Calculate intermediate values
intermediate_a = (primary_product + secondary_sum) & 0xFF
intermediate_b = (secondary_product - primary_sum) | 0xF0

# Bitwise operations with shifts
shifted_a = intermediate_a << 2
shifted_b = intermediate_b >> 1

# Final calculation combining all
final_result = (shifted_a ^ shifted_b) + int(math.log(abs(primary_sum - secondary_sum)) * 100)

print(f"Result: {final_result}")