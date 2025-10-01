import math

def process_data(arr):
    transformed = []
    for i in range(len(arr)):
        if i % 2 == 0:
            transformed.append(arr[i] ** 2)
        else:
            transformed.append(math.sqrt(abs(arr[i])))
    return transformed

def aggregate_values(data):
    total = 0
    for val in data:
        if isinstance(val, int) and val > 10:
            total += val
        elif isinstance(val, float):
            total += int(val)
    return total

data_matrix = [
    [3, -16, 5, 64, -2],
    [7, 9, 4, -25, 11],
    [2, 81, -3, 16, 5]
]

processed_rows = []
for row in data_matrix:
    processed_row = process_data(row)
    processed_rows.append(processed_row)

flattened = []
for row in processed_rows:
    for item in row:
        flattened.append(item)

filtered_values = [x for x in flattened if x >= 0 and (isinstance(x, int) or x.is_integer())]

aggregated_sum = aggregate_values(filtered_values)

binary_string = bin(aggregated_sum)[2:]  # Remove '0b' prefix

bitwise_result = 0
for i, bit in enumerate(reversed(binary_string)):
    if bit == '1':
        bitwise_result ^= (i << 2) + 1

factorial_base = 1
for i in range(1, 6):
    factorial_base *= i

final_result = (bitwise_result & factorial_base) | (aggregated_sum >> 2)
print(f'Result: {final_result}')