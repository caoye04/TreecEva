import math

def process_data(data):
    processed = []
    for item in data:
        if isinstance(item, int):
            processed.append(item ^ 0xF)
        elif isinstance(item, str):
            num_val = sum(ord(c) for c in item)
            processed.append(num_val & 0xFF)
        else:
            processed.append(len(str(item)))
    return processed

data_structure = [
    [15, 'hello', 3.14],
    {'a': 42, 'b': 'world'},
    (7, 8, 9)
]

# Flatten and transform data
flat_list = []
for element in data_structure:
    if isinstance(element, list):
        flat_list.extend(process_data(element))
    elif isinstance(element, dict):
        flat_list.extend(process_data(list(element.values())))
    elif isinstance(element, tuple):
        flat_list.extend([x << 1 for x in element])

# Perform mathematical operations
intermediate_sum = sum(flat_list)
log_val = math.log(intermediate_sum, 2)
rounded_log = round(log_val)

# Bitwise and string operations
bitwise_combo = (rounded_log & 0x1F) | (len(flat_list) << 2)
char_code_sum = sum(ord(c) for c in f"result_{bitwise_combo}")

# Final calculation
final_result = (char_code_sum * 3) % (bitwise_combo + 7)
print(f'Result: {final_result}')