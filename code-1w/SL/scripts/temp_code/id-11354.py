def analyze_pattern(sequence):
    temp_sum = 0
    control_flag = False
    for i in range(len(sequence)):
        if i % 3 == 0 and sequence[i] > 5:
            temp_sum += sequence[i] * 2
        elif i % 4 == 0:
            temp_sum -= 1
        if sequence[i] % 7 == 0:
            control_flag = True
    return temp_sum + (7 if control_flag else 0)


def filter_outliers(values):
    mean_val = sum(values) / len(values)
    deviation_scores = [(v - mean_val) ** 2 for v in values]
    threshold = sum(deviation_scores) / len(deviation_scores)
    cleaned = [v for v in values if (v - mean_val) ** 2 <= threshold]
    return cleaned if len(cleaned) > 0 else [0]


def process_segment(raw_data):
    offset = len(raw_data) // 2
    data_slice = raw_data[offset:] + raw_data[:offset]  # Rotate using slicing
    
    # Irrelevant transformation
    noise_correction = 0
    for x in raw_data:
        if x < 0:
            noise_correction += x ^ 5  # Bitwise distractor
    
    # Semi-relevant preprocessing
    adjusted = [x + 1 for x in data_slice if x % 2 == 1]  # Only odd numbers incremented
    
    # Distractor: unused intermediate
    stats_snapshot = {
        'max': max(adjusted) if adjusted else 0,
        'min': min(adjusted) if adjusted else 0,
        'count': len(adjusted)
    }
    
    # Core logic path
    if len(adjusted) >= 3:
        sample_window = adjusted[1:4]  # Slicing operation
        base_score = analyze_pattern(sample_window)
        outlier_free = filter_outliers(sample_window)
        refinement = sum(outlier_free) & 15  # Bitwise AND as minor modifier
        final_output = base_score * 3 + refinement
    else:
        final_output = sum(adjusted) * 5
    
    # Dead code path (not taken due to structure)
    if False:
        fallback = 0
        for item in data_slice:
            fallback ^= item | 3
        final_output = fallback

    return final_output

# Main execution
sensor_readings = [4, 7, 8, 14, 6, 9, 11, 21, 3]
data_slice = sensor_readings[2:8]
final_output = process_segment(data_slice)
print(f"Target result: {final_output}")