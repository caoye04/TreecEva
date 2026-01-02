from collections import defaultdict
import math

# Simulated sensor data with metadata tags
data_stream = [
    (102, 'temp', 'A'), (205, 'pressure', 'B'), (98, 'temp', 'A'),
    (190, 'pressure', 'B'), (301, 'flow', 'C'), (450, 'temp', 'D'),
    (89, 'temp', 'A'), (210, 'pressure', 'B'), (308, 'flow', 'C')
]

# Irrelevant baseline calibration map (distractor)
calibration_map = {
    'temp': lambda x: x * 1.02,
    'pressure': lambda x: x * 0.99,
    'flow': lambda x: x * 1.05
}

# Decoy transformation using string methods on numeric context (dead path)
metadata_tags = [tag for _, _, tag in data_stream]
concatenated = ''.join(metadata_tags)
char_frequency = {c: concatenated.count(c) for c in set(concatenated)}

# Unused recursive function (red herring)
def recursive_dampen(value, depth):
    if depth == 0 or value < 1:
        return value
    return 0.9 * recursive_dampen(value - 5, depth - 1)

# Actual processing begins here
raw_readings = [(val, sensor) for val, sensor, _ in data_stream]

# Group by sensor type using defaultdict (relevant)
sensor_groups = defaultdict(list)
for value, stype in raw_readings:
    sensor_groups[stype].append(value)

# Compute moving average for each sensor (partially relevant preprocessing)
moving_averages = {}
for stype, readings in sensor_groups.items():
    avg = sum(readings) / len(readings)
    moving_averages[stype] = round(avg, 2)

# Threshold policy based on statistical spread (key logic)
threshold_map = {}
for stype, readings in sensor_groups.items():
    mean_val = sum(readings) / len(readings)
    variance = sum((x - mean_val) ** 2 for x in readings) / len(readings)
    std_dev = math.sqrt(variance)
    # Threshold set at mean + 1.5*std_dev
    threshold_map[stype] = mean_val + 1.5 * std_dev

# Filtered data: only values above threshold (core filtering)
filtered_data = []
for val, sensor, loc in data_stream:
    if val > threshold_map[sensor]:
        filtered_data.append((val, sensor, loc))

# Secondary filter by location (adds nesting and dependency)
allowed_locations = {'A', 'C', 'D'}
filtered_data = [item for item in filtered_data if item[2] in allowed_locations]

# Real-time correction factor that isn't actually applied (distractor)
correction_factor = math.log(sum([x[0] for x in data_stream]) + 1, 10)
adjusted_values = [v * (1 + 0.01 * correction_factor) for v in [1, 2, 3]]  # unused

# Core diagnostic processor (critical function)
def process_readings(data, thresholds):
    if not data:
        return -1
    
    # Extract high-severity readings
    high_magnitude = [v for v, s, _ in data if v > 200]
    if not high_magnitude:
        return 0
    
    # Count per sensor type (list comprehension with filtering)
    type_counts = {
        stype: len([v for v, s, _ in data if s == stype])
        for stype in thresholds.keys()
    }
    
    # Compute entropy-like complexity score
    total = sum(type_counts.values())
    entropy = 0
    for count in type_counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log(p, 2)
    
    # Aggregate sum with positional weighting
    weighted_sum = 0
    for idx, (value, _, _) in enumerate(sorted(data, key=lambda x: x[0], reverse=True)):
        weighted_sum += value * (0.95 ** idx)  # decay factor
    
    # Final diagnostic: combination of entropy and weighted signal
    diagnostic_score = int(weighted_sum * entropy)
    
    # Dead code branch inside function (misleading)
    if diagnostic_score > 10000:
        backup_system = [math.sin(x) for x in range(5)]
        diagnostic_score -= sum(backup_system)
        
    return diagnostic_score

# Execute main computation
temp_snapshot = [x for x, s, _ in data_stream if s == 'temp']
pressure_snapshot = [x for x, s, _ in data_stream if s == 'pressure']

# Critical execution point
final_diagnostic = process_readings(filtered_data, threshold_map)

# Print result as required
print(f"Target result: {final_diagnostic}")