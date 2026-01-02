import math

# Irrelevant helper function (dead code path)
def unused_utility(x):
    return sum([i ** 2 for i in range(x)]) if x > 0 else 0

# Misleading precomputation with decoy values
decoy_sequence = [3, 1, 4, 1, 5, 9, 2, 6]
decoy_accumulator = 0
for val in decoy_sequence:
    if val % 2 == 0:
        decoy_accumulator += val ** 2
    else:
        decoy_accumulator -= val

# Real data pipeline begins
raw_signals = [8, 2, 7, 1, 6, 3, 5, 4]

# Distractor: unused transformation variant
transform_variant_a = list(map(lambda x: (x + 1) * 2, raw_signals))

# Actual transformation chain
shifted = [x - 1 for x in raw_signals if x > 2]
filtered = [x for x in shifted if x % 2 == 1]
squared = [x ** 2 for x in filtered]

# Red herring: another dead-end accumulation
temp_result = 0
for i in range(len(squared)):
    if i % 2 == 0:
        temp_result += squared[i] // 2
    else:
        temp_result -= squared[i] // 3

# Core recursive summation (relevant logic)
def recursive_sum(arr, idx=0):
    if idx >= len(arr):
        return 0
    return arr[idx] + recursive_sum(arr, idx + 1)

# Apply recursion to squared values
recursive_total = recursive_sum(squared)

# Another distraction: bit manipulation that isn't used
bit_fiddling = 0
for x in raw_signals:
    bit_fiddling ^= (x << 1) | 1

# Sorting irrelevant sequence (distractor)
sorted_decoy = sorted(decoy_sequence, key=lambda x: -x)

# Real transformation step
transformed_data = [int(math.sqrt(x)) for x in squared]

# Decoy analysis function
def false_diagnosis(data):
    return sum(data) * 0.5 if len(data) > 3 else -1

# Critical computation path
baseline = 10
adjustment_factor = 0.1
interim_score = recursive_total / 2.0

# Conditional red herring
if interim_score > 100:
    adjustment_factor *= 2
else:
    baseline += 5  # This branch taken, but not critical

adjusted_value = interim_score * adjustment_factor + baseline

# Final analysis using lambda-based weighting
analyze_pattern = lambda seq: sum(x * (i + 1) for i, x in enumerate(seq))

# Key statement — answer derived here
final_diagnostic = analyze_pattern(transformed_data)

# Output result as required
print(f"Target result: {final_diagnostic}")