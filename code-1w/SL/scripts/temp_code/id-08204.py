from collections import defaultdict

# Simulate sensor data processing with noise filtering and performance scoring
def preprocess_metrics(raw_readings):
    filtered = []
    noise_floor = 0.1
    for val in raw_readings:
        if abs(val) > noise_floor:
            filtered.append(abs(val))
    return sorted(filtered, reverse=True)

# Misleading helper: appears useful but not critical
def calculate_entropy(data):
    from math import log2
    freq = defaultdict(int)
    for x in data:
        freq[x] += 1
    total = len(data)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 4)

# Core evaluation logic
def evaluate_performance(metrics, threshold):
    # Distractor: unused intermediate
    temp_buffer = [x * 1.5 for x in metrics if x < 5]
    
    # Actual signal: count how many exceed dynamic threshold
    boosted = list(map(lambda x: x * 1.2, metrics))
    above_threshold = [b for b in boosted if b >= threshold]
    
    # Secondary filter based on position (index condition)
    significant = []
    for i, val in enumerate(boosted):
        if val >= threshold and i % 2 == 0:
            significant.append(val)
    
    # Bonus rule: if more than 3 values pass, add multiplier
    bonus_applied = False
    score = len(significant) * 10
    if len(above_threshold) > 3:
        score *= 1.5
        bonus_applied = True
    
    # Dead code path - never executed due to logic above
    if bonus_applied and False:
        correction = sum(temp_buffer) / 100
        score -= correction

    return int(score)

# Input data
raw_sensor_data = [0.5, -0.3, 0.9, 0.05, -0.02, 1.2, 0.8, 1.1, 0.4]
base_threshold = 1.0

# Processing pipeline
cleaned = preprocess_metrics(raw_sensor_data)
entropy_value = calculate_entropy(cleaned)  # Computed but not used
metric_data = [x * 1.1 for x in cleaned]  # Further transformation

# Critical statement
final_score = evaluate_performance(metric_data, base_threshold)

print(f"Result: {final_score}")