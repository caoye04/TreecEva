import math

def process_nested_data(data):
    result = []
    for i, sublist in enumerate(data):
        temp = []
        for j, val in enumerate(sublist):
            if isinstance(val, int) and val > 0:
                temp.append((val ** 2) ^ (i + 1))
            elif isinstance(val, str):
                temp.append(len(val) * (j + 1))
            else:
                temp.append(0)
        result.append(sum(temp))
    return result

def calculate_weighted_sum(values, weights):
    return sum(v * w for v, w in zip(values, weights))

def transform_and_aggregate(matrix):
    intermediate = []
    for row in matrix:
        transformed = [math.log(x + 1) if x > 0 else 0 for x in row]
        intermediate.append(sum(transformed))
    return math.floor(sum(intermediate) * 100)

# Main execution starts here
nested_data = [
    [3, 'hello', -2, 'world'],
    ['test', 5, 0, 'a'],
    [7, 'python', 2, 'code']
]

weights = [0.5, 1.5, 2.0]

processed_data = process_nested_data(nested_data)
weighted_sum = calculate_weighted_sum(processed_data, weights)

matrix_data = [
    [weighted_sum % 10, weighted_sum // 10],
    [weighted_sum & 15, weighted_sum | 7]
]

aggregated_value = transform_and_aggregate(matrix_data)

# Bitwise manipulation and final calculation
x = (aggregated_value << 2) & 255
y = (x ^ 170) + 42
final_result = (y * 3) % 1000

print(f'Result: {final_result}')