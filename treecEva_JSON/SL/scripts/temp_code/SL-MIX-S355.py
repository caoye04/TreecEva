import math

def process_data(data):
    processed = []
    for item in data:
        if isinstance(item, dict):
            temp = 0
            for k, v in item.items():
                if isinstance(v, list):
                    temp += sum(v)
                elif isinstance(v, int):
                    temp += v * 2
            processed.append(temp)
        elif isinstance(item, list):
            inner_sum = 0
            for elem in item:
                if isinstance(elem, str):
                    inner_sum += len(elem)
                elif isinstance(elem, (int, float)):
                    inner_sum += elem ** 2
            processed.append(inner_sum)
    return processed

data_container = [
    {'a': [1, 2, 3], 'b': 5},
    [4, 'hello', 2.5],
    {'x': [10, 20], 'y': 7, 'z': [1, 1, 1]},
    ['world', 3, 4.0]
]

processed_values = process_data(data_container)

# Step 1: Apply transformation using lambda and map
transformed = list(map(lambda x: x * 2 if x % 2 == 0 else x + 5, processed_values))

# Step 2: Bitwise operations
bitwise_results = []
for i in range(len(transformed)):
    val = transformed[i]
    if i % 2 == 0:
        # Even index: left shift by 1
        bitwise_results.append(val << 1)
    else:
        # Odd index: XOR with 0xF
        bitwise_results.append(val ^ 0xF)

# Step 3: Mathematical computations
math_computed = []
for idx, num in enumerate(bitwise_results):
    if idx == 0:
        math_computed.append(math.sqrt(num))
    elif idx == 1:
        math_computed.append(math.log(num + 1))
    elif idx == 2:
        math_computed.append(math.sin(num))
    else:
        math_computed.append(math.cos(num))

# Final aggregation
aggregated = sum([int(x) for x in math_computed])

# Conditional assignment based on aggregated value
if aggregated > 50:
    adjustment = 10
elif aggregated > 20:
    adjustment = 5
else:
    adjustment = 1

final_result = (aggregated + adjustment) * 3 - 7
print(f'Result: {final_result}')