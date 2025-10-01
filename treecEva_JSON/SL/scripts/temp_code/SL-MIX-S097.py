import math

def process_nested_data(data):
    result = 0
    for i, sublist in enumerate(data):
        if i % 2 == 0:
            for j, val in enumerate(sublist):
                if j % 3 == 0:
                    result += val * (i + 1)
        else:
            temp = [x for x in sublist if x > 0]
            if temp:
                result -= max(temp) // len(temp)
    return result

def compute_transformed_value(base, exp, mod):
    if base <= 0 or exp <= 0:
        return 0
    transformed = (base ** exp) % mod
    return transformed

data_structure = [
    [1, -2, 3, 4, -5, 6, 7],
    [8, -9, 10, 11],
    [-12, 13, -14, 15, 16, -17, 18, 19],
    [20, -21, 22]
]

# Initial processing
processed_value = process_nested_data(data_structure)

# Mathematical transformation
transformed_value = compute_transformed_value(processed_value, 3, 100)

# String manipulation component
stringified = str(transformed_value)
reversed_string = stringified[::-1]
char_sum = sum(ord(c) for c in reversed_string)

# Bitwise operations
bitwise_result = (char_sum & 0xFF) | (transformed_value << 2)

# Final calculation
final_result = (bitwise_result ^ (len(stringified) * 17)) + int(math.sqrt(processed_value))

print(f'Result: {final_result}')