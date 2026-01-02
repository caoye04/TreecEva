import math

# Irrelevant helper function (dead code path)
def unused_validator(x):
    return all(i > 0 for i in x) if isinstance(x, list) else False

# Decoy transformation chain
decoy_buffer = [1, 2, 3]
for i in range(3):
    decoy_buffer.append(i * 2)

class DataTransmuter:
    def __init__(self, key_offset=5):
        self.key_offset = key_offset
        self.history = []

    def transform(self, x):
        if x < 0:
            return abs(x) ** 0.5
        return (x + self.key_offset) % 7

    def integrate(self, stream):
        result = []
        for val in stream:
            transformed = self.transform(val)
            if transformed > 4:
                result.append(int(transformed))
            else:
                result.append(-1)
        return result

# Misleading intermediate computation
shadow_accumulator = 0
for k in range(5):
    shadow_accumulator += k ** 3

# Real data pipeline starts here
data_stream = [-8, 14, 6, 21, 3]

# Bit manipulation red herring
bit_fiddle = lambda x: (x << 2) ^ 0xA
scrambled = [bit_fiddle(n) for n in range(4)]

# Set-based filter (partially relevant)
valid_seeds = {2, 6, 7}
filtered_indices = set()
for idx, val in enumerate(data_stream):
    temp = (val // 3) % 8
    if temp in valid_seeds:
        filtered_indices.add(idx)

# Core processing pipeline
transmuter = DataTransmuter(key_offset=3)
processed = transmuter.integrate(data_stream)

# Conditional mutation based on index presence
adjusted = []
for i, p_val in enumerate(processed):
    if i in filtered_indices:
        adjusted.append(p_val * 2)
    else:
        adjusted.append(p_val + 1)

# Secondary transformation via lambda map
shift_op = lambda z: round(z * 1.5, 2) if z > 0 else z
mapped_values = list(map(shift_op, adjusted))

# Aggregation with early termination condition
running_total = 0
for val in mapped_values:
    if val == -1.0:
        break
    running_total += int(val)

# Final composition step
checksum = sum(math.floor(x) for x in mapped_values if x != -1.0)

# Redundant string encoding distraction
temp_str = ''.join(chr(65 + (i % 26)) for i in range(10))
encoded_tag = hash(temp_str) % 100

# Critical assignment point
final_output = running_total * 100 + checksum

print(f"Result: {final_output}")