import math

def complex_transform(data_dict):
    result = []
    for key, values in data_dict.items():
        transformed = []
        for i, val in enumerate(values):
            if i % 2 == 0:
                transformed.append(val ** 2)
            else:
                transformed.append(math.sqrt(abs(val)))
        result.append(sum(transformed))
    return result

def process_nested(nested_list):
    flattened = []
    for sublist in nested_list:
        if isinstance(sublist, list):
            flattened.extend(process_nested(sublist))
        else:
            flattened.append(sublist)
    return flattened

data = {
    'alpha': [3, -4, 5],
    'beta': [2, -9, 16, -25],
    'gamma': [-1, 4, -9, 16, -25]
}

# Stage 1: Transform data
stage1 = complex_transform(data)

# Stage 2: Create nested structure
nested = [[stage1[0], [stage1[1], stage1[2]]], stage1[0] + stage1[1] + stage1[2]]

# Stage 3: Flatten nested structure
flattened = process_nested(nested)

# Stage 4: Bitwise and mathematical operations
bitwise_sum = 0
for i in range(len(flattened)):
    if i < len(flattened) - 1:
        bitwise_sum += int(flattened[i]) & int(flattened[i+1])

# Stage 5: Trigonometric adjustments
trig_adjustment = 0
for val in flattened:
    trig_adjustment += math.sin(val) * 100

# Stage 6: Final computation
final_result = (bitwise_sum * 3) + int(trig_adjustment) - sum([x for x in flattened if x > 50])

# END OF COMPUTATION
print(f"Result: {final_result}")