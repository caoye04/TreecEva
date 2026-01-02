import math

# Sensor calibration constants (irrelevant to final result)
CALIBRATION_OFFSET = 0.023
LINEARITY_CORRECTION = [1.01, 0.99, 1.005, 1.02]

# System thresholds for diagnostics
BASELINE_SENSITIVITY = 42
DEGRADATION_FACTOR = 0.88

# Simulated raw sensor inputs (some are decoys)
raw_readings = [
    [18, 22, 25, 30, 45],
    [15, 20, 25, 40, 60],
    [10, 18, 28, 35, 50],
    [12, 24, 36, 48, 60],
    [14, 21, 28, 35, 42]
]

# Irrelevant statistical counters (distractors)
total_observations = sum(len(row) for row in raw_readings)
avg_length = total_observations / len(raw_readings)
variance_proxy = 0
for row in raw_readings:
    mean_val = sum(row) / len(row)
    variance_proxy += sum((x - mean_val) ** 2 for x in row)

# Hidden pattern: only rows where sum > 100 matter
filtered_groups = [row for row in raw_readings if sum(row) > 100]

# Transform each valid group using non-linear scaling
processed_data = []
for group in filtered_groups:
    scaled = [math.log(x) * 2.1 for x in group if x > 20]  # Only values > 20 contribute
    if len(scaled) >= 3:
        processed_data.append(scaled)

# Decoy mapping (unused)
status_codes = {
    'OK': 200,
    'WARNING': 302,
    'CRITICAL': 500
}

# Real threshold logic
threshold_map = {
    'low': BASELINE_SENSITIVITY * 0.7,
    'high': BASELINE_SENSITIVITY * DEGRADATION_FACTOR
}

# Secondary decoy calculation (dead path)
efficiency_ratio = 0.0
if len(raw_readings) > 3:
    flat = [item for sublist in raw_readings for item in sublist]
    efficiency_ratio = sum(1 for x in flat if x % 5 == 0) / len(flat)

# Unused recursive function (red herring)
def calculate_depth(node_value, depth=0):
    if node_value < 10:
        return depth
    return calculate_depth(node_value / 1.8, depth + 1)

# Core analysis logic
compliance_count = 0
for series in processed_data:
    for val in series:
        # Only values above high threshold contribute
        if val > threshold_map['high']:
            compliance_count += int(val // 3)  # Integer division contribution

# Another irrelevant transformation
checksum = sum(math.ceil(x[0]) for x in raw_readings if len(x) == 5) % 97

# Final diagnostic depends only on compliance_count and fixed offset
intermediate = compliance_count + 17

# Critical execution point
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Simulate function definition after usage (to test reasoning continuity)
def analyze_readings(data, thresholds):
    count = 0
    for seq in data:
        for v in seq:
            if v > thresholds['high']:
                count += int(v // 3)
    return count + 17

print(f"Result: {final_diagnostic}")