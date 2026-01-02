from itertools import groupby

def analyze_segments(data):
    segments = []
    for k, g in groupby(data, key=lambda x: x > 0):
        segments.append(list(g))
    positive_parts = [seg for seg in segments if sum(seg) > 0]
    return positive_parts

# Irrelevant helper function (distractor)
def compute_magnitude(vector):
    return sum(x ** 2 for x in vector) ** 0.5

# Main data processing pipeline
data_input = [3, -1, -2, 4, 5, -3, 2, 2, -4, -5, 1, 1, 1]

# Step 1: Normalize data by shifting mean to zero
mean_val = sum(data_input) / len(data_input)
shifted_data = [x - mean_val for x in data_input]

# Step 2: Discretize into integer bins (simulates sensor rounding)
discretized_data = [int(round(x)) for x in shifted_data]

# Step 3: Remove zero values (noise filtering)
filtered_data = [x for x in discretized_data if x != 0]

# Step 4: Detect and extract positive segments
processed_data = analyze_segments(filtered_data)

# Step 5: Flatten the first two valid segments (if exist)
flattened_part = []
if len(processed_data) >= 2:
    flattened_part = processed_data[0] + processed_data[1]
else:
    flattened_part = processed_data[0] if processed_data else []

# Step 6: Compute cumulative product with modular adjustment
cumprod = 1
modulus = 97
for val in flattened_part:
    cumprod = (cumprod * abs(val)) % modulus
    if cumprod == 0:
        cumprod = 1  # Avoid collapsing

# Step 7: Calculate final score using weighted transform
weight_factor = len(flattened_part) ** 1.5 if flattened_part else 0
transform_bias = sum(x for x in flattened_part if x % 2 == 0)
final_score = int(cumprod + weight_factor - transform_bias)

# Irrelevant string computation (distractor)
status_msg = "Processing complete"
status_code = status_msg.upper().replace(" ", "_")
log_entry = f"Status: {status_code} | Count: {len(data_input)}"

# Output the required result
print(f"Result: {final_score}")