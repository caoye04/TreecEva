import math

data = {
    'a': [1, 2, 3, 4, 5],
    'b': [6, 7, 8, 9, 10],
    'c': [11, 12, 13, 14, 15]
}

# Step 1: Create a new dictionary with transformed values
transformed = {k: [x**2 for x in v] for k, v in data.items()}

# Step 2: Apply a filter to keep only even squared values
filtered = {k: [x for x in v if x % 2 == 0] for k, v in transformed.items()}

# Step 3: Calculate the sum of square roots of the filtered values
sum_sqrt = sum(math.sqrt(x) for v in filtered.values() for x in v)

# Step 4: Apply a complex mathematical operation
result = int(sum_sqrt * math.log(sum_sqrt + 1))

# Step 5: Perform bitwise operations on the result
final_result = (result & 0xFF) ^ (result >> 4)
