import math

# Irrelevant helper function (dead code path)
def unused_helper(x):
    return x ** 3 + 2 * x - 1

# Distractor computation with misleading intermediate values
temp_offset = 7
magic_factor = 42
scaling_bias = -5
arbitrary_threshold = 999

# Real data processing chain begins
sequence_seed = [3, 1, 4, 1, 5, 9, 2, 6, 5]
data_chunk = sequence_seed[1:8:2]  # slicing: [1, 1, 9, 6]

# Misleading transformation (not used in final result)
decoy_transform = [x ^ temp_offset for x in data_chunk]

# Conditional branching with red herring logic
if len(data_chunk) > 3:
    adjustment = magic_factor // 6
else:
    adjustment = scaling_bias

# Core recursive logic to compute checksum
def recursive_checksum(seq, index=0):
    if index >= len(seq):
        return 0
    current_val = seq[index]
    # Bit manipulation mixed with arithmetic
    bit_modified = (current_val << 1) ^ 3
    return bit_modified + recursive_checksum(seq, index + 1)

# Secondary processing: filter and scale
filtered_data = [x for x in data_chunk if x % 2 == 1]  # keeps odds: [1, 1, 9]

# Another distraction: irrelevant list comprehension
dummy_aggregate = sum([x * scaling_bias for x in sequence_seed if x < 5])

# Linear search for a non-critical element (distractor)
found_index = -1
for i in range(len(data_chunk)):
    if data_chunk[i] == 99:
        found_index = i

# Actual key transformation pipeline
transformed = []
for val in filtered_data:
    transformed.append(int(math.sqrt(val * val + 2 * val + 1)))  # sqrt((val+1)^2) = val+1

# Now apply conditional scaling based on length
if len(transformed) == 3:
    scaled = [x * 2 for x in transformed]  # becomes [4, 4, 20]
else:
    scaled = transformed

# Aggregation with distractor variables intentionally nearby
sum_primary = sum(scaled)
sum_secondary = sum(decoy_transform)  # decoy usage

# Final processing step
intermediate_result = sum_primary + adjustment

# Key variable assignment
final_output = process_sequence(data_chunk)

# Function definition placed after use (adds cognitive load)
def process_sequence(seq):
    base = recursive_checksum(seq)
    subset = seq[::2]
    offset = len(subset) * 2
    return base - offset + len(seq)

# Print result for evaluation
print(f"Result: {final_output}")