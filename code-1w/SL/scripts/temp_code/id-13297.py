import itertools

# Irrelevant helper function (dead code path)
def unused_helper(data):
    return [x ** 2 for x in data if x % 3 == 0]

# Misleading transformation chain
def decoy_transform(seq):
    return [elem * 3 + 1 for elem in seq if elem < 50]

# Real processing function
def apply_modular_filter(seq, modulus=7, offset=2):
    # Filters elements based on modular arithmetic with offset twist
    return [num for num in seq if (num + offset) % modulus == 0]

# Intermediate transformation using itertools
def generate_pairs(values):
    # Creates sliding window pairs – not directly used but looks important
    return list(itertools.pairwise(values))

# Core transformation logic
def transform_entry(val, shift):
    if val < 0:
        return abs(val) ** 2
    else:
        return (val + shift) * 2

# Wrapper that applies transform_entry across data
def deep_transform(raw):
    shift_param = 4
    result = []
    for item in raw:
        transformed = transform_entry(item, shift_param)
        if transformed % 3 != 0:  # Additional filter
            result.append(transformed * 2)
        else:
            result.append(transformed // 2)
    return result

# Another red herring: complex-looking but unused data structure
class DataBuffer:
    def __init__(self, size):
        self.buffer = [0] * size
    def fill(self, value):
        for i in range(len(self.buffer)):
            self.buffer[i] = value * i

# Unused instance creation (distractor)
dbuff = DataBuffer(10)
dbuff.fill(7)

# Real data pipeline starts here
raw_input_data = [12, -5, 8, 21, 33, 14, 7]

# Step 1: Apply deep transformation (relevant)
transformed_data = deep_transform(raw_input_data)

# Step 2: Generate pairs (looks important, actually irrelevant)
pair_sequence = generate_pairs(transformed_data)

# Step 3: Filter using modular arithmetic (critical step)
filtered_stream = apply_modular_filter(transformed_data, modulus=5, offset=1)

# Step 4: Simulate checksum decoy (misleading intermediate)
temporary_checksum = 0
for idx, val in enumerate(filtered_stream):
    temporary_checksum += val * (idx + 1)

temporary_checksum = temporary_checksum % 997  # Looks critical, never used

# Step 5: Secondary manipulation on filtered data
manipulated_slice = [x for x in filtered_stream]
for i in range(len(manipulated_slice)):
    if i % 2 == 0:
        manipulated_slice[i] = manipulated_slice[i] // 2
    else:
        manipulated_slice[i] = manipulated_slice[i] + 10

# Step 6: Accumulate final meaningful result
accumulated = 0
for value in manipulated_slice:
    accumulated += value * 2

# Final processing function
def process_sequence(stream):
    base = 1
    for num in stream:
        base *= (num % 11)
    return base + len(stream)

# Critical execution point
final_output = process_sequence(transformed_data)

# Output result
print(f"Result: {final_output}")