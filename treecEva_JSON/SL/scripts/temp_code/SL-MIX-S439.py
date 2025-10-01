import math

def process_data(data):
    result = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            result.append(val ** 2)
        else:
            result.append(math.sqrt(val))
    return result

def aggregate_values(values):
    total = 0
    for v in values:
        if v > 10:
            total += v // 3
        else:
            total += v * 2
    return total

data_structure = {
    'group1': [4, 9, 16, 25, 36],
    'group2': [49, 64, 81, 100, 121],
    'metadata': {
        'scale': 2,
        'offset': 5,
        'flags': [True, False, True]
    }
}

# Step 1: Process group1 and group2
processed_group1 = process_data(data_structure['group1'])
processed_group2 = process_data(data_structure['group2'])

# Step 2: Combine processed data
combined_data = []
for i in range(min(len(processed_group1), len(processed_group2))):
    if data_structure['metadata']['flags'][i % 3]:
        combined_data.append(processed_group1[i] + processed_group2[i])
    else:
        combined_data.append(abs(processed_group1[i] - processed_group2[i]))

# Step 3: Apply scaling and offset
scaled_data = [x * data_structure['metadata']['scale'] + data_structure['metadata']['offset'] for x in combined_data]

# Step 4: Aggregate values
aggregated_value = aggregate_values(scaled_data)

# Step 5: Perform final calculation
final_result = (aggregated_value % 1000) * math.log10(aggregated_value // 100 + 1)

print(f'Result: {int(final_result)}')