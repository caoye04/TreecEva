import math

def complex_transform(data):
    transformed = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            transformed.append(val ** 2)
        else:
            transformed.append(math.sqrt(abs(val)))
    return transformed

def aggregate_stats(nums):
    product = 1
    for n in nums:
        product *= n if n != 0 else 1
    return sum(nums), product, max(nums) - min(nums)

# Initialize data structures
matrix = [
    [3, -4, 5],
    [2, 0, -1],
    [7, 8, -9]
]

# Process matrix diagonals
primary_diag = [matrix[i][i] for i in range(3)]
secondary_diag = [matrix[i][2-i] for i in range(3)]

# Apply transformations
processed_primary = complex_transform(primary_diag)
processed_secondary = complex_transform(secondary_diag)

# Statistical aggregations
sum_p, prod_p, range_p = aggregate_stats(processed_primary)
sum_s, prod_s, range_s = aggregate_stats(processed_secondary)

# Nested dictionary construction
metrics = {
    'primary': {
        'sum': sum_p,
        'product': prod_p,
        'range': range_p,
        'elements': processed_primary
    },
    'secondary': {
        'sum': sum_s,
        'product': prod_s,
        'range': range_s,
        'elements': processed_secondary
    }
}

# Bitwise operations on statistical values
bitwise_xor = (int(metrics['primary']['product']) ^ int(metrics['secondary']['sum'])) & 255

# Trigonometric adjustment
angle_rad = math.acos(0.5)  # 60 degrees in radians
trig_factor = math.sin(angle_rad) * 10

# Final calculation step
result = int((bitwise_xor * trig_factor) // (metrics['primary']['range'] + metrics['secondary']['range'] + 1))

print(f"Result: {result}")