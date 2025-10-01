import math

def process_nested_data(data):
    total = 0
    for i, sublist in enumerate(data):
        if i % 2 == 0:
            for val in sublist:
                total += val * (i + 1)
        else:
            for j, val in enumerate(sublist):
                if j % 2 != 0:
                    total -= val << (j // 2)
    return total

def transform_string(s):
    parts = s.split('_')
    transformed = []
    for part in parts:
        if len(part) > 3:
            transformed.append(part[::-1].upper())
        else:
            transformed.append(part.lower() * 2)
    return ''.join(transformed)

data_structure = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9],
    [10, 11, 12, 13, 14],
    [15, 16, 17]
]

string_input = "hello_world_python_code_test"

numeric_result = process_nested_data(data_structure)
transformed_str_length = len(transform_string(string_input))

angle_rad = math.pi / 4
trig_component = int(math.sin(angle_rad) * 1000) ^ int(math.cos(angle_rad) * 1000)

base_value = numeric_result & 0xFF
shifted_value = base_value << 3
masked_value = shifted_value | 0x07

conditional_result = masked_value if (transformed_str_length % 2 == 0) else (~masked_value & 0xFF)
log_value = int(math.log(conditional_result + 1) * 100)

complex_expr = ((conditional_result * 3) + (log_value >> 2) - (trig_component & 0xF)) % 256
final_result = complex_expr ^ 0xAA

print(f"Result: {final_result}")