def analyze_trends(data_sequence):
    trend_flags = {}
    upward = sum(1 for i in range(1, len(data_sequence)) if data_sequence[i] > data_sequence[i-1])
    downward = sum(1 for i in range(1, len(data_sequence)) if data_sequence[i] < data_sequence[i-1])
    stable = sum(1 for i in range(1, len(data_sequence)) if data_sequence[i] == data_sequence[i-1])
    
    trend_flags['upward'] = upward > downward
    trend_flags['volatile'] = (upward + downward) > 2 * stable
    trend_flags['consistency'] = abs(upward - downward) <= 2
    
    # Distractor: irrelevant transformation
    temp_normalized = [x / max(data_sequence) for x in data_sequence]
    entropy_proxy = 0
    for val in temp_normalized:
        if val > 0.5:
            entropy_proxy += 1
    
    return trend_flags


def extract_segments(raw_data, window_size=3):
    segments = []
    for i in range(len(raw_data) - window_size + 1):
        segment = raw_data[i:i+window_size]
        segments.append(segment)
    
    # Distractor: dead code path with unused computation
    if len(raw_data) % 2 == 0 and False:  # Simulated dead branch
        mirror_image = raw_data[::-1]
        segments.append(mirror_image[:window_size])
    
    return segments


def compute_final_score(flags_dict):
    base = 50
    if flags_dict.get('upward'):
        base += 20
    if flags_dict.get('volatile'):
        base -= 10
    if flags_dict.get('consistency'):
        base += 35
    return base

# Main execution
sensor_readings = [104, 107, 105, 108, 110, 109, 111, 113, 112, 114]

# Irrelevant preprocessing (distractor)
filtered_readings = [x for x in sensor_readings if x > 100]
sorted_readings = sorted(filtered_readings, reverse=True)
mean_value = sum(sorted_readings) / len(sorted_readings)
median_index = len(sorted_readings) // 2
median_value = sorted_readings[median_index]

# Actual relevant processing
trend_analysis = analyze_trends(sensor_readings)
all_segments = extract_segments(sensor_readings)

# Key computation
processed_data = trend_analysis
final_score = compute_final_score(processed_data)

# Additional misleading variables
peak_rate = max(sensor_readings) - min(sensor_readings)
fluctuation_index = peak_rate / mean_value if mean_value else 0

# Output result
Result: {final_score}