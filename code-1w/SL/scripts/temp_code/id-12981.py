import math

# Irrelevant helper function (dead code path)
def unused_signal_filter(x):
    return [val for val in x if val % 3 != 0]

# Decoy transformation with misleading intermediate results
def decoy_enhance(seq):
    shifted = [(x >> 2) ^ 5 for x in seq]
    return [s * s for s in shifted if s > 0]  # never used

# Real data preprocessing with bit manipulation and list comprehension
def preprocess readings(raw):
    masked = [r & 0xFF for r in raw]  # Apply byte mask
    scaled = [round(v * 1.75, 2) for v in masked]
    return [s for s in scaled if s > 50]  # Filter low signals

# Conditional transformation based on parity pattern
def transform_entry(val):
    if val % 2 == 0:
        return int(val / 2) ^ 15
    else:
        return (val + 5) * 3

# Core transformation using list comprehension and conditional logic
def apply_transformation(data):
    result = []
    for item in data:
        transformed = transform_entry(item)
        result.append(transformed)
    return result

# Red herring: complex but unused recursive function
def recursive_denoise(samples, depth=0):
    if depth >= 3 or len(samples) < 2:
        return samples[0] if samples else 0
    mid = len(samples) // 2
    left = recursive_denoise(samples[:mid], depth + 1)
    right = recursive_denoise(samples[mid:], depth + 1)
    return (left ^ right) + depth  # interesting but irrelevant

# Real analysis function that computes final result
def analyze_pattern(pattern):
    base_sum = sum(pattern)
    adjustment = 0
    for i, p in enumerate(pattern):
        if i % 3 == 0:
            adjustment += math.sin(p * 0.1)
        elif i % 3 == 1:
            adjustment -= math.cos(p * 0.05)
    score = base_sum + round(adjustment * 100, 2)
    outlier_count = len([x for x in pattern if x > 100])
    return int(score - (outlier_count * 12))

# Simulated sensor readings (input data)
sensor_readings = [204, 101, 135, 67, 240, 89, 178, 112]

# Step 1: Preprocess the raw sensor data
filtered_data = preprocess(sensor_readings)

# Step 2: Apply main transformation (key processing step)
transformed_data = apply_transformation(filtered_data)

# Step 3: Perform diagnostic analysis (target execution point)
final_diagnostic = analyze_pattern(transformed_data)

# Irrelevant sorting of a derived copy
sorted_temp = sorted([x + 10 for x in transformed_data], reverse=True)

# Unused combinatoric calculation (distractor)
total_pairs = 0
for i in range(len(transformed_data)):
    for j in range(i + 1, len(transformed_data)):
        total_pairs += (transformed_data[i] & transformed_data[j]) % 7

# Final output (must print the target variable)
print(f"Result: {final_diagnostic}")