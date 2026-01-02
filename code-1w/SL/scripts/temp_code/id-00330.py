def preprocess_sequence(seq):
    return [x for x in seq if x > 0]

def generate_signature(data):
    signature = 0
    for val in data:
        signature ^= val  # Bitwise XOR accumulation
    return signature

def filter_anomalies(raw_data, limit):
    cleaned = []
    for x in raw_data:
        if x < limit:
            cleaned.append(x)
    return cleaned

# Irrelevant helper function (dead code path)
def deprecated_calculate_entropy(arr):
    import math
    counts = {}
    for item in arr:
        counts[item] = counts.get(item, 0) + 1
    entropy = 0
    total = len(arr)
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

# Main diagnostic workflow
signal_input = [12, -5, 8, 19, 3, 7, -1, 4, 11, 6]
baseline_offset = 3
amplitude_correction = 1.5

# Step 1: Preprocess to remove non-positive values
filtered_signal = preprocess_sequence(signal_input)

# Step 2: Apply amplitude correction (irrelevant to final result)
corrected_magnitude = [round(x * amplitude_correction) for x in filtered_signal]

# Step 3: Generate working pattern buffer using bit shifting
pattern_buffer = []
for val in corrected_magnitude:
    shifted = (val << 1) - baseline_offset  # Left shift and adjust
    pattern_buffer.append(shifted)

# Step 4: Define threshold logic using set operations
threshold_set = set(range(10, 25))
complement_zone = set(range(30, 50))  # Unused distractor set
emergency_bounds = {x for x in complement_zone if x % 4 == 0}  # Dead code

# Step 5: Count occurrences in critical bands (some irrelevant)
high_band_count = 0
mid_band_count = 0
for val in pattern_buffer:
    if val > 20:
        high_band_count += 1
    if val > 10 and val < 25:
        mid_band_count += 1

# Step 6: Simulate redundant state tracking (distractor)
current_state = {'stage': 'diagnostic', 'retry_count': 0}
state_history = []
for i in range(2):
    current_state['retry_count'] += 1
    state_history.append(current_state.copy())

# Step 7: Analyze signal using set intersection and conditional logic
def analyze_signal(sequence, thresholds):
    seq_set = set(sequence)
    active_triggers = seq_set & thresholds  # Set intersection
    
    # Compute diagnostic score based on bit patterns and counts
    base_score = len(active_triggers) * 7
    bonus = 0
    for val in active_triggers:
        if val % 2 == 1:
            bonus += (val & 7)  # Bitwise AND with 7
    
    # Additional red herring computation
    phantom_metric = 0
    temp_vals = [x ^ 5 for x in sequence]  # XOR transformation (unused)
    for v in temp_vals:
        if v in emergency_bounds:  # Unreachable due to value ranges
            phantom_metric += 1
    
    # Final logic
    if len(seq_set) > 5:
        bonus += 3
    return base_score + bonus

# Execute key statement
final_diagnostic = analyze_signal(pattern_buffer, threshold_set)

# Print result for extraction
print(f"Result: {final_diagnostic}")