def analyze_pattern(sequence, threshold):
    count = 0
    for val in sequence:
        if val > threshold:
            count += 1
    return count


def extract_features(data_slice):
    magnitude = sum(abs(x) for x in data_slice)
    norm_factor = len(data_slice) if data_slice else 1
    return magnitude / norm_factor


def process_segments(raw_data, index):
    # Relevant slicing and processing
    left_segment = raw_data[:index]
    right_segment = raw_data[index+1:]
    mid_value = raw_data[index] if index < len(raw_data) else 0

    # Distractor: unused feature extraction
    _ = extract_features(left_segment)
    _ = extract_features(right_segment)

    # Real logic begins
    active_count = 0
    if len(left_segment) >= 3:
        sliced_portion = left_segment[1:-1]  # Remove first and last
        temp_sum = sum(sliced_portion)
        if temp_sum > mid_value:
            active_count += 2
    
    if len(right_segment) > 0:
        max_right = max(right_segment)
        min_left = min(left_segment) if left_segment else 0
        diff = max_right - min_left
        if diff > mid_value * 2:
            active_count += 3

    # Distractor: irrelevant counting
    zero_count = sum(1 for x in raw_data if x == 0)
    _ = zero_count  # Not used

    # Conditional branch based on character-like logic (simulated)
    flag_char = 'X'
    char_code = ord(flag_char)
    if char_code % 2 == 0:
        active_count += 1

    # Final aggregation
    base_score = sum(raw_data) // len(raw_data) if raw_data else 0
    final_tally = base_score + active_count

    # Distractor: dead code path
    if False:
        fallback = 999
        final_tally = fallback

    return final_tally

# Main execution
sensor_readings = [4, 7, 2, 9, 5, 8, 6]
pivot_index = 3
baseline_check = analyze_pattern(sensor_readings, 6)
_ = baseline_check  # Unused analysis

final_tally = process_segments(sensor_readings, pivot_index)
print(f"Result: {final_tally}")