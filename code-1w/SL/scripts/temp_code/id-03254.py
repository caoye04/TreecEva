from collections import defaultdict
import math

# Simulated sensor data stream with noise and metadata
raw_signals = [
    {'id': 'S1', 'values': [1.2, -0.5, 3.1, 2.8], 'type': 'temp', 'active': True},
    {'id': 'S2', 'values': [0.1, 0.3, 0.4, 0.2], 'type': 'pressure', 'active': True},
    {'id': 'S3', 'values': [5.5, -2.3, 4.7, 6.1], 'type': 'temp', 'active': False},
    {'id': 'S4', 'values': [1.1, 0.9, 1.3, 1.0], 'type': 'pressure', 'active': True}
]

# Irrelevant baseline metrics (distractor)
baseline_metrics = {
    'calibration_offset': 0.05,
    'last_updated': '2023-11-05',
    'version': 'v2.3'
}

# Decoy function that looks important but isn't used in critical path
def legacy_calibrate(signal):
    return [x * 0.98 for x in signal]

# Unused transformation map (red herring)
transformation_matrix = [
    [0.7, 0.3],
    [0.4, 0.6]
]

# Preprocess: filter active sensors and extract values by type
sensor_groups = defaultdict(list)
for entry in raw_signals:
    if entry['active']:
        clean_values = [abs(x) for x in entry['values'] if x != -999]  # Remove sentinel value (not present)
        sensor_groups[entry['type']].append(clean_values)

# Compute aggregate stats (some are distractions)
stats_summary = {}
total_entries = 0
for s_type, datasets in sensor_groups.items():
    all_vals = [val for ds in datasets for val in ds]
    stats_summary[s_type] = {
        'peak': max(all_vals),
        'baseline_rms': math.sqrt(sum(x**2 for x in all_vals) / len(all_vals)),
        'count': len(all_vals)
    }
    total_entries += len(all_vals)

# Dummy normalization (irrelevant to final result)
normalized_readings = []
scaling_factor = stats_summary.get('temp', {}).get('baseline_rms', 1.0)
for t_group in sensor_groups.get('temp', []):
    normalized_readings.extend([x / scaling_factor for x in t_group])

# Construct threshold map based on heuristics (used later)
threshold_map = {}
for s_type in sensor_groups:
    ref_val = stats_summary[s_type]['peak']
    if s_type == 'temp':
        threshold_map[s_type] = ref_val * 0.65
    else:
        threshold_map[s_type] = ref_val * 0.45

# Intermediate diagnostic flags (mix of relevant and irrelevant)
diagnostic_flags = []
if stats_summary['temp']['count'] > 5:
    diagnostic_flags.append(1)
else:
    diagnostic_flags.append(0)

diagnostic_flags.append(1 if stats_summary['pressure']['peak'] > 1.0 else 0)

def process_entry(data_list):
    # Apply moving average filter (only some results matter)
    filtered = []
    for series in data_list:
        smooth = []
        for i in range(len(series)):
            window = series[max(0, i-1):i+2]
            avg = sum(window) / len(window)
            smooth.append(avg)
        filtered.append(smooth)
    
    # Flatten and compute characteristics
    flat = [item for sublist in filtered for item in sublist]
    extremes = [x for x in flat if x > 1.5]
    
    # Return only the count of extreme values (key contribution)
    return len(extremes)

# Process each group
processed_data = {}
for s_type, datasets in sensor_groups.items():
    processed_data[s_type] = process_entry(datasets)

# Dead code path - never executed but looks like it could be
if __debug__:
    consistency_check = sum(processed_data.values()) % 2 == 0

# Core analysis function combining multiple concepts
def analyze_signal(data, thresholds):
    result = 0
    for s_type, count in data.items():
        thresh = thresholds.get(s_type, 1.0)
        # Integer division and conditional logic
        contribution = count // int(thresh + 0.5) if thresh > 0 else count
        if s_type == 'temp':
            # Additional bit manipulation twist
            contribution = contribution ^ 3  # XOR with constant
        result += contribution
    
    # Final adjustment using logical operations
    multiplier = 2 if (result > 5) and (result % 2 == 1) else 1
    return result * multiplier

# Execute main analysis
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")