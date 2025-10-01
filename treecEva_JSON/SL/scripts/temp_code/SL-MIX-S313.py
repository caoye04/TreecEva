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
        for i, val in enumerate(row):
            if i % 3 == 0:
                total += val * 2
            elif i % 3 == 1:
                total -= val
            else:
                total *= val if val != 0 else 1
        totals.append(total)
    return sum(totals)

# Initialize data structures
nested_data = [
    [1, -4, 3, 2],
    [2.5, -9, 4, -16, 5],
    [6, -25, 7, 8, -9, 10]
]

# Transformation step 1
step1_data = [complex_transform(row) for row in nested_data]

# Flatten and filter
flattened = [item for sublist in step1_data for item in sublist]
filtered_data = [x for x in flattened if x > 2]

# Create dictionary with mathematical operations
mapped_dict = {}
for i, val in enumerate(filtered_data):
    if i % 4 == 0:
        mapped_dict[i] = math.log(val) if val > 0 else 0
    elif i % 4 == 1:
        mapped_dict[i] = math.sin(val)
    elif i % 4 == 2:
        mapped_dict[i] = math.cos(val)
    else:
        mapped_dict[i] = val ** 0.5

# Build matrix from dictionary values
matrix_data = []
keys = list(mapped_dict.keys())
sorted_values = [mapped_dict[k] for k in sorted(keys)]

for i in range(0, len(sorted_values), 3):
    matrix_data.append(sorted_values[i:i+3])

# Final aggregation
result = aggregate_values(matrix_data)

# Apply final transformation
if result > 0:
    result = int(result * 1.5) ^ 42  # XOR with 42
else:
    result = int(result * -1.5) & 255  # Bitwise AND with 255

print(f"Result: {result}")