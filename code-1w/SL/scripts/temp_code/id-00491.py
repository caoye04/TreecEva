import math

# Simulated sensor data with noise and redundant readings
data_stream = [3.5, 2.1, -1.2, 4.4, 5.9, -0.3, 6.7, 2.2, 8.1, 9.6, 0.5, 1.3, 7.4, 3.9, 6.6]

# Irrelevant transformations (distractor)
shifted_data = [x + 0.1 for x in data_stream if x > 0]
normalized = [round((x - min(data_stream)) / (max(data_stream) - min(data_stream)), 3) for x in data_stream]

# Bit manipulation red herring (no impact on final result)
def decoy_transform(values):
    return [int(x) ^ 5 for x in values if x % 2 == 0]

decoys = decoy_transform([10, 20, 30])

# Conditional filtering based on threshold and pattern
threshold = 2.0
valid_indices = [i for i, x in enumerate(data_stream) if x >= threshold]

# Extract segments using slicing — relevant operation
segment_a = data_stream[2:9]
segment_b = data_stream[-5:]
combined_segments = segment_a + segment_b

# Redundant aggregation functions (distraction)
mean_val = sum(data_stream) / len(data_stream)
median_val = sorted(data_stream)[len(data_stream)//2]
mode_approx = max(set(data_stream), key=data_stream.count)

# Misleading intermediate filter (not used in final path)
temp_filtered = [x for x in combined_segments if math.sin(x) > 0]

# Actual computation path begins here
primary_candidates = [x for x in data_stream if x >= 3.0]  # Key selection
scaled = [x * 1.5 for x in primary_candidates]            # Transformation
rounded_vals = [round(x) for x in scaled]                 # Discretization

# Further filtering based on parity after rounding
filtered_data = [x for x in rounded_vals if x % 2 == 1]

# Critical statement
filtered_sum = sum(filtered_data)

print(f"Result: {filtered_sum}")