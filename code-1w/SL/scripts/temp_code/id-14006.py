import math

# Irrelevant helper function (dead code path)
def unused_helper(x):
    return (x ** 2 + 3 * x + 1) % 7

# Decoy transformation chain
def decoy_transform(data):
    temp = [d ^ 5 for d in data]
    return [t * 2 for t in temp if t > 10]

# Real transformation pipeline
def apply_mask(values, key=3):
    return [v ^ (key + i) for i, v in enumerate(values)]

def filter_outliers(seq):
    mean = sum(seq) / len(seq)
    dev = [(x - mean) ** 2 for x in seq]
    variance = sum(dev) / len(dev)
    threshold = math.sqrt(variance) * 1.5
    return [x for x in seq if abs(x - mean) <= threshold]

def aggregate_chunks(data):
    chunks = [data[i:i+4] for i in range(0, len(data), 4)]
    reduced = []
    for chunk in chunks:
        if len(chunk) == 4:
            # Apply modular arithmetic and integer division
            val = (chunk[0] * 2 + chunk[1]) // 3
            val = (val + chunk[2]) % 97
            val = (val * chunk[3]) % 89
            reduced.append(val)
    return reduced

# Lambda-based processor
rolling_op = lambda a, b: (a + b) * 2 % 101

def rolling_process(arr):
    result = [arr[0]]
    for i in range(1, len(arr)):
        result.append(rolling_op(result[-1], arr[i]))
    return result

# Core processing function
def process_data(batch):
    # Simulate complex data refinement
    stage1 = [x for x in batch if x % 2 == 1]  # Keep odds
    stage2 = [x * 3 + 2 for x in stage1]
    stage3 = [x for x in stage2 if x < 500]
    accumulated = 0
    for val in stage3:
        accumulated = (accumulated + val) * 1.05  # Simulate interest-like growth
    return int(accumulated)

# Misleading intermediate variables
temp_buffer = [63, 127, 255, 511, 1023]
decoy_state = {'status': 'inactive', 'counter': 999, 'flag': False}

# Real data initialization
raw_input = [10, 17, 23, 45, 56, 67, 73, 81, 99, 103]
mask_key = 7

# Apply real transformations
masked_data = apply_mask(raw_input, mask_key)
filtered_data = filter_outliers(masked_data)
split_and_reduced = aggregate_chunks(filtered_data)
rolled_data = rolling_process(split_and_reduced)
transformed_batch = [x + 10 for x in rolled_data]

# Critical execution point
final_output = process_data(transformed_batch)

# Output result
print(f"Result: {final_output}")