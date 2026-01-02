from itertools import combinations

# Simulate sensor readings with noise and validity flags
raw_sensors = [
    (12.5, True), (13.1, False), (11.9, True), (14.2, True),
    (13.0, True), (12.8, False), (13.3, True)
]

# Irrelevant backup data (distractor)
backup_logs = [
    {'id': 101, 'status': 'corrupted'},
    {'id': 102, 'status': 'valid'},
    {'id': 103, 'status': 'valid'}
]

# Extract valid sensor values
valid_readings = [val for val, valid in raw_sensors if valid]

# Calculate moving average over window size 2 (not used later - misleading)
moving_averages = [
    (valid_readings[i] + valid_readings[i+1]) / 2
    for i in range(len(valid_readings)-1)
]

# Normalize readings relative to baseline (12.0)
normalized_offsets = [round(r - 12.0, 3) for r in valid_readings]

# Flag anomalies using threshold (unused path - dead code)
def detect_anomalies(data, threshold=1.0):
    return [abs(x) > threshold for x in data]

# Unused function call (distractor)
anomaly_flags = detect_anomalies(normalized_offsets, threshold=0.75)

# Compute statistical moments (some irrelevant)
mean_offset = sum(normalized_offsets) / len(normalized_offsets)
variance = sum((x - mean_offset) ** 2 for x in normalized_offsets) / len(normalized_offsets)
std_dev = variance ** 0.5
skewness = sum((x - mean_offset) ** 3 for x in normalized_offsets)
# Kurtosis not computed — red herring in comment

# Generate all pairwise interactions (set operation via combinations)
pairwise_products = {round(a * b, 3) for a, b in combinations(normalized_offsets, 2)}

# Count how many pairs exceed interaction threshold
strong_interactions = len([p for p in pairwise_products if p > 1.5])

# Apply non-linear transformation on mean
transformed_mean = abs(mean_offset) ** 2.5

# Weighted combination formula (core logic)
def compute_final_score(data):
    base = sum(data)
    penalty = len([x for x in data if x < 0]) * 0.5
    bonus = strong_interactions * 0.3
    return int(round(base * 10 + bonus - penalty + transformed_mean))

# Processed data is just normalized offsets (misleading name)
processed_data = normalized_offsets

# Critical execution point
final_score = compute_final_score(processed_data)

print(f"Result: {final_score}")