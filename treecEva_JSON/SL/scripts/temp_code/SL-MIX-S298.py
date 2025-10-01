import math

def complex_transform(data):
    transformed = []
    for i, val in enumerate(data):
        if i % 3 == 0:
            transformed.append(val ** 2)
        elif i % 3 == 1:
            transformed.append(math.sqrt(abs(val)))
        else:
            transformed.append(math.log(abs(val) + 1))
    return transformed

def aggregate_operations(values):
    product = 1
    sum_val = 0
    xor_result = 0
    for v in values:
        product *= v if v != 0 else 1
        sum_val += v
        xor_result ^= int(v * 1000)  # Scale to avoid float issues
    return product, sum_val, xor_result

data_structure = {
    'layer1': [
        {'a': 2, 'b': [3, 5, 7]},
        {'a': -4, 'b': [11, 13, 17]},
        {'a': 6, 'b': [19, 23, 29]}
    ],
    'layer2': [
        [2, 4, 8],
        [16, 32, 64],
        [128, 256, 512]
    ],
    'layer3': [
        "hello",
        "world",
        "test"
    ]
}

# Phase 1: Extract and transform numerical data
numerical_sequence = []
for item in data_structure['layer1']:
    numerical_sequence.extend(item['b'])
    numerical_sequence.append(item['a'])

transformed_data = complex_transform(numerical_sequence)

# Phase 2: Process layer2 arrays
layer2_aggregates = []
for arr in data_structure['layer2']:
    prod, sum_val, xor_val = aggregate_operations(arr)
    layer2_aggregates.append((prod, sum_val, xor_val))

# Phase 3: String processing
string_lengths = [len(s) for s in data_structure['layer3']]
char_code_sum = sum(ord(c) for s in data_structure['layer3'] for c in s)

# Phase 4: Complex calculation using all processed data
aggregate_product = 1
aggregate_sum = 0
for prod, sum_val, _ in layer2_aggregates:
    aggregate_product *= prod
    aggregate_sum += sum_val

transformed_sum = sum(transformed_data)

# Final computation
result = (
    int(aggregate_product % 1000) +
    int(transformed_sum) +
    (char_code_sum & 0xFF) +
    (string_lengths[0] << 2) +
    (aggregate_sum % 100)
)

print(f"Result: {result}")