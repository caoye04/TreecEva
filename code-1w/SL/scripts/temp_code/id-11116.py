import math

# Simulated sensor array data (irrelevant in part)
sensor_readings = [0.88, 0.91, 0.85, 0.76, 0.99, 0.64, 0.72]
dummy_weights = [1.1, 0.9, 1.2, 0.8, 1.0, 1.3, 0.7]
weighted_sum = sum([a * b for a, b in zip(sensor_readings, dummy_weights)])
normalized_power = weighted_sum / len(sensor_readings)

# Irrelevant signal smoothing block (dead path)
if normalized_power > 1.0:
    smoothed = [x * 0.95 for x in sensor_readings]
elif normalized_power < 0.7:
    smoothed = [x * 1.05 for x in sensor_readings]
else:
    pass  # No effect

# Core diagnostic engine setup
base_thresholds = {'t1': 0.8, 't2': 0.88, 't3': 0.75}
threshold_map = {k: v * 1.05 if k != 't3' else v * 0.95 for k, v in base_thresholds.items()}

# Data ingestion buffer with red herring transformations
raw_events = [12, 15, 10, 18, 22, 14, 19, 11]
event_flags = [e % 2 == 0 for e in raw_events]
flag_distribution = {True: event_flags.count(True), False: event_flags.count(False)}
adjusted_events = [e + 2 if e < 15 else e - 1 for e in raw_events]  # Distractor

# Aggregation logic with conditional expression
aggregate_buffer = []
for idx, val in enumerate(raw_events):
    if idx % 3 == 0:
        transformed = int(math.sqrt(val) * 10)
    elif idx % 3 == 1:
        transformed = int(val ** 0.5 * 8) if val > 12 else val + 5
    else:
        transformed = val * 2 // 3
    
    # Conditional expression used here (required feature)
    capped = transformed if transformed <= 16 else 16
    aggregate_buffer.append(capped)

# Misleading intermediate analysis (distractor)
outlier_count = 0
for x in aggregate_buffer:
    if x == 16:
        outlier_count += 1
    elif x < 5:
        outlier_count += 2

# Unused function (decoy)
def analyze_anomaly_pattern(seq):
    return [i for i, x in enumerate(seq) if x % 4 == 0]

# Critical processing function
previous_result = None
def process_metrics(data, thresholds):
    global previous_result
    t1, t2, t3 = thresholds['t1'], thresholds['t2'], thresholds['t3']
    
    # First stage filter
    stage1 = [x for x in data if x >= t1]
    if not stage1:
        return -1
        
    # Second stage weighting
    stage2 = []
    for val in data:
        if val > t2:
            stage2.append(val * 1.1)
        elif val > t3:
            stage2.append(val * 1.05)
        else:
            stage2.append(val)
    
    # Third stage consolidation
    total = 0
    for v in stage2:
        if v > 15:
            total += int(v - 5)
        elif v > 10:
            total += int(v)
        else:
            total += int(v * 0.8)
    
    # Final adjustment with early return possibility
    if total > 100:
        previous_result = total
        return total - 10
    elif total > 80:
        return total + 5
    else:
        return total

# Execute critical statement
interim_check = sum(aggregate_buffer) / len(aggregate_buffer)
final_diagnostic = process_metrics(aggregate_buffer, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")