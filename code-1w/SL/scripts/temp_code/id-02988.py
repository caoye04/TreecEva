import math

# Sensor simulation data (irrelevant but realistic-looking)
sensor_ids = ['S1', 'S2', 'S3', 'S4']
base_offsets = {'S1': 12.5, 'S2': -8.3, 'S3': 15.0, 'S4': 0.0}
calibration_matrix = [[1.01, 0.02], [0.03, 0.99]]

# Irrelevant helper function (dead code path)
def legacy_calibrate(x):
    return x * 0.97 + 0.5  # Unused in execution

# Real processing begins here
raw_readings = [
    [100, 105, 98, 110, 102],
    [200, 195, 205, 190, 210],
    [50, 53, 49, 55, 51],
    [300, 295, 305, 290, 310]
]

# Distractor: unused transformation
temp_normalized = [[v / max(row) for v in row] for row in raw_readings]

# Actual signal filtering
filtered_readings = []
for i, series in enumerate(raw_readings):
    smoothed = []
    for j in range(len(series)):
        window = series[max(0, j-1):min(j+2, len(series))]
        avg = sum(window) / len(window)
        if j % 2 == 0:
            avg = math.ceil(avg)  # Minor deterministic manipulation
        smoothed.append(avg)
    filtered_readings.append(smoothed)

# Distractor: unused statistical analysis
variance_map = {}
for idx, series in enumerate(filtered_readings):
    mean_val = sum(series) / len(series)
    variance = sum((x - mean_val) ** 2 for x in series) / len(series)
    variance_map[sensor_ids[idx]] = round(variance, 3)

# Threshold configuration (critical)
threshold_map = {
    'S1': {'low': 90, 'high': 110},
    'S2': {'low': 180, 'high': 220},
    'S3': {'low': 45, 'high': 60},
    'S4': {'low': 280, 'high': 320}
}

# Process engine with multiple concepts
status_flags = set()
diagnostic_log = []

processed_data = {}
for sensor_idx in range(len(sensor_ids)):
    sid = sensor_ids[sensor_idx]
    readings = filtered_readings[sensor_idx]
    
    # Extract key features
    peak = max(readings)
    trough = min(readings)
    stable_count = sum(1 for r in readings if threshold_map[sid]['low'] <= r <= threshold_map[sid]['high'])
    
    # Compute stability ratio (used later)
    stability_ratio = stable_count / len(readings)
    
    # Bit manipulation red herring
    encoded_status = (sensor_idx << 4) | int(stability_ratio * 10)
    status_flags.add(encoded_status)
    
    # Store processed series
    processed_data[sid] = {
        'peak': peak,
        'trough': trough,
        'stability': stability_ratio,
        'readings': readings
    }
    
    # Logging distraction
    diagnostic_log.append(f"Sensor {sid}: {stability_ratio:.2f} stable")

# Decoy analysis function (not used)
def quick_diagnose(data_dict):
    return sum(int(v['stability'] > 0.7) for v in data_dict.values()) * 100

# Real analysis function
prev_results = []  # Unused accumulator (distractor)

def analyze_readings(data, thresholds):
    total_score = 0
    penalty = 0
    
    # String-based mode detection (required python feature)
    mode_indicator = "".join([k for k in data.keys() if data[k]['stability'] > 0.5])
    
    if 'S1' in mode_indicator and 'S3' in mode_indicator:
        total_score += 100
    
    # Dictionary traversal with logic chain
    for sensor_id, metrics in data.items():
        t = thresholds[sensor_id]
        
        # Primary evaluation logic
        if metrics['peak'] > t['high']:
            excess = metrics['peak'] - t['high']
            penalty += int(excess // 5)
        
        if metrics['trough'] < t['low']:
            deficit = t['low'] - metrics['trough']
            penalty += int(deficit // 4)
        
        # Set operation distraction (required feature)
        recent_alarms = {'S1', 'S3', 'S4'}
        historical_faults = {'S2', 'S3'}
        if sensor_id in (recent_alarms & historical_faults):
            penalty += 1  # Minor additional penalty
        
        # Conditional scoring based on stability
        if metrics['stability'] > 0.8:
            total_score += 25
        elif metrics['stability'] > 0.6:
            total_score += 15
        else:
            total_score += 5
    
    # Final computation
    final_value = total_score - (penalty * 3)
    
    # String formatting distractor
    report_key = f"DIAG-{''.join(sorted(data.keys()))}-{len(mode_indicator)}"
    
    return final_value

# Execution point of interest
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")