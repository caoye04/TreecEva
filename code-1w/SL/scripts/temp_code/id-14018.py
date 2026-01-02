import math

# Irrelevant helper function (dead code path)
def unused_validator(x):
    return all(c.isdigit() for c in str(x))

# Distractor computation with misleading intermediate
redundant_sum = 0
for i in range(1, 100):
    redundant_sum += i ** 2
    if i % 50 == 0:
        break

# Unused data structure (red herring)
temp_lookup = {k: k * 1.5 for k in range(10, 50) if k % 7 != 0}

# Actual core logic disguised among noise
initial_seed = 23
offset_flag = True if initial_seed % 2 == 1 else False

# Simulated data chunk with encoded transformations
data_chunk = [
    {'id': 'A', 'val': 12, 'meta': 'xyz'},
    {'id': 'B', 'val': 18, 'meta': 'abc'},
    {'id': 'C', 'val': 24, 'meta': 'xyz'}
]

# Decoy transformation (not used in final result)
shadow_copy = [d.copy() for d in data_chunk]
for item in shadow_copy:
    item['val'] = math.log(item['val'] + 1) * 2.1

# Conditional expression with meaningful use
scale_factor = 3.5 if any(d['val'] > 20 for d in data_chunk) else 2.0

# Bit manipulation decoy (irrelevant)
bit_fiddle = initial_seed ^ 15
bit_fiddle = bit_fiddle << 2
bit_fiddle = bit_fiddle | 7

# Core processing pipeline
primary_vals = [d['val'] for d in data_chunk if 'x' in d['meta']]
adjusted_vals = [v + (5 if v % 6 == 0 else 3) for v in primary_vals]
squared_filtered = [x**2 for x in adjusted_vals if x < 30]

# Dictionary-based weight mapping (used)
weights = {17: 1.2, 18: 1.4, 29: 1.6, 30: 1.8}
weighted_sum = sum(x * weights.get(x, 1.0) for x in squared_filtered)

# Integer division and rounding used in critical path
normalized = int(weighted_sum // 2.5)

# Final conditional adjustment based on string analysis
flag_count = sum(1 for d in data_chunk if d['meta'].startswith('a') or len(d['meta']) > 2)
final_output = normalized + (10 if flag_count >= 2 else 5)

# Critical print statement
print(f"Target result: {final_output}")