import math

def process_nested_data(data):
    result = 0
    for i, sublist in enumerate(data):
        if i % 2 == 0:
            for j, val in enumerate(sublist):
                if j % 3 == 0:
                    result += math.factorial(val)
                elif j % 3 == 1:
                    result -= val ** 2
                else:
                    result *= val if val != 0 else 1
        else:
            temp = [x for x in sublist if x > 0]
            result += sum(temp) if temp else 0
    return result

def transform_string(s):
    mapping = {chr(i): i-96 for i in range(97, 123)}  # a=1, b=2, ..., z=26
    total = 0
    for char in s.lower():
        if char in mapping:
            total += mapping[char]
        else:
            total -= 1
    return total

data_structure = [
    [1, 2, 3, 4, 5],
    [6, -2, 8, 0, 10],
    [2, 3, 1, 4],
    [-1, -2, -3],
    [5, 0, 2, 3, 1, 4]
]

string_value = "Complexity"

# Phase 1: Process data structure
processed_value = process_nested_data(data_structure)

# Phase 2: Transform string
transformed_value = transform_string(string_value)

# Phase 3: Mathematical operations
angle_rad = math.pi / 4
sin_val = math.sin(angle_rad)
cos_val = math.cos(angle_rad)
trig_result = int((sin_val ** 2 + cos_val ** 2) * 1000)  # Should be 1000

# Phase 4: Bitwise operations
bitwise_a = processed_value & 0xFF
bitwise_b = transformed_value | 0xF0
bitwise_result = bitwise_a ^ bitwise_b

# Phase 5: Final calculation sequence
step1 = processed_value + transformed_value
step2 = step1 * trig_result
step3 = step2 - bitwise_result
step4 = step3 // 7
final_result = step4 % 1000  # TARGET ASSIGNMENT

print(f"Result: {final_result}")