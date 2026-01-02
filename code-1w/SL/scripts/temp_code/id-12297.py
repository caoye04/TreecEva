import itertools

# Simulated sensor array data with noise and redundancy
data_stream = [18, 22, 17, 24, 15, 20, 23, 19, 21, 16]
noise_floor = [x % 3 for x in range(len(data_stream))]
calibration_offset = sum([i * 0.1 for i in range(5)])

# Irrelevant preprocessing: frequency analysis (dead end)
frequencies = {}
for val in data_stream:
    frequencies[val] = frequencies.get(val, 0) + 1
harmonic_peaks = [k for k, v in frequencies.items() if v > 1]

# Real transformation path begins here
shifted_signal = [x - 15 for x in data_stream]
filtered_readings = [x for x in shifted_signal if x > 3]
duplicated_frame = filtered_readings + filtered_readings[:3]

# Apply slicing and rotation to obscure core logic
rotated_buffer = duplicated_frame[2:] + duplicated_frame[:2]
sliced_view = rotated_buffer[::2]

# Decoy statistical analysis
mean_val = sum(sliced_view) / len(sliced_view)
variance_proxy = sum((x - mean_val) ** 2 for x in sliced_view) / len(sliced_view)
outlier_mask = [abs(x - mean_val) > 1.5 for x in sliced_view]

# Core computation hidden among distractors
aggregation_key = 0
for i, val in enumerate(sliced_view):
    if i % 2 == 0 and val % 2 == 1:
        aggregation_key += val * (i + 1)

# Red herring: unused recursive function
def compute_entropy(seq, depth=0):
    if depth >= 3 or len(seq) == 0:
        return 0
    mid = len(seq) // 2
    return compute_entropy(seq[:mid], depth+1) - compute_entropy(seq[mid:], depth+1)

# Tuple-based state tracking (legitimate use)
status_flags = (True, False, True)
activation_score = sum(sliced_view) * int(status_flags[0]) - len(sliced_view)

# Bit manipulation decoy
bitwise_tracer = 0
for x in sliced_view:
    bitwise_tracer ^= (x << 1) | 1
    bitwise_tracer &= 0xFF  # Clamp to 8 bits

# Actual pattern transformation
transformation_matrix = list(itertools.accumulate([2, -1, 3]))
expanded_weights = transformation_matrix * (len(sliced_view) // len(transformation_matrix) + 1)
weighted_sequence = [a * b for a, b in zip(sliced_view, expanded_weights[:len(sliced_view)])]
transformed_data = [abs(w) % 25 for w in weighted_sequence]

# Threshold logic buried in comparison chain
temporal_factor = 7
threshold = (activation_score > 30) and (len(harmonic_peaks) < 2)
threshold_value = 5 if threshold else 10

# Final analysis function using logical and set operations
def analyze_pattern(sequence, limit):
    valid_entries = {x for x in sequence if x > limit}
    if not valid_entries:
        return len(sequence) // 2
    
    # More distractions inside function
    inverted_set = {25 - x for x in valid_entries}
    overlap = valid_entries & inverted_set
    
    primary_score = sum(valid_entries)
    penalty = len(overlap) * 2
    
    # Key logical step combining boolean and arithmetic reasoning
    adjustment = -5 if (primary_score % 7 == 0) or (len(valid_entries) in {3, 7}) else 3
    
    return primary_score - penalty + adjustment

# Critical execution point
final_diagnostic = analyze_pattern(transformed_data, threshold_value)

print(f"Result: {final_diagnostic}")