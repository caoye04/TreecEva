def analyze_readings(sensor_readings):
    avg = sum(sensor_readings) / len(sensor_readings)
    deviations = [(x - avg) ** 2 for x in sensor_readings]
    variance = sum(deviations) / len(deviations)
    return avg, variance

sensor_data = [12, 15, 18, 14, 20, 16, 19, 17]
sample_timestamps = [100, 101, 102, 103, 104, 105, 106, 107]

# Misleading intermediate processing with irrelevant transformations
temp_offsets = [x % 5 for x in sample_timestamps]
adjusted_readings = [sensor_data[i] + temp_offsets[i] for i in range(len(sensor_data))]

def process_readings(data, threshold=15):
    above_threshold = [x for x in data if x > threshold]
    below_or_equal = [x for x in data if x <= threshold]
    ratio = len(above_threshold) / len(below_or_equal) if below_or_equal else 0
    return above_threshold, below_or_equal, ratio

# Initial analysis on raw data
raw_avg, raw_var = analyze_readings(sensor_data)
high_vals, low_vals, ratio_val = process_readings(sensor_data)

# Simulate redundant normalization (distractor)
normalized = [(x - raw_avg) / (raw_var ** 0.5) for x in sensor_data]
re_normalized = [abs(x) ** 0.5 for x in normalized]  # Unused path

# Core logic disguised among distractors
combined = list(zip(sensor_data, sample_timestamps))
enum_combined = list(enumerate(combined))

effective_values = []
for idx, (value, timestamp) in enum_combined:
    if value > raw_avg and timestamp % 2 == 0:
        effective_values.append(value * 1.1)
    elif value < raw_avg and timestamp % 2 == 1:
        effective_values.append(value * 0.9)
    else:
        effective_values.append(value)

# Secondary adjustment using enumerate for tracking
offset_map = {}
for i, val in enumerate(effective_values):
    offset_map[i] = val + (i * 0.05)

interim_result = [offset_map[k] for k in sorted(offset_map.keys())]

# Further distraction: tuple-based grouping
group_a = (x for x in interim_result if x < 16)
group_b = (x for x in interim_result if 16 <= x <= 18)
group_c = (x for x in interim_result if x > 18)

count_a = sum(1 for _ in group_a)
count_b = sum(1 for _ in group_b)  # Unused metric
count_c = sum(1 for _ in group_c)

def calculate_final_score(data):
    base = sum(data)
    penalty = count_a * 0.5
    bonus = len(high_vals) * 0.3
    score = base - penalty + bonus
    return int(score)

processed_data = interim_result
final_score = calculate_final_score(processed_data)
print(f"Target result: {final_score}")