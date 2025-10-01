import math

def process_nested_data(data):
    result = 0
    for i, sublist in enumerate(data):
        if i % 2 == 0:
            for j, val in enumerate(sublist):
                if j % 3 == 0:
                    result += val * (i + 1)
                elif j % 3 == 1:
                    result -= val // (i + 1)
                else:
                    result ^= val
        else:
            temp = [x for x in sublist if x > 0]
            if temp:
                result += max(temp) * len(temp)
    return result

def transform_string(s):
    parts = s.split('_')
    transformed = []
    for part in parts:
        if len(part) % 2 == 0:
            transformed.append(part[::-1])
        else:
            transformed.append(part.upper())
    return ''.join(transformed)

def calculate_expression(a, b, c):
    return (a ** 2 + b * c - math.log(abs(c) + 1)) / (a + b + 1)

data_structure = [
    [12, -5, 8, 15, -3, 20],
    [7, -2, 14, 0, 9],
    [3, 6, -9, 12, 15, -18, 21],
    [-4, 11, -8, 13, 5]
]

string_input = "hello_world_python_programming"

processed_data = process_nested_data(data_structure)
transformed_string = transform_string(string_input)
char_sum = sum(ord(c) for c in transformed_string)

x = 5
y = -3
z = 7

expr_result = calculate_expression(x, y, z)

bitwise_combo = (x << 2) & (y | z) ^ (x + y + z)

conditional_val = 0
if processed_data > 100:
    conditional_val = processed_data * 2
elif processed_data > 50:
    conditional_val = processed_data + 50
else:
    conditional_val = processed_data - 20

final_result = int(expr_result * conditional_val + char_sum + bitwise_combo)

print(f"Result: {final_result}")