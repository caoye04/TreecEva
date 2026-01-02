from collections import Counter, defaultdict

# Simulate sensor data with noise and valid readings
def process_sensor_data(raw_readings):
    filtered_readings = [x for x in raw_readings if 10 <= x <= 100]
    outlier_count = len(raw_readings) - len(filtered_readings)
    average_value = sum(filtered_readings) / len(filtered_readings) if filtered_readings else 0
    
    # Misleading computation: not used later
    temp_adjustment = 0
    for val in filtered_readings:
        if val > 90:
            temp_adjustment += 0.5
    
    normalized = [round((x - average_value) * 1.5, 2) for x in filtered_readings]
    return normalized, outlier_count, average_value

# Analyze pattern frequency in adjusted data
def analyze_patterns(data_sequence):
    seq_str = ''.join(str(int(abs(x))) for x in data_sequence)
    freq_counter = Counter(seq_str)
    most_common_digit = freq_counter.most_common(1)[0][1] if freq_counter else 0
    
    # Distractor: complex but unused structure
    digit_map = defaultdict(list)
    for i, d in enumerate(seq_str):
        digit_map[d].append(i)
    
    pattern_score = sum(min(len(positions), 5) for positions in digit_map.values())
    return pattern_score

# Main scoring logic
def calculate_final_score(data):
    base_score = sum(abs(x) for x in data)
    length_bonus = len(data) * 2 if len(data) > 5 else 0
    
    # Extra distraction: irrelevant conditional chain
    adjustment_factor = 1.0
    if base_score > 100:
        adjustment_factor *= 0.9
    elif base_score > 50:
        adjustment_factor *= 1.1
    else:
        adjustment_factor *= 1.05
    
    instability_metric = max(data) - min(data) if len(data) > 1 else 0
    penalty = 10 if instability_metric > 20 else 0
    
    final_score = int((base_score + length_bonus) - penalty)
    return final_score

# Simulated input: sensor readings with noise
raw_sensor_data = [5, 15, 23, 45, 67, 89, 92, 105, -3, 76, 88, 95]

# Processing pipeline
processed_data, dropped, avg = process_sensor_data(raw_sensor_data)
pattern_complexity = analyze_patterns(processed_data)
final_score = calculate_final_score(processed_data)

# Additional red herring computations
reversed_data = processed_data[::-1]
checksum = sum(reversed_data[i] * (i+1) for i in range(len(reversed_data)))
summary_report = f'Data points: {len(processed_data)}, Dropped: {dropped}'

print(f'Result: {final_score}')