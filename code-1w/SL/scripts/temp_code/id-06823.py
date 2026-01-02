from collections import defaultdict, Counter
import math

# Simulated sensor data with noise and redundant channels
data_stream = [
    (1, [3.2, 1.5, 0.8, 4.1, 2.2]),
    (2, [3.3, 1.4, 0.9, 4.0, 2.3]),
    (3, [3.1, 1.6, 0.85, 4.2, 2.1]),
    (4, [6.0, 5.8, 5.7, 5.9, 5.85]), # anomaly spike
    (5, [3.0, 1.7, 0.88, 4.3, 2.0])
]

# Irrelevant baseline reference (distractor)
baseline_metrics = {
    'norm_factor': 2.1,
    'tolerance': 0.05,
    'calibration': [0.98, 1.02, 0.99],
    'history': []
}

# Decoy function - looks important but unused in main logic
def validate_calibration(signal):
    if not signal:
        return False
    avg = sum(signal) / len(signal)
    return abs(avg - 1.0) < 0.1

# Unused transformation map (red herring)
transform_map = defaultdict(lambda: 'unknown')
for i, tag in enumerate(['alpha', 'beta', 'gamma', 'delta', 'epsilon']):
    transform_map[i] = tag

# Real processing begins here
smoothed_readings = []
noise_floor = 0.5
anomaly_threshold = 5.0

# Signal smoothing with sliding window (relevant)
for idx, readings in data_stream:
    clean_slice = []
    for val in readings:
        if val > anomaly_threshold:
            # Clip anomalous values instead of removing
            val = anomaly_threshold
        if val >= noise_floor:
            clean_slice.append(val)
    if clean_slice:
        smoothed_readings.append((idx, sum(clean_slice) / len(clean_slice)))

# Dead code path - never executed due to prior clipping (misleading)
anomalous_events = []
for t, vals in data_stream:
    peak = max(vals)
    if peak > 10.0:  # Impossible condition (distraction)
        anomalous_events.append(t)

# Data aggregation by time bin (partially relevant)
time_bins = defaultdict(list)
for t, val in smoothed_readings:
    bin_key = t // 2
    time_bins[bin_key].append(val)

# Compute bin averages (only bin 2 is used later)
bin_averages = {}
for b, vals in time_bins.items():
    bin_averages[b] = sum(vals) / len(vals)

# Extract specific features for analysis
feature_vector = []
for b in sorted(bin_averages.keys()):
    raw_val = bin_averages[b]
    # Apply non-linear transformation
    transformed = math.log(raw_val + 1) * 1.5
    feature_vector.append(transformed)

# Simulated filter bank (some outputs are irrelevant)
filter_outputs = []
for i, fv in enumerate(feature_vector):
    if i == 0:
        filtered = fv * 0.8
    elif i == 1:
        filtered = fv * 1.2  # This one gets used
    else:
        filtered = fv * 0.5
    filter_outputs.append((i, filtered))

# Select working channel based on index logic
primary_channel = None
for i, out in filter_outputs:
    if i == 1:
        primary_channel = out
        break

# Secondary processing on selected channel
processed_data = []
cumulative_shift = 0.0

for i in range(3):
    shift = (primary_channel * 0.1) * (i + 1)
    shifted_val = primary_channel + shift + cumulative_shift
    cumulative_shift += shift
    processed_data.append(shifted_val)

# Final diagnostic algorithm (recursive refinement)
def refine_estimate(values, depth=0):
    if depth >= 2 or len(values) == 1:
        return values[0] if values else 0.0
    
    new_values = []
    for a, b in zip(values, values[1:]):
        new_values.append((a + b) / 2 * 0.95)
    
    return refine_estimate(new_values, depth + 1)

# Auxiliary statistic - looks important but unused (distractor)
mode_analysis = Counter([round(x) for x in processed_data])
frequent_mode = mode_analysis.most_common(1)

# Actual usage: analyze_signal uses slicing and recursion
def analyze_signal(signal_segment):
    if len(signal_segment) < 3:
        return sum(signal_segment)
    
    # Use slicing to isolate core segment
    core = signal_segment[1:3]  # Take middle two
    
    # Augment with derived value
    derived = math.sqrt(core[0] * core[1])
    extended = core + [derived]
    
    # Final computation chain
    total = 0.0
    for i, val in enumerate(extended):
        if i == 0:
            total += val * 1.1
        elif i == 1:
            total += val * 0.9
        else:
            total += val * 1.05
    
    # Final adjustment using enumerate pattern
    adjustments = [0.1, -0.05, 0.02]
    for j, adj in enumerate(adjustments):
        if j < len(extended):
            total -= adj * extended[j]
    
    return total

# Critical execution point
final_diagnostic = analyze_signal(processed_data)

print(f"Result: {final_diagnostic}")