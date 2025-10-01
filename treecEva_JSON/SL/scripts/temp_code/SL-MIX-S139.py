import math

def process_nested_data(data):
    result = []
    for i, sublist in enumerate(data):
        temp = []
        for j, val in enumerate(sublist):
            if isinstance(val, str):
                temp.append(len(val) * (i + 1))
            elif isinstance(val, int):
                temp.append(val ** (j + 1))
            else:
                temp.append(int(val))
        result.append(sum(temp) % 7)
    return result

data_structure = [
    ["hello", 2, 3.5],
    [4, "world", 2.2, True],
    ["a", "bb", "ccc", 5, False]
]

processed = process_nested_data(data_structure)

# Perform advanced calculations
x = sum(processed) * 3
y = math.factorial(len(processed))
z = x ** 2 - y

if z > 100:
    final_result = z // 10 + len(str(z))
else:
    sqrt_z = math.isqrt(abs(z)) if z >= 0 else 0
    final_result = sqrt_z + (z % 7)

print(f'Result: {final_result}')