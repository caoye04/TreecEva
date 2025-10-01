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

def aggregate_stats(values):
    if not values:
        return 0
    product = 1
    for v in values:
        product *= v if v != 0 else 1
    return product ** (1/len(values))

# Initialize data structures
matrix = [
    [2, -4, 8, 16],
    [32, -64, 128, 256],
    [512, -1024, 2048, 4096]
]

# Flatten matrix and apply transformation
flat_data = [item for sublist in matrix for item in sublist]
transformed_data = complex_transform(flat_data)

# Apply conditional filtering
filtered_data = [x for x in transformed_data if x > 10 or x < -10]

# Calculate statistical measure
stat_measure = aggregate_stats(filtered_data)

# Perform bitwise operations on integer parts
int_part = int(stat_measure)
bitwise_result = (int_part << 2) ^ (int_part >> 1) & 0xFF

# String manipulation sequence
pattern = "COMPLEX_" + str(bitwise_result) + "_CALCULATION"
char_sum = sum(ord(c) for c in pattern if c.isalnum())

# Final computation combining all previous results
final_result = (char_sum * bitwise_result) % (len(filtered_data) + 1)

print(f"Result: {final_result}")