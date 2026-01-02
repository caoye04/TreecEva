from itertools import combinations

# Simulate sensor readings with calibration offsets
def collect_readings():
    raw_data = [105, 98, 110, 95, 102]
    calibrated = [x - 10 for x in raw_data]
    return calibrated

# Apply environmental correction based on time of day
def correct_for_time(readings, hour):
    if 6 <= hour < 12:
        factor = 1.05
    elif 12 <= hour < 18:
        factor = 0.95
    else:
        factor = 1.0
    return [round(x * factor, 2) for x in readings]

# Filter anomalies using simple statistical threshold
def filter_anomalies(data):
    mean_val = sum(data) / len(data)
    deviances = [(x - mean_val) ** 2 for x in data]
    variance = sum(deviances) / len(deviances)
    std_dev = variance ** 0.5
    return [x for x in data if abs(x - mean_val) <= 2 * std_dev]

# Compute weighted aggregate with normalization
def compute_aggregate(values, weights):
    normalized_weights = [w / sum(weights) for w in weights]
    weighted_sum = sum(v * w for v, w in zip(values, normalized_weights))
    return round(weighted_sum, 2)

# Auxiliary function to generate weight patterns (not fully used)
def generate_weight_patterns(n):
    patterns = []
    for i in range(1, n+1):
        pattern = [j % i + 1 for j in range(n)]
        patterns.append(pattern)
    return patterns

# Main processing pipeline
readings = collect_readings()
corrected = correct_for_time(readings, hour=14)
filtered = filter_anomalies(corrected)

# Generate extraneous data
all_combinations = list(combinations(filtered, 2))
distorted_readings = [x * 1.1 + 3 for x in readings]  # Irrelevant transformation

# Weight vector – only the first few weights matter
base_weights = [3, 2, 4, 1, 3]
weight_patterns = generate_weight_patterns(5)
primary_weights = weight_patterns[2]  # [1, 2, 0, 1, 2]

# Final computation step
results = filtered[:len(primary_weights)]  # Truncate results to match weight length
final_score = compute_aggregate(results, primary_weights)

# Print result as required
print(f"Result: {final_score}")