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

def apply_bitwise_operations(numbers):
    xor_result = 0
    for num in numbers:
        xor_result ^= num
    return xor_result

data_structure = [
    [3, 'hello', 2.5, 4],
    ['world', 5, None, 7],
    [1, 'a'*6, 9, 'test']
]

processed_data = process_nested_data(data_structure)
bitwise_result = apply_bitwise_operations(processed_data)

# Perform advanced mathematical operations
log_val = math.log(bitwise_result + 10)
sin_val = math.sin(log_val)
cos_val = math.cos(log_val * 2)

# Complex calculation chain
intermediate_result = (bitwise_result * log_val) // 3
final_adjustment = (sin_val + cos_val) * 100
final_result = int(intermediate_result + final_adjustment)

print(f'Result: {final_result}')