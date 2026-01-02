from collections import defaultdict, Counter
import math

# Simulated sensor array data with noise and redundant channels
data_stream = [
    (1, 15.2), (2, 14.8), (3, 16.1), (4, 15.0), (5, 15.3),
    (6, 14.9), (7, 15.4), (8, 15.1), (9, 15.2), (10, 15.0)
]

# Irrelevant diagnostic thresholds (red herring)
system_thresholds = {
    'voltage': (110, 240),
    'current_rms': (0.5, 3.0),
    'thermal_limit': 85.0
}

# Misleading intermediate calculations (distractor)
avg_power_draw = 120.5
peak_load = max([x[1] for x in data_stream]) * 7.8  # Not used later
baseline_shift = sum([x[1] for x in data_stream]) / len(data_stream) - 0.3

# Real processing begins: extract time-series values
readings = [value for _, value in data_stream]

# Apply smoothing filter (relevant)
smoothed = []
for i in range(len(readings)):
    if i == 0:
        smoothed.append(readings[i])
    else:
        smoothed.append(0.7 * readings[i] + 0.3 * smoothed[i-1])

# Compute moving variance (partially relevant, but only last value matters)
variance_window = []
for i in range(1, len(smoothed)):
    diff = smoothed[i] - smoothed[i-1]
    variance_window.append(diff ** 2)

if len(variance_window) > 0:
    avg_variance = sum(variance_window) / len(variance_window)
else:
    avg_variance = 0

# Noise floor estimation (irrelevant - looks important but unused)
noise_floor = math.sqrt(avg_variance) * 0.577
confidence_damping = 1.0 / (1.0 + noise_floor) if noise_floor > 0 else 1.0

# Begin actual signal integrity analysis
anomaly_flags = []
for val in smoothed:
    if val < 15.0 or val > 15.5:
        anomaly_flags.append(True)
    else:
        anomaly_flags.append(False)

flag_count = sum(1 for f in anomaly_flags if f)
detection_rate = flag_count / len(anomaly_flags)

# Bit manipulation decoy (looks critical but irrelevant)
status_word = 0b10101010
masked_word = status_word & 0b11110000
shifted_diag = masked_word >> 4
parity_check = bin(shifted_diag).count('1') % 2

# Data structure cross-reference distraction
counter_log = Counter()
for i, val in enumerate(smoothed):
    band = int(val) // 0.5  # Quantize
    counter_log[f'band_{band}'] += 1

# Unused nested dictionary aggregation (dead path)
summary_tree = defaultdict(lambda: defaultdict(int))
for val in readings:
    key1 = f'range_{int(val)}'
    key2 = f'bucket_{int((val % 1) * 10)}'
    summary_tree[key1][key2] += 1

# Actual critical computation chain starts here
raw_aggregate = sum(smoothed) * 1.05

# Conditional adjustment based on trend (only one branch is ever taken)
trend_direction = 0
for i in range(1, len(smoothed)):
    if smoothed[i] > smoothed[i-1]:
        trend_direction += 1
    elif smoothed[i] < smoothed[i-1]:
        trend_direction -= 1

if trend_direction > 0:
    adjustment_multiplier = 1.1
elif trend_direction < 0:
    adjustment_multiplier = 0.9
else:
    adjustment_multiplier = 1.0

adjusted_total = raw_aggregate * adjustment_multiplier

# Secondary correction using statistical mode (actual relevance)
mode_result = Counter([round(x, 1) for x in smoothed]).most_common(1)[0][1]
mode_based_weight = mode_result * 0.2

# Key intermediate result (used later)
consistency_score = len(smoothed) - flag_count

# Decoy function that is never called
def compute_robust_median(values):
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    if n % 2 == 1:
        return sorted_vals[n//2]
    else:
        return (sorted_vals[n//2-1] + sorted_vals[n//2]) / 2.0

# Another red-herring algorithm: circular buffer simulation (unused)
circular_buffer = [0]*8
buffer_ptr = 0
for val in readings[:5]:
    circular_buffer[buffer_ptr] = val * 0.95
    buffer_ptr = (buffer_ptr + 1) % 8

# Final computation components
aggregate_score = consistency_score * 100 + mode_based_weight * 10

correction_factor = 0.85
offset_value = 17.3

# CRITICAL STATEMENT: target execution point
final_diagnostic = aggregate_score * correction_factor + offset_value

print(f"Result: {final_diagnostic}")