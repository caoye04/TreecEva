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
    geometric_mean = product ** (1/len(numbers)) if product > 0 else 0
    return math.log(squared_sum + 1) * geometric_mean

data_structure = [
    [1, 'hello', 3, 'world'],
    [2.5, 'test', 0, 'a'*5],
    [4, 3, 'python', 7]
]

# Process the nested data
processed = process_nested_data(data_structure)

# Perform bit shifting operations on processed data
shifted_values = []
for i, val in enumerate(processed):
    if i % 2 == 0:
        shifted_values.append(val << 1)  # Left shift for even indices
    else:
        shifted_values.append(val >> 1)  # Right shift for odd indices

# Calculate advanced statistics
stats_value = compute_advanced_stats(shifted_values)

# Apply trigonometric transformation
trig_result = math.sin(stats_value) * math.cos(stats_value/2)

# Final calculation combining all previous results
final_result = int((trig_result * sum(shifted_values)) ** 1.5) % 1000

print(f'Result: {final_result}')