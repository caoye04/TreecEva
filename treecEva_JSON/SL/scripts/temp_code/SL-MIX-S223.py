import math

def process_nested_data(data):
    result = []
    for sublist in data:
        temp = []
        for item in sublist:
            if isinstance(item, int):
                temp.append(item ** 2)
            elif isinstance(item, str):
                temp.append(len(item))
            else:
                temp.append(0)
        result.append(sum(temp))
    return result

def compute_advanced_stats(numbers):
    if not numbers:
        return 0
    n = len(numbers)
    mean = sum(numbers) / n
    variance = sum((x - mean) ** 2 for x in numbers) / n
    return math.sqrt(variance)  # Standard deviation

data_structure = [
    [1, 'hello', 3.5, 'world'],
    ['a', 'bb', 'ccc', 4, 5],
    [10, 20, 'test', 30]
]

# Process the nested data
processed = process_nested_data(data_structure)

# Perform bit shifting operations on processed values
shifted_values = []
for i, val in enumerate(processed):
    if i % 2 == 0:
        shifted_values.append(val << 1)  # Left shift for even indices
    else:
        shifted_values.append(val >> 1)  # Right shift for odd indices

# Apply mathematical transformations
transformed = []
for v in shifted_values:
    if v > 50:
        transformed.append(math.log(v))
    else:
        transformed.append(math.exp(v/100))

# Compute advanced statistics
stats_val = compute_advanced_stats(transformed)

# Final complex calculation involving multiple operations
accumulator = 0
for i, t in enumerate(transformed):
    if i % 2 == 0:
        accumulator += t * stats_val
    else:
        accumulator -= t / stats_val

final_result = int(accumulator * 1000)  # Convert to integer after scaling
print(f'Result: {final_result}')