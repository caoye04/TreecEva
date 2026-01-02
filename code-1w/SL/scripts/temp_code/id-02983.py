from collections import defaultdict
import math

# Simulated sensor data acquisition (distractor: some sensors are inactive)
sensor_ids = ['S1', 'S2', 'S3', 'S4', 'S5']
raw_readings = {
    'S1': [1.2, 1.5, 1.1, 1.8, 2.0],
    'S2': [0.0, 0.0, 0.0],  # Malfunctioning sensor (red herring)
    'S3': [3.1, 2.9, 3.3, 3.0],
    'S4': [],  # Empty readings (decoy)
    'S5': [4.5, 4.7, 4.6]
}

# Irrelevant calibration function (dead code path)
def calibrate_sensor(signal, factor=1.1):
    return [x * factor for x in signal]  # Never actually used

# Noise filter using median (relevant preprocessing)
def reduce_noise(data):
    if len(data) == 0:
        return 0.0
    sorted_data = sorted(data)
    mid = len(sorted_data) // 2
    median = sorted_data[mid] if len(sorted_data) % 2 == 1 else (sorted_data[mid-1] + sorted_data[mid]) / 2
    return round(sum([abs(x - median) for x in data]) / len(data), 3)

# Secondary irrelevant metric (distractor)
def compute_entropy(data):
    if len(data) == 0:
        return 0.0
    counts = defaultdict(int)
    for x in data:
        rounded = round(x, 1)
        counts[rounded] += 1
    total = len(data)
    return round(-sum((cnt/total) * math.log2(cnt/total) for cnt in counts.values()), 3)

# Core processing: extract diagnostic magnitude
processed_data = {}
for sid in sensor_ids:
    raw = raw_readings[sid]
    if len(raw) > 0 and max(raw) > 0.5:  # Filter non-trivial signals
        noise_level = reduce_noise(raw)
        avg = sum(raw) / len(raw)
        peak = max(raw)
        # Distractor computation with unused intermediate
        stability = (1 / (1 + noise_level)) if noise_level > 0 else 1.0
        entropy = compute_entropy(raw)  # Computed but not used later
        processed_data[sid] = {
            'average': avg,
            'peak': peak,
            'variance_proxy': noise_level,
            'weight': len(raw)
        }

# Threshold configuration map (used in final analysis)
threshold_map = defaultdict(lambda: 1.0)
threshold_map.update({
    'S1': 0.8, 'S2': 0.5, 'S3': 1.2, 'S4': 0.6, 'S5': 1.4
})

# Decoy aggregation (never called)
aggregation_modes = ['avg', 'max', 'median']
lambda_weight = lambda w, m: w * 1.2 if m == 'S5' else w * 0.8

# Main analysis logic
accumulated_score = 0.0
def analyze_signal(data_dict, thresholds):
    base_score = 0
    adjustment_factor = 1.0
    
    # Irrelevant sorting (distraction)
    sorted_sensors = sorted(data_dict.keys(), key=lambda k: data_dict[k]['average'])
    
    for sensor in sorted_sensors:
        entry = data_dict[sensor]
        t = thresholds[sensor]
        
        # Real contribution to score
        if entry['peak'] > t:
            contribution = entry['average'] * entry['weight']
            if sensor == 'S3':
                contribution *= 1.5  # Special multiplier
            base_score += int(contribution)
        
        # Dead branch (misleading)
        if entry['variance_proxy'] < 0.3:
            adjustment_factor *= 1.05
    
    # Final transformation
    final_value = int(base_score * adjustment_factor)
    return final_value

# Execution point of interest
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Output result as required
print(f"Result: {final_diagnostic}")