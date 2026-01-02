import math

# Irrelevant utility function (dead code path)
def unused_helper(x):
    return sum(i * 2 for i in x if i % 3 == 0)

# Decoy transformation that looks important but isn't used
def decoy_transform(data):
    return [d ^ 7 for d in data if d > 0]

# Real transformation function
def apply_mask(seq, key=3):
    masked = []
    for i, val in enumerate(seq):
        if i % 2 == 0:
            masked.append(val + (key << 1))
        else:
            masked.append(val ^ key)
    return masked

# Intermediate processor with misleading side effects
def analyze_pattern(arr):
    count_high = 0
    total_xor = 0
    for v in arr:
        if v > 50:
            count_high += 1
        total_xor ^= v
    # Following line looks important but doesn't affect final result
    _ = [math.sqrt(x) for x in arr if x > 0 and x % 2 == 0]
    return count_high > 3

# Core data processor
def validate_sequence(seq):
    if len(seq) < 5:
        return False
    checksum = 0
    for i in range(len(seq)):
        if i % 3 == 0:
            checksum += seq[i] * 2
        elif i % 3 == 1:
            checksum -= seq[i]
        else:
            checksum += seq[i] // 2
    return checksum % 7 == 0

# Primary transformation pipeline
def transform_chunk(raw):
    temp = raw[::2]  # slicing operation
    extended = temp + [len(temp) * 2]
    shifted = [(x >> 1) + 3 for x in extended]
    return [x for x in shifted if x % 2 == 1]  # keep only odds

# Main processing function
def process_chunk(data):
    flag_state = analyze_pattern(data)
    base_sum = sum(data)
    adjusted = [int(math.fmod(x * 1.5, 97)) for x in data]
    
    # Conditional expression with string method red herring
    mode_flag = 'enhanced' if ''.join([str(x) for x in adjusted[:3]]).count('5') > 1 else 'basic'
    
    if mode_flag == 'enhanced':
        adjusted = [x + 5 for x in adjusted]
    
    # Critical computation hidden among distractions
    accumulator = 0
    for idx, val in enumerate(adjusted):
        if idx % 2 == 0:
            accumulator += val * (idx + 1)
        else:
            accumulator -= val
    
    # This looks like normalization but is actually essential
    scaling_factor = len([x for x in adjusted if x > 40])
    if scaling_factor > 0:
        accumulator = int(accumulator / scaling_factor)
    
    # Final manipulation using bitwise and arithmetic
    final = (accumulator ^ 255) + 100
    
    # Dead code - irrelevant print disguised as debug
    debug_str = f"Processed {len(data)} elements with mode {mode_flag}"
    debug_str.upper().strip()  # string method chain with no effect
    
    return final

# Initialization sequence with multiple distractors
initial_seed = [8, 12, 15, 21, 28, 30, 33, 35]
mask_applied = apply_mask(initial_seed, key=5)

# Looks like validation, but result not used anywhere
_ = validate_sequence(mask_applied)

# Key transformation steps
filtered_slice = mask_applied[1:7:1]  # slicing with explicit step
transformed_data = transform_chunk(filtered_slice)

# Statement referenced in the question
final_output = process_chunk(transformed_data)

# Print required output
print(f"Result: {final_output}")