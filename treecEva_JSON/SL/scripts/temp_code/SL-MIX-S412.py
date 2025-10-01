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
    squared_sum = sum(x**2 for x in numbers)
    product = 1
    for num in numbers:
        product *= num if num != 0 else 1
    harmonic_mean = len(numbers) / sum(1/x if x != 0 else 0 for x in numbers)
    return math.sqrt(squared_sum) + math.log(abs(product) + 1) + harmonic_mean

data_structure = [
    [1, 'hello', 3.5, 'world'],
    [2, 4, 'test', None, 5],
    ['a', 'bb', 'ccc', 7, 8, 9]
]

# Step 1: Process nested data
processed = process_nested_data(data_structure)

# Step 2: Perform bitwise operations on processed data
bitwise_results = []
for i in range(len(processed)-1):
    bitwise_results.append(processed[i] & processed[i+1])

# Step 3: Apply mathematical transformations
transformed = []
for val in bitwise_results:
    if val > 0:
        transformed.append(math.sin(val) * math.cos(val) * 100)
    else:
        transformed.append(0)

# Step 4: Compute advanced statistics
stats_value = compute_advanced_stats(transformed)

# Step 5: Final calculation combining all results
final_result = int(sum(transformed) + stats_value) % 1000

print(f'Result: {final_result}')