import math

# Irrelevant helper function (dead code path)
def unused_helper(x):
    return sum(i ** 2 for i in range(x)) if x > 0 else 0

# Distractor transformation chain
def transform_sequence(seq):
    temp_a = [x * 2 + 1 for x in seq]
    temp_b = [math.sin(x) for x in temp_a]
    temp_c = [abs(int(math.cos(x) * 10)) for x in temp_b]
    return temp_c[:len(temp_c)//2]  # Only half used, rest is distraction

# Another decoy function with misleading intermediate results
def evaluate_threshold(values):
    threshold = 4.75
    result_flags = []
    for v in values:
        flag = (v > threshold) or (v == threshold and v % 2 == 0)
        result_flags.append(flag)
    return result_flags

# Core logic hidden among distractors
data_chunk = list(range(8, 16))

# Red herring: complex-looking but unused bitwise shift chain
bit_noise = 0
for i in range(len(data_chunk)):
    bit_noise ^= data_chunk[i] << 2
    bit_noise |= (bit_noise >> 3) & 0xFF

# Decoy list comprehension with case conversion (irrelevant)
status_codes = ['ACTIVE', 'PENDING', 'FAILED']
status_lower = [s.lower() for s in status_codes]
class_mapping = {i: status_lower[i % 3] for i in range(10)}

# Conditional expression mixed with lambda (required python feature)
select_mode = True
operation_lambda = lambda x: x ** 2 if select_mode else x ** 0.5

# Tuple unpacking and distractor assignments
aux_data = (sum(data_chunk), len(data_chunk), max(data_chunk))
(total_sum, count, peak_value) = aux_data
redundant_tuple = (total_sum * 2, count + 5, peak_value - 1)

# Real computation buried in noise
def compute_weighted_score(seq):
    base_scores = [operation_lambda(x - 9) for x in seq]
    weights = [0.5 ** i for i in range(len(base_scores))]
    weighted = sum(b * w for b, w in zip(base_scores, weights))
    return weighted

# Multi-step processing pipeline with red herrings
def process_pipeline(chunk):
    # Step 1: filter even numbers (only this matters)
    filtered = [x for x in chunk if x % 2 == 0]
    
    # Step 2: apply actual transformation needed
    transformed = [int(math.log2(x)) * 3 for x in filtered]
    
    # Step 3: distractor aggregation
    fake_moving_avg = [sum(transformed[i:i+2]) / 2 for i in range(len(transformed)-1)]
    
    # Step 4: real reduction
    aggregate = sum(transformed) + len(transformed)
    
    # Step 5: conditional override that doesn't trigger (misleading)
    final_value = aggregate * 1.5 if any(x > 100 for x in fake_moving_avg) else aggregate
    
    # Step 6: irrelevant bit manipulation
    mask = 0b1111
    masked_value = int(final_value) & mask
    
    # Step 7: final adjustment based on tuple unpacking
    offset = redundant_tuple[1] - 4  # resolves to 6 - 4 = 2
    return final_value + offset

# Critical execution point
final_output = process_pipeline(data_chunk)

print(f"Target result: {final_output}")