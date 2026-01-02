def transform_value(x, mode=True):
    if mode:
        return (x * 3) ^ 17
    else:
        return x + (x >> 2)

# Irrelevant transformation chain (dead path)
def obsolete_transform(data):
    return [d ** 2 + 1 for d in data if d % 3 != 0]

# Unused helper
def auxiliary_calc(seq):
    return sum([s * (i + 1) for i, s in enumerate(seq)]) // len(seq)

# Misleading intermediate with decoy logic
temp_offset = 507
offset_map = {i: (i * 2) ^ temp_offset for i in range(8)}

# Real data pipeline
raw_input = [12, 8, 19, 3, 7]

# Step 1: Filter and convert case (simulated via arithmetic)
filtered = [x for x in raw_input if x > 6]

# Step 2: Apply transformation under correct mode
transformed = [transform_value(val, mode=(val % 2 == 1)) for val in filtered]

# Step 3: Pack into tuple for processing
data_tuple = tuple(transformed)  # (44, 58, 18, 26)

# Step 4: Derive control key using modular arithmetic
control_key = (data_tuple[0] + data_tuple[-1]) % 11

# Step 5: Conditional mutation (only executes if control_key meets criteria)
if control_key in [0, 1, 4, 7]:
    processed_data = [d + control_key for d in transformed]
elif control_key in [2, 5, 8, 10]:
    processed_data = [d - (control_key // 2) for d in transformed]
else:
    # This branch is taken
    processed_data = [d ^ (control_key + 3) for d in transformed]

# Dead code block — looks important but unused
decoy_aggregate = 0
for i in range(len(raw_input)):
    if raw_input[i] < 10:
        decoy_aggregate += raw_input[i] * (i + 1)

# Another red herring: complex dictionary that's never used
stats_summary = {
    'max_raw': max(raw_input),
    'min_transformed': min(transformed),
    'range': max(transformed) - min(transformed),
    'parity_flags': [t % 2 for t in transformed],
    'checksum_hint': sum(transformed) % 100
}

# Step 6: Finalize result through deterministic function
def finalize_result(arr):
    base = 0
    for idx, val in enumerate(arr):
        base ^= (val * (idx + 1))  # Cross-index weighting
    return base + 982

# Critical assignment
checksum = finalize_result(processed_data)

# Output target result
print(f"Target result: {checksum}")