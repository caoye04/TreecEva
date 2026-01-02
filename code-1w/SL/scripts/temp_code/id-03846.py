from collections import defaultdict, Counter
import itertools

# Simulate sensor readings with some noise and redundancy
def generate_sensor_data():
    raw_readings = [15, 18, 15, 20, 22, 18, 25, 22, 20, 15]
    timestamps = list(range(10))
    return list(zip(timestamps, raw_readings))

# Filter out unstable readings (noise) using sliding window
def filter_stable_readings(data):
    stable = []
    for i in range(1, len(data) - 1):
        prev_val = data[i-1][1]
        curr_val = data[i][1]
        next_val = data[i+1][1]
        if abs(curr_val - prev_val) <= 5 and abs(curr_val - next_val) <= 5:
            stable.append(curr_val)
    return stable

# Transform data by grouping repeated values
def transform_readings(values):
    grouped = defaultdict(int)
    for k, g in itertools.groupby(sorted(values)):
        grouped[k] += len(list(g))
    return grouped

# Analyze frequency distribution to detect dominant mode
def analyze_distribution(groups):
    counter = Counter(groups)
    most_freq_value = counter.most_common(1)[0][0] if counter else 0
    total_unique = len(counter)
    # Distractor computation: irrelevant entropy-like measure
    entropy = sum(-(v/sum(counter.values())) * (v/sum(counter.values())) for v in counter.values()) if counter else 0
    return most_freq_value, entropy, total_unique

# Calculate final diagnostic score based on processed data
def calculate_final_score(data_dict):
    values = list(data_dict.keys())
    base_score = sum(v * data_dict[v] for v in values)
    adjustment = len(values) * 2
    # Red herring calculation: unused health metric
    health_metric = (base_score / (adjustment or 1)) > 5
    stability_factor = data_dict.get(max(values), 0)
    final_score = base_score + adjustment - stability_factor
    return int(final_score)

# Main execution pipeline
sensor_data = generate_sensor_data()
filtered_readings = filter_stable_readings(sensor_data)
processed_groups = transform_readings(filtered_readings)
mode_value, _, unique_count = analyze_distribution(processed_groups)
temp_correction = (unique_count * 3) // 2  # Unused correction factor (distractor)
final_score = calculate_final_score(processed_groups)
print(f"Result: {final_score}")