import math

# Irrelevant helper function (dead code path)
def unused_validator(x):
    return all(i > 0 for i in x) if isinstance(x, list) else False

# Decoy transformation chain
def decoy_transform(data):
    shifted = [d ^ 255 for d in data[:10]]
    return [s * 3 + 7 for s in shifted]

# Real preprocessing with distractor logic
def normalize_readings(raw):
    base = sum(raw) / len(raw)
    adjusted = [(r - base) * 1.5 for r in raw]
    # Red herring: complex but unused filtering
    filtered_outliers = [a for a in adjusted if abs(a) < 2 * base]
    return adjusted  # actual return

# Bit manipulation misdirection
def bit_scramble(index, value):
    return (value << 2) | (index & 3)

# Logical core processing (used)
threshold_filter = lambda x: x > 0.1

# Data masking with nested comprehensions (partially relevant)
def mask_data(seq, mask):
    return [s if m else 0 for s, m in zip(seq, mask)]

# Critical processing pipeline
raw_sensor_data = [12, 15, 23, 18, 9, 7, 31, 25, 14, 11, 19, 27]

# Step 1: Normalize sensor readings
normalized = normalize_readings(raw_sensor_data)

# Step 2: Generate bit-noise pattern (irrelevant)
noise_pattern = [bit_scramble(i, int(n)) for i, n in enumerate(normalized[:8])]

# Step 3: Create logical mask using threshold (relevant)
logical_mask = list(map(threshold_filter, normalized))

# Step 4: Apply mask to original data (red herring operation)
decoy_filtered = mask_data(raw_sensor_data, logical_mask)

# Step 5: Real processing — compute deviations above median
median_val = sorted(normalized)[len(normalized)//2]
deviations = [abs(n - median_val) for n in normalized if n > median_val]

# Step 6: Transform only positive contributions
transformed_signals = [math.log(d + 1) * 2 for d in deviations]

# Step 7: Simulate signal recombination (with unused branch)
if len(transformed_signals) % 2 == 0:
    pivot = len(transformed_signals) // 2
    left_part = transformed_signals[:pivot]
    right_part = [r * 1.1 for r in transformed_signals[pivot:]]
    combined = left_part + right_part
else:
    combined = transformed_signals  # never reached due to even length

# Step 8: Aggregate final result using lambda-based reduction
aggregator = lambda acc, val: acc + val ** 2
processed_data = [round(c, 3) for c in combined]

# Step 9: Final computation — this is the key statement
aggregate_result = lambda data: int(sum(map(aggregator, [0] + data[:-1], data)))
filtration_score = aggregate_result(processed_data)

# Print target result
print(f"Target result: {filtration_score}")