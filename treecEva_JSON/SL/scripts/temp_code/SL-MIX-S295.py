import math

def process_nested_data(data):
    result = []
    for i, sublist in enumerate(data):
        temp = []
        for j, val in enumerate(sublist):
            if isinstance(val, int):
                transformed = (val ** 2) if val % 2 == 0 else math.factorial(val)
                temp.append(transformed)
            elif isinstance(val, str):
                temp.append(len(val) * (i + 1))
        result.append(sum(temp))
    return result

def apply_bitwise_operations(numbers):
    xor_result = 0
    for num in numbers:
        xor_result ^= num
    return xor_result

data_structure = [
    [2, 3, "hello"],
    [5, "world", 4, 1],
    ["test", 6, 7]
]

processed = process_nested_data(data_structure)
bitwise_result = apply_bitwise_operations(processed)

# Further transformations
a, b = divmod(bitwise_result, 7)
c = a & b
d = (c << 2) | (c >> 1) if c > 0 else 0

# Nested conditional logic
if d > 10:
    e = math.log(d, 2)
else:
    e = math.sqrt(abs(d)) * 2

f = round(e)
g = f ^ 0xF0
h = g & 0x0F

# Final computation sequence
i = h * 3
j = i - 5
k = j // 2 if j % 2 == 0 else (j + 1) // 2
l = k ** (1/3)
m = round(l)
n = m + 10
o = n & 0xFF

final_result = o
print(f'Result: {final_result}')