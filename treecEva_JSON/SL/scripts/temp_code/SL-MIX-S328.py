import math

def process_nested_data(data_structure):
    result = 0
    for i, sublist in enumerate(data_structure):
        sub_result = 1
        for j, value in enumerate(sublist):
            if i % 2 == 0:
                sub_result *= value if value != 0 else 1
            else:
                sub_result += value
        if i % 3 == 0:
            result ^= sub_result
        elif i % 3 == 1:
            result |= sub_result
        else:
            result &= sub_result
    return result

def transform_string(s):
    transformed = ''
    for i, char in enumerate(s):
        if i % 3 == 0:
            transformed += char.upper()
        elif i % 3 == 1:
            transformed += str(ord(char) % 10)
        else:
            transformed += char.lower()
    return transformed

data = [
    [2, 3, 0, 5],
    [1, 4, 2],
    [6, 0, 3, 1, 2],
    [2, 2, 2, 2, 2, 2],
    [5, 1, 0, 3]
]

string_data = "ComplexDataProcessing"

# First processing step
processed_value = process_nested_data(data)

# String transformation
transformed_string = transform_string(string_data)

# Calculate ASCII sum of transformed string
ascii_sum = sum(ord(c) for c in transformed_string)

# Mathematical operations
log_value = math.log(ascii_sum, 2)
exp_mod = (math.exp(log_value % 3) * 100) // 1

# Bitwise operations with processed values
shift_amount = processed_value % 5
bitwise_result = (int(exp_mod) << shift_amount) & 0xFF

# Final complex calculation
final_result = ((bitwise_result ^ 0xAA) + processed_value * 3) % 1000

print(f"Result: {final_result}")