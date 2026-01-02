import math

# Irrelevant helper function (dead code path)
def unused_signal_filter(x):
    return [val for val in x if val > 0.5]

# Distractor computation with misleading intermediate
temp_calibration = [math.sin(i * 0.1) for i in range(20)]
calibration_sum = sum(temp_calibration)  # Looks important but unused later

# Real data processing begins here
raw_samples = [i**2 + 3*i - 4 for i in range(15)]  # Generate base dataset

# Slice manipulation - relevant
processed_slice = raw_samples[5:12:2]  # Take every second element from index 5 to 11

# Bit manipulation red herring
bit_mask = 0b101010
masked_values = [x ^ bit_mask for x in raw_samples[:10]]  # Computed but not used

# Conditional logic with early return simulation
threshold = 20
def evaluate_sample(x):
    if x < threshold:
        return x * 1.5
    elif x == threshold:
        return x
    else:
        return x * 0.8

# Unused sorting operation (distractor)
sorted_distractor = sorted(processed_slice, key=lambda x: -x)  # Not used in final chain

# Core transformation pipeline
transform_fn = lambda val: int((val + 5) * 0.7) if val % 2 == 0 else int((val - 3) * 0.9)

# Data stream with slicing and filtering
data_stream = [transform_fn(x) for x in processed_slice if x % 3 != 1]

# Secondary irrelevant list comprehension
shadow_copy = [x for x in data_stream if x > 10]  # Partially overlaps but not used

# Complex conditional counting (partially relevant)
count_valid = 0
for item in data_stream:
    if item > 8:
        count_valid += 1
    elif item < 3:
        count_valid -= 1  # Rare case

# Key nested operation: tuple unpacking and arithmetic
intermediate_results = []
for idx, val in enumerate(data_stream):
    offset = math.log(2 * idx + 2)  # Avoid log(0)
    adjusted = val + int(offset)
    category_flag = 'A' if adjusted > 10 else 'B'
    intermediate_results.append((idx, adjusted, category_flag))

# Final aggregation with conditional expression and slicing
aggregate = 0
for record in intermediate_results[::2]:  # Every other record
    _, value, flag = record
    multiplier = 2 if flag == 'A' else 0.5
    aggregate += value ** 1.1 * multiplier

# Decoy assignment just before final result
decoy_output = aggregate * 0.1  # Looks like candidate but not correct

# Actual final output calculation
final_output = int(aggregate / len(intermediate_results) if intermediate_results else 0)

# Print required result
print(f"Target result: {final_output}")