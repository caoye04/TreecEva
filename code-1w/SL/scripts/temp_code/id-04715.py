def analyze_pattern(sequence, threshold=0.75):
    """ Analyze sequence for hidden patterns (distractor function) """
    count = 0
    for i in range(len(sequence) - 1):
        if sequence[i] < sequence[i+1]:
            count += 1
    ratio = count / (len(sequence) - 1) if sequence else 0
    return ratio > threshold

# Irrelevant data structures (red herrings)
data_log = [0.1, 0.3, 0.6, 0.8, 0.9, 1.2, 1.5]
scaling_factors = [2**i for i in range(8)]
temp_buffer = {k: v for k, v in enumerate([x * 0.05 for x in range(7)])}

# Core computation setup (only part actually used)
def preprocess_input(raw_values):
    cleaned = []
    for idx, val in enumerate(raw_values):
        if idx % 2 == 0:
            cleaned.append(val + 1.5)
        else:
            cleaned.append(val - 0.5)
    return cleaned

def transform_coordinates(x_list, y_list):
    # Unused transformation (dead path)
    return [a * b for a, b in zip(x_list, y_list)]

# Key recursive function with distractors
def compute_weighted_depth(arr, depth=0, multiplier=1.0):
    if depth >= 3 or not arr:
        return 0.0
    
    total = 0.0
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Real work happens here
    for i, (pos, val) in enumerate(enumerate(arr)):
        if i % 3 == 0:
            total += val * (multiplier + depth)
    
    # Recursive calls contribute marginally
    recursive_contribution = (
        compute_weighted_depth(left_half, depth + 1, multiplier * 0.5) +
        compute_weighted_depth(right_half, depth + 1, multiplier * 0.3)
    )
    
    return total + recursive_contribution * 0.1

# Decoy accumulator (misleading intermediate result)
cumulative_trace = 0
for t in data_log:
    cumulative_trace += t ** 2

# Main processing pipeline
raw_input_stream = [4, -2, 7, 1, 8, 3]
processed_data = preprocess_input(raw_input_stream)

# Secondary irrelevant transformation
shifted_data = [x >> 1 for x in raw_input_stream if x > 0]  # Bitwise distraction

# Real aggregation logic
summation_anchor = 0
for index, value in enumerate(processed_data):
    if value > 3.0:
        summation_anchor += value * (index + 1)

# Control flow with logical operations and comparisons
flag_state = (summation_anchor > 10) and not (len(shifted_data) < 2)
override_mode = False or (False and True)  # Obvious false, distractor

if flag_state and not override_mode:
    base_metric = summation_anchor
else:
    base_metric = 5.5

# Complex data restructuring using enumerate and zip
indexed_grid = list(enumerate(processed_data))
pair_mapping = list(zip(processed_data[:-1], processed_data[1:]))

# Final calculation chain
aggregation_key = 0
for i, (a, b) in enumerate(pair_mapping):
    diff = abs(a - b)
    if diff > 1.0 and (i + 1) % 2 == 1:
        aggregation_key += diff * 1.5

auxiliary_score = compute_weighted_depth(processed_data)

# Final composite score (this is the real answer)
final_score = int(base_metric + aggregation_key - 2.0 + auxiliary_score * 0.5)

# Output target result
print(f"Target result: {final_score}")