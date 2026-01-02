import math

# Irrelevant helper function (dead code path)
def unused_helper(x):
    return x ** 2 + 3 * x - 7

# Decoy transformation chain
def decoy_transform(sequence):
    temp = [x * 1.5 for x in sequence if x % 2 == 0]
    return sorted(temp, reverse=True)

# Real processing pipeline
transform_fn = lambda val: val ^ (val << 1)  # Bit manipulation

filter_condition = lambda x: x > 0 and (x & (x - 1)) == 0  # Power of two check

def extract_features(dataset):
    features = []
    for item in dataset:
        if item < 0:
            continue
        shifted = item >> 2
        if shifted % 3 == 0:
            features.append(shifted)
    return features

# Misleading intermediate calculation
tainted_accum = 0
for i in range(100):
    if i % 7 == 0:
        tainted_accum += i * 0.5  # Red herring

# Core logic disguised among noise
base_sequence = [12, 7, 16, 3, 8, 21, 4, 31]

# Irrelevant set operation (distractor)
unique_tails = {x % 10 for x in base_sequence if x > 10}

# Actual data stream preparation
data_stream = list(map(transform_fn, base_sequence))

# Another decoy variable
event_tracker = {'count': 0, 'flags': []}
for val in data_stream:
    if val % 4 == 0:
        event_tracker['count'] += 1
        event_tracker['flags'].append(val | 5)

# Feature extraction with filtering
selected_features = extract_features(data_stream)
cleaned_data = list(filter(filter_condition, selected_features))

# Secondary transformation
processed_intermediate = []
for x in cleaned_data:
    processed_intermediate.append(int(math.log2(x)) + (x & 7))

# Tertiary aggregation with distraction
aggregate_pool = []
decoys = [33, 44, 55]
for idx, v in enumerate(processed_intermediate):
    if idx in {0, 2, 4}:
        aggregate_pool.append(v * 2)
    else:
        aggregate_pool.append(v + 1)

# Final pipeline step
offset_compensation = sum([1 for x in decoys if x > 40])  # Misleading use

mask_value = 0xAA

# Critical computation chain
masked_results = []
for num in aggregate_pool:
    masked = num ^ mask_value  # XOR with constant
    if masked < 100:
        masked_results.append(masked)

# Reduction step
reduction_key = len(masked_results) if len(masked_results) > 2 else 1
final_sum = sum(masked_results) // reduction_key

# Auxiliary adjustment
adjustment_table = {i: i * (i - 1) for i in range(1, 6)}
adjustment = adjustment_table.get(len(cleaned_data), 0)  # Depends on filtered count

# Final output calculation
final_output = final_sum - adjustment

# Output result
print(f"Result: {final_output}")