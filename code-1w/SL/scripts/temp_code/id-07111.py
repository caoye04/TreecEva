import math

# Irrelevant helper function (dead code path)
def unused_helper(x):
    return sum(i ** 2 for i in range(x)) if x > 5 else 0

# Misleading data transformation chain
temp_buffer = [i * 1.5 + 2 for i in range(8)]
offset_map = {i: math.sin(i) for i in range(6)}

# Core data setup with red herring elements
raw_sequence = [3, 1, 4, 1, 5, 9, 2, 6]
scaling_factor = 2.5
noisy_adjustment = [x * scaling_factor for x in raw_sequence]

# Distractor: complex but unused bitwise manipulation
bit_fiddling = 0
for x in raw_sequence:
    bit_fiddling ^= (x << 2) | (x >> 1)

# Another decoy variable with plausible-looking accumulation
cumulative_checksum = 0
for i, val in enumerate(noisy_adjustment):
    cumulative_checksum += int(val) * (i + 1)

# Actual relevant transformation: extract peaks based on simple combinatorics
transformed_data = []
for i in range(1, len(raw_sequence) - 1):
    if raw_sequence[i] > raw_sequence[i-1] and raw_sequence[i] > raw_sequence[i+1]:
        transformed_data.append(raw_sequence[i])

# Secondary transformation: map via conditional expression
eval_marks = [x if x > 3 else x * 2 for x in transformed_data]

# Threshold determined by irrelevant trigonometric sum (misdirection)
threshold_basis = sum(math.cos(i) for i in range(4))
threshold = int(abs(threshold_basis) * 10) or 3  # resolves to 3

# Decoy control flow with no impact
if len(eval_marks) > threshold:
    dummy_flag = True
    shadow_copy = [x * 10 for x in eval_marks]  # dead assignment
else:
    dummy_flag = False

# Actual analysis function with embedded logic
def analyze_pattern(data, limit):
    if not data:
        return -1
    
    # Accumulation with conditional expression twist
    total = 0
    for val in data:
        # Conditional expression used meaningfully
        contribution = val ** 2 if val >= limit else val * 1.5
        total += contribution
    
    # Nested adjustment based on list length (3 levels deep)
    adjustment = 0
    if len(data) == 1:
        adjustment = 5
    elif len(data) > 1:
        for i in range(len(data)):
            if i % 2 == 0:
                adjustment += math.floor(data[i] / 2)
    
    # Final computation combining multiple concepts
    result = total - adjustment
    
    # Red herring: unused intermediate
    normalized = result / (sum(data) or 1)
    
    return result

# Critical execution point
final_diagnostic = analyze_pattern(transformed_data, threshold)

# Output the target result
print(f"Target result: {final_diagnostic}")