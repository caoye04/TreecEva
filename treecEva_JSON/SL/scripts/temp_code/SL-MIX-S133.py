import math

def process_data(data):
    processed = []
    for item in data:
        if isinstance(item, dict):
            temp = sum(v for v in item.values() if isinstance(v, int))
            processed.append(temp)
        elif isinstance(item, list):
            temp = 1
            for x in item:
                if isinstance(x, int):
                    temp *= x
            processed.append(temp)
        elif isinstance(item, tuple):
            temp = 0
            for i, x in enumerate(item):
                if isinstance(x, int):
                    temp += x * (i + 1)
            processed.append(temp)
    return processed

def transform_values(lst):
    transformed = []
    for val in lst:
        if val % 2 == 0:
            transformed.append(val // 2)
        else:
            transformed.append(val * 3 + 1)
    return transformed

data_structure = [
    {'a': 5, 'b': 10, 'c': 'hello'},
    [2, 3, 4],
    (1, 2, 3, 4),
    {'x': 7, 'y': 14},
    [5, 0, 2],
    (10, 20),
    {'m': 3, 'n': 9, 'o': 12}
]

# First transformation
step_one = process_data(data_structure)

# Second transformation
step_two = transform_values(step_one)

# Third transformation: apply mathematical operations
step_three = []
for idx, num in enumerate(step_two):
    if idx % 2 == 0:
        step_three.append(math.sqrt(num) if num >= 0 else 0)
    else:
        step_three.append(math.log(num) if num > 0 else 0)

# Fourth transformation: aggregate and manipulate
aggregate = sum(step_three)

# Final complex calculation
x = int(aggregate)
y = x & 0xFF  # Bitwise AND with 255
z = y ^ 0xAA  # XOR with 170
w = z << 2    # Left shift by 2

final_result = w + (x % 17)
print(f"Result: {final_result}")