import math

def process_nested_data(data):
    total = 0
    for i, sublist in enumerate(data):
        if isinstance(sublist, list):
            for j, val in enumerate(sublist):
                if isinstance(val, (int, float)):
                    adjusted_val = val * (i + 1) * (j + 1)
                    if adjusted_val % 2 == 0:
                        total += adjusted_val
                    else:
                        total -= adjusted_val // 2
                elif isinstance(val, str):
                    numeric_part = ''.join(filter(str.isdigit, val))
                    if numeric_part:
                        num = int(numeric_part)
                        total += num if num % 3 == 0 else -num
    return total

def transform_with_formula(x, y, z):
    intermediate = (x ** 2 + y ** 2) / (abs(z) + 1)
    result = math.log(intermediate + 1) * math.sin(math.radians(45))
    return round(result, 4)

data_structure = [
    [12, "abc45def", 7.5],
    ["xyz90", 3, [4, "test15"]],
    [2.2, "num33", 8]
]

# Expand nested lists into main structure
expanded_data = []
for item in data_structure:
    if isinstance(item, list):
        expanded_data.extend(item)
    else:
        expanded_data.append(item)

processed_sum = process_nested_data([expanded_data])

a, b, c = 5, -3, 4
formula_result = transform_with_formula(a, b, c)

bitwise_combo = (a << 2) & (b | c) ^ (c >> 1)
conditional_factor = 1 if processed_sum > formula_result else -1

final_result = int((processed_sum + formula_result) * conditional_factor) ^ bitwise_combo
print(f'Result: {final_result}')