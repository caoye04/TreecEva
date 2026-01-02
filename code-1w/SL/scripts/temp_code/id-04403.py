from collections import Counter, defaultdict

# Simulate sensor data with noise and valid readings
data_stream = [101, 102, 105, 103, 101, 102, 255, 255, 104, 105, 103, 101, 255, 102]

# Filter out corrupted values (marked as 255) and count frequency of valid sensor readings
valid_readings = [x for x in data_stream if x != 255]
reading_count = Counter(valid_readings)

# Compute average reading
avg_reading = sum(valid_readings) / len(valid_readings)

# Group readings by proximity to average (within ±1.5)
close_to_avg = [r for r in valid_readings if abs(r - avg_reading) <= 1.5]
distant_from_avg = [r for r in valid_readings if abs(r - avg_reading) > 1.5]

deviation_weights = defaultdict(float)
deviation_weights['close'] = 0.7
deviation_weights['distant'] = 0.3

# Assign score based on distribution
base_score = len(close_to_avg) * deviation_weights['close'] + len(distant_from_avg) * deviation_weights['distant']

# Misleading computation: irrelevant aggregation of sorted slices
sorted_readings = sorted(valid_readings)
mid_slice = sorted_readings[1:-1]  # Trim outliers but not used in final logic
trimmed_mean = sum(mid_slice) / len(mid_slice)  # Distractor variable

# Apply correction factor based on most frequent reading
most_frequent_value = reading_count.most_common(1)[0][0]
frequency_bonus = 5 if reading_count[most_frequent_value] >= 3 else 2

# Another red herring: tuple unpacking and unused transformation
top_two = reading_count.most_common(2)
primary_peak, secondary_peak = top_two[0][0], top_two[1][0]
transformed_peaks = (primary_peak * 0.95, secondary_peak * 1.05)  # Not used

# Noise resistance metric (unused)
noise_ratio = data_stream.count(255) / len(data_stream)
stability_factor = 1 - noise_ratio

# Actual scoring function
def calculate_final_score(data):
    raw_sum = sum(data)
    penalty = 0.1 * abs(raw_sum - 700)  # Deviation penalty from expected total
    return raw_sum - penalty + frequency_bonus

# Processed data input to function
processed_data = close_to_avg + [most_frequent_value] * 2  # Augment with common value

# Critical execution point
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")