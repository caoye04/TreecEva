from collections import defaultdict, Counter
from itertools import cycle, islice

# Irrelevant helper functions (distractors)
def unused_helper_1(x):
    return sum(i * 2 for i in x if i % 3 == 0)

def deprecated_calculator(arr):
    temp = 0
    for i in range(len(arr)):
        if arr[i] < 5:
            temp += arr[i] ** 2
    return temp

# Misleading data transformations
decoys = [x ** 2 + 1 for x in range(15) if x % 4 != 0]
shadow_map = {i: decoys[i] * 3 for i in range(len(decoys))}

# Actual signal within noise
data_stream = [8, 3, 6, 1, 9, 2, 7]

# Complex but partially irrelevant preprocessing
buffer = defaultdict(int)
for idx, val in enumerate(data_stream):
    buffer[f'item_{idx}'] = val * (idx + 1)

# Dead code path - never called
class UnusedProcessor:
    def __init__(self, values):
        self.values = values
        self.checksum = sum(v ** 0.5 for v in values if v > 4)

    def transform(self):
        return [v + 10 for v in self.values]

# Decoy function that looks important
def analyze_integrity(seq):
    freq = Counter(seq)
    return all(count <= 2 for count in freq.values())

# Red herring computation with bit manipulation (unused)
bitmask_result = 0
for num in data_stream:
    if num % 2 == 0:
        bitmask_result ^= (num << 2)
    else:
        bitmask_result |= (num >> 1)

# Conditional logic chain with distractions
threshold = 5
temp_cache = []
for val in data_stream:
    if val > threshold:
        temp_cache.append(val * 1.5)
    elif val == threshold:
        temp_cache.append(val)
    else:
        temp_cache.append(val * 0.5)

# Another layer of misdirection: recursive shadow calculation
def fake_recursive_sum(lst, n):
    if n <= 0:
        return 0
    return lst[(n - 1) % len(lst)] + fake_recursive_sum(lst, n - 3)

_ = fake_recursive_sum(decoys, 10)

# Real processing begins here — deeply nested and obscured
scaling_factor = 2.0
def process_pipeline(input_data):
    # Step 1: Filter and scale
    filtered = [x for x in input_data if x % 2 == 1]  # Keep only odds
    
    # Step 2: Apply non-linear transformation
    transformed = list(map(lambda x: x ** 2 - x, filtered))
    
    # Step 3: Accumulate with offset
    accumulator = 0
    multicycle = cycle([2, -1])
    for val, coeff in zip(transformed, islice(multicycle, len(transformed))):
        accumulator += val * coeff
    
    # Step 4: Corrective shift based on length
    if len(transformed) > 3:
        accumulator -= len(input_data) * 3
    else:
        accumulator += 5
    
    # Step 5: Final scaling
    return int(accumulator * scaling_factor)

# Key execution point
final_output = process_pipeline(data_stream)

# Output result as required
print(f"Result: {final_output}")