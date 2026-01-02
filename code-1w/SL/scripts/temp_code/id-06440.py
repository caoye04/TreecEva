def analyze_pattern(seq):
    """Irrelevant helper function for signal processing (dead code path)"""
    return sum(x ** 2 for x in seq if x > 0) - len(seq)


def validate_entry(record):
    """Unused validation function (distractor)"""
    return all(isinstance(r, (int, float)) and r >= 0 for r in record)


def transform_coordinates(data):
    """Geospatial decoy transformation (irrelevant)"""
    transformed = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            transformed.append(val * 1.5 + 3)
        else:
            transformed.append(val // 2 - 1)
    return transformed

# Irrelevant global constants (red herrings)
MAX_BUFFER_SIZE = 1024
DEFAULT_TIMEOUT = 30.5
RETRY_LIMIT = 3

# Core data structures with mixed relevance
raw_readings = [180, 95, 142, 77, 201, 65, 118, 88]
filter_mask = [x > 80 for x in raw_readings]  # Used indirectly

# Misleading intermediate computation (partially unused)
cumulative_score = 0
for i, reading in enumerate(raw_readings):
    if filter_mask[i]:
        cumulative_score += reading * (i + 1)

# Distractor: unused aggregation
temp_aggregate = [raw_readings[i] for i in range(len(raw_readings)) if i % 3 == 0]
weighted_sum = sum(temp_aggregate) * 0.9  # Dead computation

# Real work begins: health monitoring logic
baseline = [70, 80, 120, 90, 200, 60, 110, 80]
thresholds = {'critical': 190, 'warning': 150, 'normal': 90}
signal_peaks = [raw_readings[i] for i in range(len(raw_readings)) if raw_readings[i] > baseline[i]]

# Bit manipulation decoy
encoded_flags = 0
for val in signal_peaks:
    encoded_flags ^= (val & 255) >> 2

# Actual relevant logic chain
adjustment_factor = 1.75
metric_history = []

for idx, (current, ref) in enumerate(zip(raw_readings, baseline)):
    deviation = current - ref
    if deviation > thresholds['warning']:
        adjusted_dev = deviation * adjustment_factor
    elif deviation > thresholds['normal']:
        adjusted_dev = deviation * 1.2
    else:
        adjusted_dev = max(deviation, 0) * 0.8
    metric_history.append(round(adjusted_dev, 3))

# Secondary processing with slicing
recent_trend = metric_history[2:6]
evaluation_windows = []

for i in range(len(recent_trend) - 1):
    window_val = recent_trend[i] + recent_trend[i+1]
    evaluation_windows.append(window_val)

# Conditional branching with early exit pattern
trigger_count = 0
for val in metric_history:
    if val > 30:
        trigger_count += 1
        if trigger_count >= 3:
            break

# Key variable construction
aggregate_risk = sum(evaluation_windows)

# Decoy string processing (irrelevant)
diagnostic_log = "ERR_301, CHK_412, NET_205"
log_codes = diagnostic_log.split(', ')
error_count = len([c for c in log_codes if c.startswith('ERR')])

# Final computation that depends on prior state
scaling_factor = len(signal_peaks) / (trigger_count + 1)
interim_result = aggregate_risk * scaling_factor

# Main answer variable
final_diagnostic = int(interim_result + encoded_flags)  # encoded_flags adds subtle distraction

print(f"Result: {final_diagnostic}")