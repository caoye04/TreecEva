import math

def process_nested_data(data):
    result = 0
    for key, value in data.items():
        if isinstance(value, dict):
            result += process_nested_data(value)
        elif isinstance(value, list):
            for i, item in enumerate(value):
                if isinstance(item, (int, float)):
                    result += item * (i + 1)
                elif isinstance(item, str):
                    result += len(item) * (-1 if key.startswith('neg') else 1)
        elif isinstance(value, (int, float)):
            result += value if value > 0 else value * -2
    return result

def transform_string(s, shifts):
    result = ''
    for i, char in enumerate(s):
        shift = shifts[i % len(shifts)]
        new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        result += new_char
    return result

def calculate_weighted_sum(matrix):
    total = 0
    for i, row in enumerate(matrix):
        row_sum = sum(row)
        total += row_sum * (i + 1)
        if i % 2 == 1:  # For odd-indexed rows, apply additional transformation
            total -= max(row) * 2
    return total

data_structure = {
    'level1_a': {
        'level2_a': [10, -5, 'hello', 3.14],
        'level2_b': 42,
        'neg_level2_c': ['test', 7, -2.5]
    },
    'level1_b': [20, 'world', -15, 8],
    'level1_c': -100
}

# Process the nested data structure
processed_value = process_nested_data(data_structure)

# Transform a string using a shifting pattern
secret_message = transform_string('python', [1, 3, 2, 4, 5, 6])

# Calculate a weighted sum from a matrix
matrix_data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]
matrix_sum = calculate_weighted_sum(matrix_data)

# Perform a series of mathematical operations
a = processed_value
b = len(secret_message)  # Should be 6
c = matrix_sum

d = math.pow(a, 1/3)  # Cube root of a
if d > 0:
    e = math.floor(d)
else:
    e = math.ceil(d)

f = b * c + e

g = f % 17
h = math.log(abs(g) + 1) if g != 0 else 1

# Bitwise operations
i = int(h) & 0xF  # Lower 4 bits
j = i << 2  # Left shift by 2

# Final calculation combining all previous results
final_result = (j ^ 0xA) + int(math.sqrt(abs(processed_value)))

print(f'Result: {final_result}')