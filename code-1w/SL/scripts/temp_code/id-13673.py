import math

# Irrelevant helper function (dead code path)
def compute_legacy_score(values):
    return sum(v ** 0.5 for v in values if v % 2 == 0)

# Distractor variables
temp_cache = [0] * 100
legacy_threshold = 42.5
junk_data = list(range(50, 70))

# Real data pipeline
raw_input = [3, 7, 12, 15, 21, 24, 30, 36]

# Step 1: Filter relevant elements using slicing and condition
filtered = raw_input[1:-1]  # Remove first and last

# Step 2: Transform with lambda and trigonometric mapping
dynamic_weights = list(map(lambda x: math.sin(x / 10) + 1.5, filtered))

# Step 3: Pair with indices and apply conditional scaling
indexed = [(i, v * dynamic_weights[i]) for i, v in enumerate(filtered)]
scaled_values = []
for idx, val in indexed:
    if idx % 2 == 0:
        scaled_values.append(val * 1.2)
    else:
        scaled_values.append(val * 0.8)

# Step 4: Apply moving average filter (window size 2)
moving_avg = []
for i in range(len(scaled_values) - 1):
    moving_avg.append((scaled_values[i] + scaled_values[i+1]) / 2)

# Step 5: Extract every second element using slicing
sampled = moving_avg[::2]

# Step 6: Normalize to reference baseline
baseline = sum(sampled) / len(sampled)
normalized = [x / baseline for x in sampled]

# Step 7: Quantize using floor with offset
quantized = [int(x * 100 + 0.5) for x in normalized]

# Step 8: Simulate checksum validation (irrelevant logic branch)
current_checksum = sum(quantized[i] * (i + 1) for i in range(len(quantized))) % 1000
expected_checksum = 887
is_valid = current_checksum == expected_checksum  # Always false, distractor

# Step 9: Transform via bit manipulation (XOR with prime)
prime_mask = 211
masked = [q ^ prime_mask for q in quantized]

# Step 10: Aggregate using min/max/avg combo heuristic
min_val = min(masked)
max_val = max(masked)
avg_val = sum(masked) / len(masked)
aggregate_score = (min_val + max_val + avg_val) / 3

# Step 11: Clamp and round to nearest integer
clamped = int(round(max(0, min(10000, aggregate_score))))

# Step 12: Final processing step — key execution point
def process_chunk(data):
    # Irrelevant pre-check
    if any(d < 0 for d in data):
        return -1
    # Actual transformation chain
    squared_sum = sum(x * x for x in data)
    root_val = int(math.sqrt(squared_sum))
    # Double hash with string conversion (uses string method)
    str_hash = str(root_val).zfill(6)
    second_hash = str_hash[::-1]  # String slicing reverse
    return int(second_hash[:3]) + int(second_hash[3:])

def transform_data(seq):
    # Unused transformation (red herring)
    return [s >> 2 for s in seq]

def cleanup_buffer(buf):
    # Dead function, never called
    return [b for b in buf if b % 3 != 0]

# Key assignment statement
transformed_data = masked
final_output = process_chunk(transformed_data)

# Output result
print(f"Result: {final_output}")