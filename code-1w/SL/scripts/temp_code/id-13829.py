from collections import defaultdict, Counter
import math

# Simulated IoT sensor fusion system for environmental health monitoring
def preprocess_readings(raw_readings):
    processed = []
    noise_floor = 0.041
    calibration_offset = 0.008
    for val in raw_readings:
        if abs(val) < noise_floor:
            val = 0
        corrected = round(val + calibration_offset, 3)
        processed.append(corrected)
    return processed

# Irrelevant signal smoothing function (dead code path)
def smooth_signal(data, window=3):
    smoothed = []
    for i in range(len(data)):
        start = max(0, i - window // 2)
        end = min(len(data), i + window // 2 + 1)
        smoothed.append(sum(data[start:end]) / (end - start))
    return smoothed

# Core diagnostic engine
def compute_thermal_index(readings):
    if not readings:
        return 0.0
    weighted_sum = sum(idx * val ** 1.5 for idx, val in enumerate(readings, 1))
    normalization_factor = sum(idx for idx in range(1, len(readings) + 1))
    return round(weighted_sum / normalization_factor, 4)

# Secondary metric calculator (partially relevant)
def analyze_variability(readings):
    mean_val = sum(readings) / len(readings)
    variance = sum((x - mean_val) ** 2 for x in readings) / len(readings)
    variability_score = math.sqrt(variance)
    category = 'low'
    if variability_score > 0.15:
        category = 'high'
    elif variability_score > 0.08:
        category = 'moderate'
    return variability_score, category

# Distractor: Unused fault detection heuristic
def detect_anomalies(log_data):
    anomalies = []
    for i, entry in enumerate(log_data):
        if isinstance(entry, dict) and 'voltage' in entry:
            if entry['voltage'] < 2.1 or entry['voltage'] > 3.3:
                anomalies.append(i)
    return anomalies

# Main aggregation logic
def aggregate_metrics(sensor_log, thresholds):
    # Extract temperature channel
    temp_readings = [entry['temp'] for entry in sensor_log if 'temp' in entry]
    
    # Preprocess with noise filtering
    clean_temps = preprocess_readings(temp_readings)
    
    # Compute primary index
    thermal_index = compute_thermal_index(clean_temps)
    
    # Compute auxiliary metrics (only one used)
    variability_score, var_category = analyze_variability(clean_temps)
    
    # Red herring: unused spatial correlation
    spatial_pattern = [abs(clean_temps[i] - clean_temps[i-1]) for i in range(1, len(clean_temps))]
    pattern_entropy = 0.0
    if spatial_pattern:
        counts = Counter([round(p, 2) for p in spatial_pattern])
        pattern_entropy = -sum((count/len(counts)) * math.log2(count/len(counts)) for count in counts.values())
    
    # Threshold evaluation
    baseline = thresholds['base_reference']
    tolerance = thresholds['fluctuation_cap']
    
    # Diagnostic decision tree
    if thermal_index > baseline + tolerance:
        severity = 3
    elif thermal_index > baseline + tolerance * 0.5:
        severity = 2
    elif thermal_index > baseline - tolerance:
        severity = 1
    else:
        severity = 0
    
    # Final computation - only this output matters
    adjustment_factor = thresholds['scaling_factor']
    final_diagnostic = int((thermal_index * adjustment_factor + severity * 17) * 100)
    
    # Decoy derived values
    phantom_metric = sum(1 for x in clean_temps if x > 0.1) * len(spatial_pattern)
    ghost_ratio = (pattern_entropy + 0.01) / (variability_score + 0.01) if variability_score else 0
    
    return final_diagnostic

# Simulated sensor log data (mixed format)
health_log = [
    {'temp': 0.12, 'humidity': 43.2, 'node': 'A1'},
    {'temp': 0.09, 'voltage': 2.8, 'node': 'A2'},
    {'temp': 0.15, 'timestamp': 1718870400, 'node': 'A3'},
    {'temp': 0.08, 'humidity': 45.1, 'node': 'A4'},
    {'temp': 0.14, 'voltage': 3.1, 'node': 'A5'},
    {'temp': 0.11, 'timestamp': 1718870460, 'node': 'A6'},
    {'temp': 0.16, 'humidity': 42.8, 'node': 'A7'},
    {'temp': 0.07, 'voltage': 2.9, 'node': 'A8'}
]

# Threshold configuration map
threshold_map = {
    'base_reference': 0.11,
    'fluctuation_cap': 0.035,
    'scaling_factor': 8.5,
    'base_margin': 0.012
}

# Execute main computation
final_diagnostic = aggregate_metrics(health_log, threshold_map)
print(f"Result: {final_diagnostic}")