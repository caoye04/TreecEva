import math

# Irrelevant helper function (dead code path)
def unused_helper(x):
    return sum(i * 2 for i in x if i % 3 == 0)

# Decoy transformation chain
def decoy_transform(data):
    temp = [x ^ 5 for x in data]
    return [t + 1 for t in temp if t > 10]

# Real processing begins here
raw_input = list(range(1, 26))  # [1..25]

# Step 1: Apply bitwise mask to select specific indices
index_mask = lambda i, val: (i + 1) & val & 7  # Complex but selective filter
masked_indices = [index_mask(i, v) for i, v in enumerate(raw_input)]

# Step 2: Generate control flags (some misleading)
control_flags = []
for idx in range(len(raw_input)):
    flag = ((idx ^ 3) | 5) % 4
    control_flags.append(flag)

# Step 3: Actual filtering condition based on dual criteria
valid_entries = []
for i, (val, flag) in enumerate(zip(raw_input, control_flags)):
    if (val % 2 == 1) and (flag in {1, 3}):  # Only odd values with odd flags
        valid_entries.append(val * 2)

# Step 4: Secondary transformation using trigonometric scaling (only some affect result)
angle_radians = [math.pi * v / 180 for v in valid_entries]
scaled_values = []
for v, a in zip(valid_entries, angle_radians):
    scaled = v * math.cos(a) + (v % 7)  # Mix arithmetic and trig
    scaled_values.append(round(scaled))

# Step 5: Create histogram-like count groups (distractor)
group_counts = {}
for sv in scaled_values:
    bucket = sv // 10
    group_counts[bucket] = group_counts.get(bucket, 0) + 1

# Step 6: Bit manipulation chain (partially relevant)
bit_shifted = []
for sv in scaled_values:
    shifted = ((sv << 2) ^ 15) & 255  # Transform with XOR and mask
    bit_shifted.append(shifted)

# Step 7: Filter out high-frequency outliers based on set membership
frequent_keys = {k for k, cnt in group_counts.items() if cnt >= 2}
refined_values = []
for sv, bs in zip(scaled_values, bit_shifted):
    bucket = sv // 10
    if bucket in frequent_keys:
        refined_values.append(bs)

# Step 8: Final aggregation
filtered_sum = sum(refined_values) // len(refined_values) if refined_values else 0

# Irrelevant output
_ = unused_helper(raw_input)
debug_log = decoy_transform(raw_input)

# Key execution point: final transformation applies no further change, just returns filtered_sum
def final_transformation(processed_data):
    return filtered_sum  # No-op wrapper to obscure focus

# Output target result
print(f"Target result: {final_transformation(refined_values)}")