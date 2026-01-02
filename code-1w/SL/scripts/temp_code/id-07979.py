from itertools import compress, count
import math

# Simulated sensor data stream with metadata
data_stream = [104, 217, 92, 188, 251, 73, 164, 205]
metadata_flags = [1, 0, 1, 1, 0, 1, 0, 1]

# Irrelevant transformations (distractors)
decoy_transform = lambda x: (x << 3) | (x >> 2)
decoy_list = [decoy_transform(x) for x in data_stream if x % 2 == 0]

# Real processing begins
valid_indices = list(compress(count(0), metadata_flags))
selected_data = [data_stream[i] for i in valid_indices]

# Bit manipulation chain
shifted = [(x >> (x % 3)) ^ 17 for x in selected_data]
modular_squares = [(x * x) % 257 for x in shifted]

# Filtering logic with red herring condition
threshold = 150
spurious_sum = sum([x for x in modular_squares if x > threshold])  # unused but plausible
sum_filtered = sum([x for x in modular_squares if x < threshold])

# Decoy function (never called)
def analyze_pattern(seq):
    return [seq[i] ^ seq[i-1] for i in range(1, len(seq))] + [seq[0]]

# Another decoy: complex unused calculation
reconstructed = list(map(lambda a, b: (a | 13) & b, data_stream[:-1], data_stream[1:]))

# Critical bit mask derived from prime analysis
mask = 0
for i in range(8):
    if all((i % j) != 0 for j in range(2, int(math.sqrt(i)) + 1)) and i >= 2:
        mask |= (1 << i)

# Finalization function (simple but obscured)
finalize = lambda x: x ^ 0x5F

# Key assignment — this is the execution point of interest
current_state = {'final': None}
checksum = finalize(sum_filtered & mask)
current_state['final'] = checksum

# Dead code path (misleading control flow)
if len(reconstructed) > spurious_sum % 100:
    checksum -= 1000  # never executes due to logic
else:
    pass  # deliberate obfuscation

# Output result as required
print(f"Result: {checksum}")