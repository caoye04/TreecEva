import math

def process_nested_data(data):
    result = []
    for i, sublist in enumerate(data):
        temp = []
        for j, val in enumerate(sublist):
            if isinstance(val, int):
                temp.append((val ** 2) % (j + 2))
            elif isinstance(val, str):
                temp.append(len(val) * (i + 1))
            else:
                temp.append(0)
        result.append(sum(temp))
    return result

def compute_advanced_stats(numbers):
    if not numbers:
        return 0
    squares = [x**2 for x in numbers]
    mean_of_squares = sum(squares) / len(squares)
    geometric_mean = math.prod(numbers)**(1/len(numbers)) if all(x > 0 for x in numbers) else 0
    return round(mean_of_squares - geometric_mean)

# Main logic starts here
matrix_data = [
    [3, 'hello', 7, 'a'],
    ['world', 5, 2],
    [1, 2, 'test', 9, 4]
]

processed_values = process_nested_data(matrix_data)
stats_value = compute_advanced_stats([x for x in processed_values if x > 0])

# Bitwise manipulations
bitwise_combo = (processed_values[0] << 2) ^ (processed_values[2] & 0xF) | stats_value

# Final computation sequence
accumulator = 0
for idx in range(len(processed_values)):
    term = ((processed_values[idx] + idx) * (bitwise_combo >> idx)) % (idx + 5)
    accumulator += term

final_modifier = math.floor(math.sqrt(accumulator)) if accumulator > 0 else 1
final_result = (bitwise_combo * stats_value + accumulator) // final_modifier

print(f'Result: {final_result}')