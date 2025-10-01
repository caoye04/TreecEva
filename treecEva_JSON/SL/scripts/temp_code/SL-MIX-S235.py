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

def calculate_weighted_sum(values, weights):
    total = 0
    for i in range(len(values)):
        total += values[i] * weights[i % len(weights)]
    return total

data_structure = [
    [1, 'hello', 3.5, 2],
    ['world', 4, None, 5],
    [6, 'test', 7, 'a']
]

weights = [0.5, 1.5, 2.0]

processed_data = process_nested_data(data_structure)
weighted_sum = calculate_weighted_sum(processed_data, weights)

x = math.log(weighted_sum, 2)
y = int(x) ^ 0b1010  # XOR with binary 1010 (decimal 10)
z = (y << 2) + 0xF   # Left shift by 2 and add hexadecimal F (decimal 15)

a = ~z & 0xFF        # Bitwise NOT and mask with 0xFF
b = abs(a - 42)
c = (b // 3) * 7

d = c % 17
e = d ** 3
f = math.sqrt(e) if e > 0 else 0

g = round(f)
h = g | 0x0F         # Bitwise OR with hexadecimal 0F (decimal 15)

sequence = [h, h+1, h+2, h+3, h+4]
transformed = list(map(lambda n: n**2 if n%2==0 else n**3, sequence))
final_result = sum(transformed) - (h << 3)  # Subtract h shifted left by 3

print(f"Result: {final_result}")