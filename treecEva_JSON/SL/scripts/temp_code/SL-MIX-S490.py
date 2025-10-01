import math

def process_data(arr):
    transformed = []
    for i, val in enumerate(arr):
        if i % 2 == 0:
            transformed.append(val ** 2)
        else:
            transformed.append(math.sqrt(abs(val)))
    return transformed

data = [4, -9, 16, -25, 36]
processed = process_data(data)

# Nested dictionary with lambda transformations
ops = {
    'add': lambda x, y: x + y,
    'multiply': lambda x, y: x * y,
    'power': lambda x, y: x ** y,
    'aggregate': {
        'sum_all': lambda lst: sum(lst),
        'product_all': lambda lst: math.prod(lst)
    }
}

# Perform sequential operations using processed data
interim_a = ops['add'](processed[0], processed[1])
interim_b = ops['multiply'](interim_a, processed[2])
interim_c = ops['power'](interim_b, 1/3)  # Cube root

# Aggregate operations
sum_total = ops['aggregate']['sum_all'](processed)
product_total = ops['aggregate']['product_all'](processed)

# Conditional logic based on intermediate results
if sum_total > product_total:
    final_result = ops['add'](interim_c, sum_total)
else:
    adjusted_values = [v + 10 for v in processed]
    adjusted_sum = ops['aggregate']['sum_all'](adjusted_values)
    final_result = ops['multiply'](interim_c, adjusted_sum)

print(f'Result: {int(final_result)}')