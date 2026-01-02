from collections import defaultdict, Counter

# Simulated sensor array data from environmental monitoring station
data_stream = [
    (101, 'temp', 23.5), (102, 'humidity', 45.2), (103, 'temp', 24.1),
    (104, 'co2', 410), (105, 'temp', 22.8), (106, 'humidity', 47.3),
    (107, 'co2', 395), (108, 'temp', 25.6), (109, 'humidity', 44.1),
    (110, 'co2', 420), (111, 'temp', 26.3), (112, 'humidity', 48.7),
    (113, 'co2', 435), (114, 'temp', 24.9), (115, 'humidity', 46.5)
]

# Irrelevant mapping - not used in final computation
deprecated_mapping = {
    't': 'temperature',
    'h': 'humid',
    'c': 'carbon'
}

# Misleading intermediate aggregation (dead-end analysis)
raw_aggregates = defaultdict(list)
for sid, stype, reading in data_stream:
    raw_aggregates[stype].append(reading)

# Distractor: complex but unused statistical summary
distractor_stats = {}
for k, v in raw_aggregates.items():
    mean_val = sum(v) / len(v)
    variance = sum((x - mean_val) ** 2 for x in v) / len(v)
    distractor_stats[k] = {'mean': mean_val, 'variance': variance, 'peak': max(v)}

# Real processing begins: filter only high-frequency temp readings above ID 105
filtered_data = [item for item in data_stream if item[1] == 'temp' and item[0] > 105]

# Another red herring: co2 trend analysis (not connected to output)
co2_readings = [r for s, t, r in data_stream if t == 'co2']
trend_pairs = [(co2_readings[i+1] - co2_readings[i]) for i in range(len(co2_readings)-1)]
potential_spike = any(t > 20 for t in trend_pairs)
spike_count = sum(1 for t in trend_pairs if t > 15)  # Unused

# Threshold configuration map - actually used
threshold_map = defaultdict(lambda: 0)
threshold_map['temp_critical'] = 25.0
threshold_map['temp_warning'] = 24.0

# Decoy function that looks important but isn't called
def analyze_pattern(sequence):
    count = 0
    for i in range(len(sequence) - 1):
        if sequence[i] < sequence[i+1]:
            count += 1
    return count if count % 2 else count // 2

# Auxiliary function with slicing distraction
def smooth_signal(signal, window=3):
    if len(signal) < window:
        return signal
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window + 1)
        end = min(len(signal), i + 1)
        window_avg = sum(signal[start:end]) / (end - start)
        smoothed.append(round(window_avg, 2))
    return smoothed[::1]  # Redundant slice operation

# Process function that actually computes the answer
def process_readings(readings, thresholds):
    # Extract values and sort by sensor ID (descending)
    values = sorted([r for _, _, r in readings], reverse=True)
    
    # Apply smoothing (distractor, but still executed)
    smoothed_vals = smooth_signal(values)
    
    # Count how many exceed warning vs critical thresholds
    warning_count = 0
    critical_count = 0
    for val in smoothed_vals:
        if val >= thresholds['temp_critical']:
            critical_count += 1
        elif val >= thresholds['temp_warning']:
            warning_count += 1
    
    # Compute weighted diagnostic score
    base_score = sum(smoothed_vals[:3])  # Top 3 values
    penalty = critical_count * 10 + warning_count * 3
    adjustment_factor = 0.85 if potential_spike else 1.0  # potential_spike is defined earlier
    
    # Final computation
    result = (base_score - penalty) * adjustment_factor
    return int(round(result))

# Key statement
final_diagnostic = process_readings(filtered_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")