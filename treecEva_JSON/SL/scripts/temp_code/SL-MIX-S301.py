import math

def process_nested_data(data):
    result = []
    for i, sublist in enumerate(data):
        temp = []
        for j, val in enumerate(sublist):
            if isinstance(val, int):
                temp.append((val ** 2) + (i * j))
            elif isinstance(val, str):
                temp.append(len(val) * (i + 1))
            else:
                temp.append(0)
        result.append(sum(temp))
    return result

data_structure = [
    [3, "hello", 2.5, 7],
    ["world", 5, "test"],
    [1, 2, "a", "bb", 9]
]

processed = process_nested_data(data_structure)

# Perform mathematical transformations
transformed = []
for idx, value in enumerate(processed):
    if idx % 2 == 0:
        transformed.append(math.sqrt(value) if value >= 0 else 0)
    else:
        transformed.append(math.log(value) if value > 0 else 0)

# Aggregate results using bitwise and arithmetic operations
aggregate = 0
for i, t_val in enumerate(transformed):
    bit_shift = i & 3  # Bitwise AND to limit shift amount
    shifted = int(t_val) << bit_shift if t_val >= 0 else int(t_val) >> abs(bit_shift)
    aggregate ^= shifted  # XOR aggregation

# Final adjustment with trigonometric function
final_result = round(aggregate * math.sin(math.radians(45)))

print(f"Result: {final_result}")