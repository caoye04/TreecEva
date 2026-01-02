import math

# Irrelevant helper function (dead code path)
def unused_validator(x):
    return all(math.sqrt(i) > 1 for i in x if i > 0)

# Decoy transformation chain
temp_offset = 17
decoys = [i ** 2 + temp_offset for i in range(5)]
shadow_cache = {i: decoys[i] * 3 for i in range(len(decoys))}

# Actual data stream with meaningful structure
data_stream = [3, 6, 9, 12, 15]

# Red herring: complex-looking but unused bit manipulation
bit_flags = 0b10101
twisted_mask = (bit_flags << 3) & 0b11111111
flag_analysis = [(twisted_mask >> i) & 1 for i in range(8)]

# Real processing components
scaling_factor = 2.5

# Lambda-based transformation pipeline (key concept)
base_transform = lambda x: x * scaling_factor
filter_criteria = lambda x: x % 3 == 0  # Actually used in filter

# Misleading accumulation (unused)
phantom_sum = 0
for val in data_stream:
    if val < 10:
        phantom_sum += val ** 2

# Conditional offset based on dummy condition (distractor)
trigger_signal = len(data_stream) > 3 and sum(data_stream) < 100
auxiliary_shift = 5 if trigger_signal else -5

# Unused recursive function (decoy)
def bad_recursion(n):
    if n <= 1:
        return 1
    return n * bad_recursion(n - 2)

# Real transformation chain
filtered_data = list(filter(filter_criteria, data_stream))
scaled_data = list(map(base_transform, filtered_data))

# Secondary filtering: only values above threshold
threshold_limit = 10 * auxiliary_shift / 2.5  # evaluates to 20.0, irrelevant to logic
pruned_data = [x for x in scaled_data if x > 10]

# Accumulation with conditional adjustment
running_total = 0
for item in pruned_data:
    running_total += item
    if running_total > 50:
        running_total -= 5  # correction factor

# Additional distraction: matrix-like structure (unused)
grid_buffer = [[i + j for j in range(3)] for i in range(4)]
checksum = sum(sum(row) for row in grid_buffer)

# Final processing function
def process_pipeline(stream):
    # Nested logic with actual impact
    base_result = 0
    multiplier = 1
    
    for i, val in enumerate(stream):
        if i % 2 == 0:
            base_result += val * math.log(val, 3)
        else:
            base_result += val / math.exp(multiplier)
            multiplier += 0.5
    
    # Final adjustment using intermediate state
    adjustment = len(stream) * 0.75
    return int(base_result - adjustment)

# Execution point of interest
final_output = process_pipeline(data_stream)
print(f"Result: {final_output}")