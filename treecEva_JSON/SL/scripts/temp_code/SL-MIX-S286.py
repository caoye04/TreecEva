import math

def process_data(arr):
    result = []
    for i in range(len(arr)):
        if isinstance(arr[i], int) and arr[i] > 0:
            result.append(math.factorial(arr[i]))
        elif isinstance(arr[i], str):
            result.append(len(arr[i]) ** 2)
        else:
            result.append(0)
    return result

data = [
    5,
    "hello",
    -3,
    "world!",
    4.2,
    3,
    "a",
    None
]

processed = process_data(data)

# Perform advanced aggregation
aggregated = 0
for idx, val in enumerate(processed):
    if idx % 2 == 0:
        aggregated += val * 2
    else:
        aggregated -= val // 3

# Apply modulus and power operations
mod_power = (aggregated % 100) ** 2

# Nested list comprehension with conditionals
nested_comp = [x * 2 if x % 3 == 0 else x // 2 if x % 2 == 0 else x for x in processed]

# Sum of transformed list
sum_transformed = sum(nested_comp)

# Final complex calculation
final_result = (mod_power + sum_transformed) ^ 0xFF  # XOR with 255

print(f"Result: {final_result}")