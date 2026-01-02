from collections import defaultdict, Counter
from itertools import zip_longest

# Simulated sensor input data (real-world context: environmental monitoring system)
sensor_readings = [
    [23.4, 24.1, 25.0, 26.5, 27.3],
    [19.8, 20.5, None, 21.3, 22.0],
    [30.2, None, 31.5, 32.1, 33.0],
    [18.5, 19.0, 19.7, None, 20.4]
]

# Irrelevant auxiliary mapping (distractor - not used in final calculation)
sensor_names = ['temp_A', 'temp_B', 'temp_C', 'temp_D']
sensor_map = {idx: name for idx, name in enumerate(sensor_names)}

# Preprocessing: clean and align time-series data
cleaned_data = []
for readings in sensor_readings:
    filled = []
    last_valid = 0
    for val in readings:
        if val is not None:
            last_valid = val
        else:
            last_valid += 0.7  # Simple interpolation heuristic
        filled.append(last_valid)
    cleaned_data.append(filled)

# Compute rolling trends (moving average over window size 3)
trend_data = []
for series in cleaned_data:
    rolling_avg = []
    for i in range(2, len(series)):
        avg = (series[i-2] + series[i-1] + series[i]) / 3
        rolling_avg.append(round(avg, 2))
    trend_data.append(rolling_avg)

# Baseline calibration from historical reference (mock data)
baseline = {
    'ref_year': 2023,
    'values': [24.5, 25.1, 26.0, 26.8, 27.5]
}

# Spurious transformation chain (dead path - looks important but unused)
legacy_buffer = []
for entry in cleaned_data:
    transformed = [x * 0.98 + 1.2 for x in entry]
    legacy_buffer.extend(transformed)

# Secondary metric: anomaly frequency counting (partially relevant)
anomaly_tracker = defaultdict(int)
for i, series in enumerate(cleaned_data):
    for val in series:
        if val < 20.0:
            anomaly_tracker['cold'] += 1
        elif val > 30.0:
            anomaly_tracker['hot'] += 1

# Unused statistical summary (red herring)
stats_summary = dict()
for key, count in anomaly_tracker.items():
    stats_summary[key] = {'count': count, 'severity': count * 1.5}

# Auxiliary function for metric aggregation
def aggregate_metrics(trends, base):
    flat_trends = [item for sublist in trends for item in sublist]  # Flatten all trend values
    base_vals = base['values']
    
    # Align lengths for comparison
    min_len = min(len(flat_trends), len(base_vals))
    diff_sum = 0.0
    for i in range(min_len):
        diff_sum += abs(flat_trends[i] - base_vals[i])
    
    # Incorporate length mismatch penalty
    len_diff = abs(len(flat_trends) - len(base_vals))
    return round(diff_sum + len_diff * 0.5, 2)

# Decoy function that appears related but is never called
def deprecated_aggregation(data):
    counter = Counter()
    for row in data:
        for val in row:
            bucket = int(val // 5)
            counter[bucket] += 1
    return sum(counter.values())

# Adjustment derived from environmental compensation model
compensation_factor = 0.0
for series in cleaned_data:
    for val in series:
        if val > 25.0:
            compensation_factor += 0.02
        elif val < 20.0:
            compensation_factor -= 0.01

adjustment_factor = round(compensation_factor * 1.5, 2)

# Critical statement: compute final diagnostic index
final_diagnostic = aggregate_metrics(trend_data, baseline) + adjustment_factor

# Print result for observable output
print(f"Result: {final_diagnostic}")