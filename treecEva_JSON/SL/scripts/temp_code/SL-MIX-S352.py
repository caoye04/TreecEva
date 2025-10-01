import math

def transform_data(data_dict):
    result = []
    for key, values in data_dict.items():
        sub_result = 0
        for i, val in enumerate(values):
            if i % 2 == 0:
                sub_result += val ** 2
            else:
                sub_result -= math.sqrt(abs(val))
        result.append(sub_result)
    return result

def process_sequences(sequences):
    processed = []
    for seq in sequences:
        transformed = [x if x > 0 else -x for x in seq]
        reduced = sum(transformed) // len(transformed)
        processed.append(reduced)
    return processed

data = {
    'alpha': [3, -4, 5, -6, 7],
    'beta': [-2, 8, -10, 12],
    'gamma': [1, -1, 2, -2, 3, -3]
}

# Step 1: Transform the data
step1_result = transform_data(data)

# Step 2: Process sequences
sequences = [
    [15, -3, 9, -12],
    [-5, 7, -9, 11, -13],
    [2, -4, 6, -8, 10, -12]
]
step2_result = process_sequences(sequences)

# Step 3: Combine results with bitwise operations
combined = []
for i in range(min(len(step1_result), len(step2_result))):
    a = int(step1_result[i])
    b = step2_result[i]
    xor_result = a ^ b
    combined.append(xor_result)

# Step 4: Mathematical transformation
mapped_values = list(map(lambda x: math.log(abs(x) + 1), combined))

# Step 5: Aggregate and finalize
aggregated = sum(mapped_values)
final_result = int(aggregated * 1000)  # Scale for integer result

print(f"Result: {final_result}")