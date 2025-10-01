import math

def process_data(lst):
    transformed = []
    for i, val in enumerate(lst):
        if i % 2 == 0:
            transformed.append(val ** 2)
        else:
            transformed.append(math.sqrt(abs(val)))
    return transformed

data = [4, -9, 5, -16, 7]
processed = process_data(data)

# Nested dictionary with lambda transformations
transform_ops = {
    'exp': lambda x: math.exp(x / 10),
    'log': lambda x: math.log(x + 1) if x > 0 else 0,
    'bitwise': lambda x: int(x) & 0xF
}

nested_structure = {
    'level1': {
        'level2a': {
            'values': processed[:3],
            'ops': ['exp', 'log', 'bitwise']
        },
        'level2b': {
            'values': processed[3:],
            'ops': ['log', 'exp', 'exp']
        }
    }
}

accumulated = 0
for level_key, level_val in nested_structure.items():
    for sub_key, sub_val in level_val.items():
        values = sub_val['values']
        ops = sub_val['ops']
        for i in range(len(values)):
            op_func = transform_ops[ops[i]]
            transformed_val = op_func(values[i])
            accumulated += transformed_val

# Bitwise and arithmetic combination
mask = 0xFF
shifted_accum = int(accumulated * 1000) >> 2
masked_value = shifted_accum & mask

# Final calculation sequence
final_result = ((masked_value ^ 0xAA) + 17) * 3 - (math.floor(math.sqrt(masked_value)) << 1)
print(f"Result: {final_result}")