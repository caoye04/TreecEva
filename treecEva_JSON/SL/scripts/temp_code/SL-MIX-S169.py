import math

def process_data(arr):
    result = []
    for i in range(len(arr)):
        if isinstance(arr[i], list):
            sub_sum = sum(process_data(arr[i]))
            result.append(sub_sum)
        else:
            result.append(arr[i] ** 2)
    return result

data = [
    [1, 2, [3, 4]],
    [5, [6, [7, 8]], 9],
    10
]

processed = process_data(data)
flattened = []
for item in processed:
    if isinstance(item, list):
        flattened.extend(item)
    else:
        flattened.append(item)

mapped_values = list(map(lambda x: x * math.log(x + 1) if x > 0 else 0, flattened))
filtered_values = [x for x in mapped_values if x > 10]
sorted_values = sorted(filtered_values, reverse=True)

if len(sorted_values) >= 3:
    selected = sorted_values[:3]
else:
    selected = sorted_values + [0] * (3 - len(sorted_values))

weighted_sum = sum([selected[i] * (i + 1) for i in range(len(selected))])
bitwise_ops = (int(weighted_sum) & 0xFF) | ((int(weighted_sum) >> 8) ^ 0xAA)
final_result = bitwise_ops % 1000
print(f"Result: {final_result}")