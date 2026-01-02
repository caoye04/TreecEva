def analyze_pattern(sequence, threshold=5):
    # Irrelevant transformation (distractor)
    temp_buffer = [x ** 0.5 for x in sequence if x > 0]
    
    # Semi-relevant pre-processing
    filtered = list(filter(lambda x: x % 2 == 1, sequence))
    
    # Key computation: count transitions above threshold
    spike_count = 0
    for i in range(1, len(sequence)):
        if sequence[i] > threshold and sequence[i-1] <= threshold:
            spike_count += 1

    # Dead code path (misleading)
    debug_state = None
    if len(temp_buffer) > 100:
        debug_state = sum(temp_buffer) // len(temp_buffer)

    return spike_count

# Secondary helper with slicing distraction
def shift_window(data, window_size=3):
    shifted = []
    for i in range(len(data)):
        # Slice-based context window
        window = data[max(0, i - window_size):i]
        if len(window) == window_size:
            shifted.append(sum(window) // window_size)
        else:
            shifted.append(0)
    
    # Unused result (irrelevant)
    reverse_scan = [x for x in data[::-1] if x < 7]
    
    return shifted

# Main processing chain
raw_data = [3, 8, 1, 9, 4, 7, 2, 6, 5]

# Apply pattern analysis
spike_analysis = analyze_pattern(raw_data, threshold=4)

# Bitwise manipulation layer (partially relevant)
masked_values = [x ^ 3 for x in raw_data]
sync_flag = sum(masked_values) & 1  # Used later

# Conditional transformation based on sync_flag
if sync_flag:
    processed_signal = [x * 2 for x in masked_values]
else:
    processed_signal = [x + 1 for x in masked_values]

# Window-based smoothing
smoothed = shift_window(processed_signal, window_size=2)

# Final aggregation with lambda folding
calculate_weight = lambda x: x * 1.5 if x > 8 else x * 0.8
intermediate_scores = [calculate_weight(val) for val in smoothed]

# Destructuring assignment (red herring)
first, *rest = intermediate_scores
offset_correction = first * 0.1

# Actual final score computation
baseline = sum(intermediate_scores) / len(intermediate_scores)
penalty = len([x for x in raw_data if x < 3]) * 1.5
final_score = int(baseline - penalty + spike_analysis)

print(f"Result: {final_score}")