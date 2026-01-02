from collections import defaultdict, Counter
import math

# Simulated sensor array data with noise and redundant channels
data_stream = [
    (1, [3.2, 1.5, 0.8, 4.1, 2.2]),
    (2, [3.3, 1.4, 0.9, 4.0, 2.1]),
    (3, [3.1, 99.9, 0.85, 4.2, 2.3]),  # anomaly in index 1 (noise)
    (4, [3.25, 1.6, 0.82, 4.15, 2.25]),
    (5, [3.18, 1.55, 0.88, 4.05, 2.18]),
    (6, [3.22, 1.48, 0.84, 4.12, 2.22]),
    (7, [3.21, 1.52, 0.86, 4.08, 2.21])
]

# Irrelevant metadata about sensors (distractor)
sensor_specs = {
    'range': (0, 10),
    'precision': 0.01,
    'channels': 5,
    'sampling_rate': 100
}

# Decoy function - looks important but unused
def calibrate_sensor(raw, factor=1.0):
    return [x * factor for x in raw]

# Another decoy - appears to analyze but never called
def compute_entropy(data):
    counts = Counter(data)
    total = len(data)
    return -sum((count/total) * math.log2(count/total) for count in counts.values())

# Noise detection heuristic based on z-score (used)
def is_anomaly(reading, mean, std):
    if std == 0:
        return False
    z = abs(reading - mean) / std
    return z > 3

# Aggregate function using lambda (required feature)
channel_averager = lambda readings: [sum(x[i] for x in readings) / len(readings) for i in range(len(readings[0]))]

# Misleading intermediate calculation (red herring)
total_samples = sum(len(record[1]) for record in data_stream)
avg_sample_count = total_samples / len(data_stream)
redundancy_ratio = avg_sample_count / sensor_specs['channels']  # Looks diagnostic

# Extract baseline stats per channel for anomaly filtering
baseline_values = defaultdict(list)
for timestamp, readings in data_stream:
    for i, val in enumerate(readings):
        baseline_values[i].append(val)

# Compute means and stds for filtering
channel_stats = {}
for ch, vals in baseline_values.items():
    mean = sum(vals) / len(vals)
    std = (sum((x - mean)**2 for x in vals) / len(vals))**0.5
    channel_stats[ch] = (mean, std)

# Filter out anomalous readings per channel (key processing step)
filtered_data = []
for timestamp, readings in data_stream:
    clean_readings = []
    for i, val in enumerate(readings):
        mean, std = channel_stats[i]
        if is_anomaly(val, mean, std):
            continue  # skip anomalous value
        clean_readings.append(val)
    # Only include records that have at least 3 valid channels
    if len(clean_readings) >= 3:
        filtered_data.append((timestamp, clean_readings))

# Dead code path - looks like it might be used (distractor)
consistency_flags = []
for ts, reads in filtered_data:
    if len(reads) > 4:
        consistency_flags.append(True)
    else:
        consistency_flags.append(False)

# Unused transformation map (red herring)
transform_map = {
    i: (lambda x, m=ch_m: (x - m[0]) / (m[1] + 1e-8)) 
    for i, ch_m in enumerate(channel_stats.values())
}

# Core diagnostic processor (uses filtered_data)
def process_readings(data):
    # Extract all values for global stats
    all_vals = [val for _, reads in data for val in reads]
    
    # Intermediate distractor variables
    peak = max(all_vals)
    trough = min(all_vals)
    span = peak - trough
    
    # Real computation: weighted stability index
    mean_val = sum(all_vals) / len(all_vals)
    variance = sum((x - mean_val)**2 for x in all_vals) / len(all_vals)
    stability = 1 / (1 + variance)  # higher = more stable
    
    # Apply non-linear compression
    compressed_stability = math.log1p(stability * 100)
    
    # Use Counter to count frequency of binned values (required feature)
    rounded_vals = [round(x, 1) for x in all_vals]
    freq_dist = Counter(rounded_vals)
    dominant_count = max(freq_dist.values())
    
    # Final fusion: combine stability with dominance
    final_score = compressed_stability * (dominant_count / len(all_vals))
    
    # Introduce a misleading scaling (but still deterministic)
    scaled_diagnostic = final_score * 1000
    
    # This is the actual answer variable
    final_diagnostic = int(scaled_diagnostic)  # truncate to integer
    
    return final_diagnostic

# Critical execution point
final_diagnostic = process_readings(filtered_data)

print(f"Result: {final_diagnostic}")