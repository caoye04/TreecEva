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

def compute_advanced_math(x, y, z):
    a = math.log(x) * math.sin(y)
    b = math.cos(z) ** 2
    c = math.sqrt(abs(a - b))
    return c

data_structure = [
    [1, 'hello', 3.5, 'world'],
    [2, 'test', 4, 'case'],
    [5, 'complex', 6, 'scenario']
]

processed_data = process_nested_data(data_structure)
math_result = compute_advanced_math(10, math.pi/4, math.pi/6)

# Manipulate strings
strings_list = ['alpha', 'beta', 'gamma', 'delta']
concatenated = ''.join(strings_list)
char_sum = sum(ord(c) for c in concatenated)

# Bitwise operations
bitwise_result = (char_sum & 0xFF) | (processed_data[0] << 2)

# Final calculation
final_result = int(math_result * bitwise_result) % 1000

print(f'Result: {final_result}')