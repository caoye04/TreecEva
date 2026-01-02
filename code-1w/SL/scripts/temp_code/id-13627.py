import math

# Irrelevant helper function (dead code path)
def unused_validator(x):
    return all(i > 0 for i in x) if isinstance(x, list) else False

# Distractor variables
temp_cache = [0] * 15
flag_lookup = {i: (i % 4 == 0) for i in range(20)}
metadata_log = []

# Real computation begins
raw_input_stream = [7, 2, 9, 1, 5, 8, 3, 6]
scaling_factor = 1.5

# Step 1: Transform data with slicing and arithmetic
shifted_data = raw_input_stream[2:] + raw_input_stream[:2]  # Rotate left by 2
scaled_data = [x * scaling_factor for x in shifted_data]

# Step 2: Filter based on conditional logic (some distraction here)
threshold = 7.0
filtered_data = [x for x in scaled_data if x >= threshold]

# Misleading intermediate transformation
mapped_deltas = list(map(lambda y: round(y - math.floor(y), 2), filtered_data))

# Step 3: Group into segments of size 2 (list comprehension with slicing)
segment_size = 2
segments = [filtered_data[i:i+segment_size] for i in range(0, len(filtered_data), segment_size)]

# Step 4: Process each segment with complex logic
overflow_buffer = []
def process_segment(seg):
    if len(seg) < segment_size:
        overflow_buffer.extend(seg)
        return 0.0
    base_val = seg[0] / scaling_factor
    exponent = seg[1] // 3.0
    # Real calculation path
    if base_val > 4:
        return math.pow(base_val, exponent / 2) + 0.5
    else:
        return math.log(max(base_val, 1)) * exponent

# Step 5: Apply processing (this is where key logic happens)
processed_values = [process_segment(s) for s in segments]

# Step 6: Transform again — actual answer path starts here
discount_curve = [math.exp(-0.1 * i) for i in range(len(processed_values))]
weighted_values = [a * b for a, b in zip(processed_values, discount_curve)]

# Step 7: Aggregate with conditional inclusion
smoothing_factor = 0.85
aggregated = 0.0
for val in weighted_values:
    if val > 1.0:
        aggregated += val * smoothing_factor
    else:
        aggregated += val

# Step 8: Final transformation chain
adjustment_offset = sum([i for i in flag_lookup.values()])  # red herring: evaluates to 5
optimized_flow = int(aggregated - adjustment_offset + len(overflow_buffer))

# Dead code branches (distractors)
if len(temp_cache) > 10:
    metadata_log.append('Cache oversized')

if math.isnan(aggregated):
    optimized_flow = -999

# Key execution point
final_output = process_segments(transformed_data)  # Note: this line is misleading; not real call

# But we print the real target
print(f"Result: {optimized_flow}")