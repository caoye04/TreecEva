def transform_sequence(seq, factor):
    """Irrelevant transformation function (dead code path)"""
    return [x * factor + 2 for x in seq if x % 2 == 0]

# Sensor simulation parameters (mostly irrelevant)
sensor_bias = 7
offset_grid = [[1, 3], [4, 2]]
calibration_map = {k: v**2 for k, v in enumerate([3, 1, 4, 1, 5])}

# Core diagnostic data
raw_readings = [84, 92, 77, 88, 95, 72, 81, 90]
scaling_factor = 0.85

# Misleading intermediate calculation (red herring)
adjusted_scores = sum([(r - sensor_bias) * scaling_factor for r in raw_readings])

# Actual processing begins
filtered_readings = [r for r in raw_readings if r > 75]
normalized = [round(r * 0.1, 2) for r in filtered_readings]  # Scale to deci-units

# Simulate multi-sensor fusion (partly relevant)
sensor_b_offset = 3.2
fused_stream = []
for i, val in enumerate(normalized):
    if i % 2 == 0:
        fused_stream.append(val + sensor_b_offset)
    else:
        fused_stream.append(val - 0.5)

# Decoy statistical analysis (distractor)
mean_fused = sum(fused_stream) / len(fused_stream)
variance_proxy = sum((x - mean_fused) ** 2 for x in fused_stream)

# Real processing: categorize levels
level_tags = []
for f in fused_stream:
    if f < 9.0:
        level_tags.append('low')
    elif f < 12.0:
        level_tags.append('medium')
    else:
        level_tags.append('high')

# Map with enumerate and string ops (required feature)
tag_counts = {}
for idx, tag in enumerate(level_tags):
    clean_tag = tag.strip().upper()  # string method
    if clean_tag not in tag_counts:
        tag_counts[clean_tag] = 0
    tag_counts[clean_tag] += 1

# Create threshold map using dictionary operations (required)
threshold_map = {
    'HIGH': 12.0,
    'MEDIUM': 9.0,
    'LOW': 0.0
}

# Processed data construction using zip (required)
status_codes = ['OK', 'WARN', 'OK', 'CRIT']
processed_data = list(zip(fused_stream, level_tags, status_codes[:len(fused_stream)]))

# Red herring: unused recursive function
def recursive_sum(n):
    if n <= 1:
        return n
    return n + recursive_sum(n - 2)  # never called

# Core analysis function
def analyze_readings(data, thresholds):
    high_count = 0
    cumulative_drift = 0.0
    
    for reading, level, code in data:
        # Relevant logic branch
        if level == 'high' and code == 'CRIT':
            high_count += 1
        
        baseline = thresholds[level.upper()]
        drift = abs(reading - baseline)
        cumulative_drift += drift
        
        # Simulated correction (has side effect on accumulator)
        if drift > 2.0:
            cumulative_drift -= 0.3  # arbitrary compensation
    
    # Final computation
    score_component = high_count * 100
    drift_penalty = int(cumulative_drift * 10)
    return score_component - drift_penalty

# Critical execution point
final_diagnostic = analyze_readings(processed_data, threshold_map)

print(f"Target result: {final_diagnostic}")