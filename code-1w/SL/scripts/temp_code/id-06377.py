import math

# Irrelevant helper function (dead code path)
def unused_helper(data):
    return [x * 2 for x in data if x % 3 == 0]

# Decoy transformation with misleading intermediate results
def decoy_transform(seq):
    shifted = [((x << 2) ^ 5) % 17 for x in seq]  # Bit manipulation red herring
    return [math.sin(x) for x in shifted]  # Trigonometric distraction

# Actual key transformation
def transform_value(x):
    if x <= 0:
        return abs(x) * 3
    else:
        return (x ** 2) % 19  # Modular arithmetic core

# Real processing chain
def process_chunk(chunk):
    a = sum(chunk) % 7
    b = math.ceil(sum([transform_value(x) for x in chunk]) / len(chunk))
    c = (a * b) ^ 13  # XOR obfuscation
    return c

# Higher-level orchestration with slicing distraction
def slice_and_process(data):
    mid = len(data) // 2
    left, right = data[:mid], data[mid:]
    # Distracting slice reversals (not used in final path)
    _ = left[::-1], right[::-1]
    # Only right slice matters
    return process_chunk(right)

# Core data transformation
def transform_sequence(seq):
    # String manipulation red herring
    identifier = ''.join([chr(97 + (x % 26)) for x in seq[:5]])  # Maps to 'abcde'-like string
    # Actual relevant transformation
    base_modified = [transform_value(x) + (i % 4) for i, x in enumerate(seq)]
    extended = base_modified + [sum(base_modified[:3]), sum(base_modified[-3:])]
    return extended

# Final computation
def process_sequence(data):
    temp_result = 0
    for i, val in enumerate(data):
        if i % 2 == 0:
            temp_result += val * (i + 1)
        else:
            temp_result -= val
    return temp_result + (data[0] ^ data[-1])  # Final adjustment

# Irrelevant global variables
MAX_LIMIT = 9999
THRESHOLD_MAP = {k: k*2+1 for k in range(10)}
CONFIG_FLAGS = [True, False, True]

# Input sequence (real problem data)
input_data = [8, -3, 12, 7, 0, 15, 4, 9]

# Distraction block 1: Unused branching
if sum(input_data) > 50:
    processed_input = [x for x in input_data if x % 2 == 1]
elif any(x < 0 for x in input_data):
    processed_input = [x + 5 for x in input_data]  # This branch taken, but result not used directly
else:
    processed_input = input_data.copy()

# Distraction block 2: Parallel decoy processing
decoy_output = decoy_transform(input_data)
placeholder = slice_and_process(input_data)  # Uses real data but doesn't affect output

# Real execution path begins here
adjusted_input = [x + 1 for x in input_data]  # Minor adjustment
transformed_data = transform_sequence(adjusted_input)

# Critical statement
final_output = process_sequence(transformed_data)

print(f"Result: {final_output}")