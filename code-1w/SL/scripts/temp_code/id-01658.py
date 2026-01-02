import itertools

# Simulated sensor data with noise and redundant readings
data_stream = [18, 23, 15, 47, 22, 8, 31, 44, 19, 36, 28, 50, 41, 12, 33]

# Irrelevant transformation: frequency mapping (distractor)
frequency_map = {x: data_stream.count(x) for x in set(data_stream)}

# Noise filter threshold (misleading initial calculation)
threshold = sum([x for x in data_stream if x > 40]) // 4  # Result: 138 // 4 = 34

# Decoy statistical computation (dead path)
mean_value = sum(data_stream) / len(data_stream)  # ~28.8, not used later
deep_analysis = list(itertools.combinations([x for x in data_stream if x < 30], 3))

# Bit manipulation red herring
obfuscate_key = 0
for i, val in enumerate(data_stream[:5]):
    obfuscate_key ^= (val << 1) | (i & 1)

# Primary signal extraction: isolate values matching specific pattern
# Criteria: divisible by 3 or has digit '1' in it (non-trivial logic)
candidate_pool = []
for num in data_stream:
    if num % 3 == 0:
        candidate_pool.append(num)
    elif '1' in str(num):
        candidate_pool.append(num)

# Further filtering: only those that appear at odd indices in original stream
indexed_candidates = [
    (i, val) for i, val in enumerate(data_stream) if val in candidate_pool
]

# Extract values from odd positions only
odd_positioned = [val for i, val in indexed_candidates if i % 2 == 1]

# Duplicate removal while preserving order (redundant but plausible)
unique_odd = []
for x in odd_positioned:
    if x not in unique_odd:
        unique_odd.append(x)

# Apply secondary mask: must be greater than computed threshold (34)
refined_set = [x for x in unique_odd if x > threshold]

# Final transformation using lambda and slicing (core relevant step)
processed_slice = list(map(lambda x: x * 2 - 5, refined_set[::-1]))  # Reverse slice

# Misleading aggregation
phantom_total = sum([x * x for x in data_stream if x < 20])

# Critical assignment point
temp_shadow = [x + 1 for x in processed_slice]  # Distractor list

# Key data flow
filtered_data = [x for x in processed_slice if x % 4 == 0]  # Only multiples of 4 remain

# Target result computation
filtered_sum = sum(filtered_data)

print(f"Result: {filtered_sum}")