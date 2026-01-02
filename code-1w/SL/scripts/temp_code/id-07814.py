def analyze_trends(data_slice, threshold=10):
    trend_count = 0
    temp_sum = 0
    noise_counter = 0  # distractor
    for i in range(len(data_slice)):
        if data_slice[i] > threshold:
            trend_count += 1
            temp_sum += data_slice[i]
        else:
            noise_counter += 1  # irrelevant tracking
    average_spike = temp_sum / trend_count if trend_count > 0 else 0
    return trend_count, average_spike


def filter_outliers(raw_sequence):
    filtered = [x for x in raw_sequence if 5 <= x <= 100]
    outlier_gap = max(filtered) - min(filtered)  # semi-relevant
    return filtered[:len(filtered)//2], outlier_gap  # return half and gap


def calculate_final_score(dataset):
    segment_a, gap_a = filter_outliers(dataset)
    count_b, avg_b = analyze_trends(segment_a[::2], threshold=15)  # slicing + analysis
    
    # Distractor block: dead logic path
    debug_stats = {}
    if len(segment_a) > 100:
        debug_stats['oversize'] = True
    else:
        debug_stats['oversize'] = False  # never used
    
    shift_key = len(segment_a) & 7  # bitwise AND for no critical purpose
    adjusted_avg = avg_b + (shift_key * 0.25)
    
    # Core calculation
    base_metric = count_b * adjusted_avg
    penalty = 0
    for val in segment_a:
        if val < 15:
            penalty += 1
    final_score = int(base_metric - penalty)
    
    # Red herring: unused transformation
    normalized = [round(x / max(segment_a), 3) for x in segment_a]  # not used
    
    return final_score

# Simulated sensor readings
sensor_readings = [8, 12, 45, 67, 91, 3, 11, 22, 53, 68, 95, 102, 4, 14, 29, 77, 88, 103, 5, 13]

# Preprocessing with slicing
raw_subset = sensor_readings[1:15]
dummy_var = sum([x**2 for x in raw_subset]) / len(raw_subset)  # distraction: RMS-like calc
processed_data = raw_subset[::-1]  # reverse the list

final_score = calculate_final_score(processed_data)
print(f"Target result: {final_score}")