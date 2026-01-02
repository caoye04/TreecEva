from collections import defaultdict, Counter

# Simulate sensor data with noise and redundant readings
def generate_sensor_readings():
    raw_data = [15, 17, 15, 18, 20, 17, 19, 15, 21, 18, 17, 16, 15, 20]
    timestamps = list(range(len(raw_data)))
    return list(zip(timestamps, raw_data))

def filter_outliers_and_aggregate(data):
    # Irrelevant statistics (distractor)
    total_entries = len(data)
    sum_values = sum(val for _, val in data)
    avg_value = sum_values / total_entries if total_entries else 0
    
    # Actual processing: count frequency of values above threshold
    filtered_values = [val for _, val in data if val > 16]
    freq = Counter(filtered_values)
    
    # Extra distraction: unused transformation
    squared_map = {k: v**2 for k, v in freq.items()}
    
    return freq

def compute_entropy(frequency_dict):
    import math
    total = sum(frequency_dict.values())
    if total == 0:
        return 0.0
    entropy = 0.0
    for count in frequency_dict.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

def normalize_scores(freq_dict, entropy_val):
    base_score = 0
    multiplier = int(entropy_val * 10)  # Scale entropy to influence score
    for val, count in freq_dict.items():
        if count >= 2:
            base_score += val * count
    # Distractor calculations
    temp_adjustment = 0
    for i in range(3):
        temp_adjustment += (i + 1) * 5  # Unused loop
    unused_flag = False
    if temp_adjustment > 10:
        unused_flag = True  # Dead code branch
    return base_score * multiplier

def calculate_final_score(data_list):
    # Track state across multiple stages
    state_log = defaultdict(int)
    cumulative_shift = 0
    
    for item in data_list:
        state_log[item] += 1
        cumulative_shift ^= item  # Bitwise distraction
    
    # Core logic hidden among side operations
    main_value = sum(state_log.keys())
    shift_influence = cumulative_shift & 0xF  # Use lower 4 bits
    
    return main_value + shift_influence

# Main execution flow
data_readings = generate_sensor_readings()
processed_freq = filter_outliers_and_aggregate(data_readings)
entropy_metric = compute_entropy(processed_freq)
normalized_result = normalize_scores(processed_freq, entropy_metric)

# Key statement
final_score = calculate_final_score(list(processed_freq.keys()))
print(f"Result: {final_score}")