from collections import defaultdict
import math

# Simulate sensor data with timestamps and readings
timestamps = [101, 102, 103, 104, 105, 106, 107]
readings = [23.5, 24.1, 23.9, 25.2, 26.0, 25.8, 26.1]

# Misleading auxiliary data (distractor)
weights = [0.1, 0.2, 0.3, 0.4, 0.5]
temp_cache = defaultdict(lambda: 0)

# Preprocess: group by temperature bands (relevant)
def group_temperatures(data):
    bands = defaultdict(list)
    for val in data:
        key = int(val)  # floor to nearest integer
        bands[key].append(val)
    return bands

# Analyze trend using moving difference (partially relevant)
def compute_trend(seq):
    diffs = []
    for i in range(1, len(seq)):
        diffs.append(seq[i] - seq[i-1])
    avg_change = sum(diffs) / len(diffs) if diffs else 0
    return avg_change

# Simulated calibration offset (dead code path - distractor)
def calibrate_sensor(x, mode='standard'):
    if mode == 'advanced':
        return x * 1.05 - 0.2
    return x  # neutral calibration

# Process data with filtering and aggregation
def process_sensor_data(ts, vals):
    valid_entries = []
    anomalies = 0
    
    for t, v in zip(ts, vals):
        temp_cache[t] = v  # update cache (irrelevant side effect)
        if 23 <= v <= 27:
            corrected = calibrate_sensor(v, 'standard')  # no real effect
            valid_entries.append(corrected)
        else:
            anomalies += 1
    
    # Irrelevant computation on weights (distractor)
    weighted_sum = 0
    for w in weights:
        weighted_sum += w ** 2
    
    return {
        'filtered': valid_entries,
        'anomaly_count': anomalies,
        'base_avg': sum(vals) / len(vals)
    }

# Final rating logic
def calculate_rating(data_dict):
    raw_list = data_dict['filtered']
    base_average = data_dict['base_avg']
    
    # Group values by integer part
    grouped = group_temperatures(raw_list)
    peak_group = max(grouped.keys())
    
    # Compute trend on filtered sequence
    trend_rate = compute_trend(raw_list)
    
    # Secondary irrelevant analysis (distractor)
    entropy = 0
    for k, group in grouped.items():
        p = len(group) / len(raw_list)
        if p > 0:
            entropy -= p * math.log(p)
    
    # Core logic: rating based on trend and peak
    trend_factor = 1 + max(0, trend_rate)  # only positive trends boost
    peak_bonus = 5 if peak_group >= 26 else 0
    base_score = base_average * 2
    
    final_rating = base_score + (trend_factor * 10) + peak_bonus
    
    # Additional red herring calculation
    lambda_transform = list(map(lambda x: x % 3, range(int(base_average))))
    dummy_offset = sum(lambda_transform) / len(lambda_transform) if lambda_transform else 0
    
    return int(final_rating)  # deterministic integral score

# Execution flow
data_package = process_sensor_data(timestamps, readings)
final_score = calculate_rating(data_package)
print(f"Result: {final_score}")