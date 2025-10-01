import math

def process_data(data):
    transformed = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            transformed.append(val ** 2)
        else:
            transformed.append(math.sqrt(val))
    return transformed

def aggregate_values(values):
    total = 0
    product = 1
    for v in values:
        total += v
        product *= v if v != 0 else 1
    return total, product

data_structure = {
    'group_a': [4, 9, 16, 25],
    'group_b': [36, 49, 64, 81],
    'metadata': {
        'scale_factor': 2.5,
        'offset': -3,
        'tags': ['even', 'odd', 'even', 'odd']
    }
}

# Step 1: Process group_a and group_b
processed_a = process_data(data_structure['group_a'])
processed_b = process_data(data_structure['group_b'])

# Step 2: Combine processed lists element-wise
combined = []
for i in range(len(processed_a)):
    combined.append(processed_a[i] + processed_b[i])

# Step 3: Apply metadata transformation
scaled_combined = [
    (val * data_structure['metadata']['scale_factor']) + data_structure['metadata']['offset']
    for val in combined
]

# Step 4: Aggregate values
sum_val, prod_val = aggregate_values(scaled_combined)

# Step 5: Final calculation using both aggregation results
intermediate = math.log(sum_val) if sum_val > 0 else 0
result = int(prod_val / (intermediate + 1))

print(f'Result: {result}')