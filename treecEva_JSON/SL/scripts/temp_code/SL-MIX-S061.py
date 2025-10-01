import math

def process_data(data):
    result = []
    for i, sublist in enumerate(data):
        transformed = []
        for j, val in enumerate(sublist):
            if isinstance(val, int):
                transformed.append((val ** 2) % (j + 2))
            elif isinstance(val, str):
                transformed.append(len(val) * (i + 1))
            else:
                transformed.append(0)
        result.append(transformed)
    return result

data_matrix = [
    [3, 'hello', 7.2, 4],
    ['world', 5, None, 2.8],
    [1, 'test', 9, 'example']
]

processed = process_data(data_matrix)

# Flatten processed list and calculate sum of squares
flattened = [item for sublist in processed for item in sublist]
sum_of_squares = sum(x**2 for x in flattened if isinstance(x, int))

# Perform modular exponentiation
mod_exp_result = pow(sum_of_squares, 3, 1000)

# Bitwise operations
bitwise_and = mod_exp_result & 0xFF
bitwise_or = mod_exp_result | 0xF0
xor_result = bitwise_and ^ bitwise_or

# Trigonometric adjustment
angle_rad = math.radians(xor_result % 90)
sin_val = math.sin(angle_rad)
adjusted = round(sin_val * 1000)

# Final calculation sequence
final_result = ((adjusted << 2) + (xor_result >> 1)) % 1000
print(f'Result: {final_result}')