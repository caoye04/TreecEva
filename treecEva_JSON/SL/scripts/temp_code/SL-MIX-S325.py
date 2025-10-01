import math

def complex_transform(data_list):
    transformed = []
    for i, val in enumerate(data_list):
        if i % 3 == 0:
            transformed.append(val ** 2)
        elif i % 3 == 1:
            transformed.append(math.sqrt(abs(val)))
        else:
            transformed.append(val * -1)
    return transformed

def aggregate_metrics(values):
    product = 1
    sum_vals = 0
    count = 0
    for v in values:
        if v > 0:
            product *= v
            sum_vals += v
            count += 1
    avg = sum_vals / count if count > 0 else 0
    return product, avg, count

data = [4, -9, 16, 25, -36, 49, 64, -81, 100]
stage1 = complex_transform(data)
stage2 = [round(x) for x in stage1 if isinstance(x, float) or x == int(x)]

# Perform bit shifting operations on even indices
for i in range(len(stage2)):
    if i % 2 == 0 and stage2[i] > 0:
        stage2[i] = stage2[i] << 1
    elif i % 2 == 1 and stage2[i] > 0:
        stage2[i] = stage2[i] >> 1

# Apply modulo operation with a prime number
prime = 17
stage3 = [x % prime for x in stage2]

# Calculate final metrics
product_result, average_result, count_result = aggregate_metrics(stage3)

# Final calculation combining all metrics
final_result = int((product_result ** (1/3)) + (average_result * count_result) - len(stage3))

print(f'Result: {final_result}')