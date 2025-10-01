import math

def process_data(data):
    result = []
    for i, sublist in enumerate(data):
        temp = []
        for j, val in enumerate(sublist):
            if isinstance(val, str):
                temp.append(len(val) * (i + 1))
            elif isinstance(val, int):
                temp.append(val ** (j + 1))
            elif isinstance(val, float):
                temp.append(round(math.sqrt(val), 2))
        result.append(temp)
    return result

def aggregate_values(processed_data):
    totals = []
    for sublist in processed_data:
        total = 0
        for val in sublist:
            total += val if isinstance(val, int) else int(val)
        totals.append(total)
    return totals

data = [
    ["hello", 2, 9.0, "world"],
    [3, "test", 4.0, 5],
    ["a", "bb", 3, 2.25]
]

processed = process_data(data)
aggregated = aggregate_values(processed)

# Bitwise operations and mathematical transformations
x = aggregated[0] << 1
y = aggregated[1] >> 1
z = aggregated[2] & 0xF

# Complex calculation using x, y, z
intermediate = (x * y) + (z ^ 0xA) - int(math.log10(max(aggregated)) * 10)

# Final result computation
final_result = (intermediate % 7) ** 3 + sum([ord(c) for c in hex(intermediate)[-3:] if c.isdigit()])

print(f"Result: {final_result}")