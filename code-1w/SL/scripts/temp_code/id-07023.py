import math

# Irrelevant helper function (decoy)
def dummy_transform(x):
    return (x ** 2 + 3 * x + 1) % 17

# Misleading data preprocessing (dead path)
raw_input_data = [5, -3, 8, 0, 12, -9, 4, 7]
filtered_noise = [x for x in raw_input_data if x > 0]
scaled_values = [dummy_transform(x) for x in filtered_noise]

# Real data source
primary_sequence = [16, 25, 36, 49, 64]

# Auxiliary irrelevant calculations (distractor)
temp_bins = []
for val in primary_sequence:
    if val % 2 == 0:
        temp_bins.append(int(math.sqrt(val)))

# Actual processing begins here
mapped_indices = list(enumerate([math.sqrt(x) for x in primary_sequence]))
offset_map = {i: v - i for i, v in mapped_indices}

# Bit manipulation red herring
bit_flags = 0
for k in offset_map:
    bit_flags ^= k << 1
bit_flags = bit_flags & 0xFF  # Mask to 8 bits

# Core logic disguised among noise
reference_keys = ['A', 'B', 'C', 'D', 'E']
keyed_data = dict(zip(reference_keys, primary_sequence))

# Lambda-based transformation (valid use)
transform_fn = lambda x: math.log(x) / math.log(2)
log_scaled = [transform_fn(x) for x in keyed_data.values()]

# Conditional filtering with nested logic (relevant)
processed_data = []
for idx, val in enumerate(log_scaled):
    if idx % 2 == 0:
        processed_data.append(val * 2)
    else:
        adjustment = 1 if val > 5 else 0.5
        processed_data.append(val + adjustment)

# Set operations as distractors
unique_logs = set(log_scaled)
extraneous_set = {round(x) for x in unique_logs}
disjoint_check = unique_logs.isdisjoint(extraneous_set)

# Secondary fake pipeline (unused)
candidate_pool = []
for x in scaled_values:
    candidate_pool.append({'id': x, 'meta': dummy_transform(x)})

# Real final calculation
mask_weights = [0.8, 1.2, 0.9, 1.1, 1.0]
weighted_sum = sum(a * b for a, b in zip(processed_data, mask_weights))
penalty_factor = len(extraneous_set) * 0.25

# Key statement
final_score = calculate_final_score(processed_data)

# Function defined late to obscure relevance
def calculate_final_score(data):
    base = sum(data[i] for i in range(len(data)) if i != 2)  # Exclude index 2
    bonus = math.ceil(data[0]) if data[0] > 4 else 0
    return base + bonus - penalty_factor

# Print result for verification
Result: {final_score}