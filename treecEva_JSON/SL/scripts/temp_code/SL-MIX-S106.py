import math

def process_nested_data(data):
    result = 0
    for i, sublist in enumerate(data):
        sub_result = 1
        for j, val in enumerate(sublist):
            if isinstance(val, int) and val > 0:
                sub_result *= val
            elif isinstance(val, str):
                sub_result *= len(val)
            elif isinstance(val, float):
                sub_result *= int(math.floor(val))
        result += sub_result if i % 2 == 0 else -sub_result
    return result

def transform_dict(d):
    new_dict = {}
    for k, v in d.items():
        if isinstance(v, list):
            new_dict[k] = sum(v)
        elif isinstance(v, dict):
            new_dict[k] = transform_dict(v)
        else:
            new_dict[k] = v * 2
    return new_dict

data_structure = [
    [2, "hello", 3.7, -1],
    [4, "world", 2.1],
    [1, 2, {"a": [3, 4], "b": 5}]
]

# Process the nested list
intermediate_value = process_nested_data(data_structure[:2])

# Transform the last element
if isinstance(data_structure[2][2], dict):
    modified_dict = transform_dict(data_structure[2][2])
    dict_sum = sum(modified_dict.values())
else:
    dict_sum = 0

# Bitwise operations
bitwise_result = (intermediate_value << 2) ^ dict_sum

# Mathematical operations
log_val = math.log(abs(bitwise_result)) if bitwise_result != 0 else 0
exp_val = math.exp(log_val % 3) if log_val > 0 else 1

# Final calculation
final_result = int(exp_val * 100) & 0xFF

print(f"Result: {final_result}")